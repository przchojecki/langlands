#!/usr/bin/env python3
"""
GLC Task 2: TeX -> metadata-first claim index.

This script extracts theorem-like environments defined via \\newtheorem{...}
(e.g. thm/lem/prop/cor/defn/rem/...) from TeX sources and produces:

- atlas/glc/claims/GLC*.index.jsonl   (one claim per line)
- atlas/glc/claims/all_claims.csv    (aggregate)
- atlas/glc/claims/stats.json        (counts)

By default, it stores only a truncated 'statement_preview' plus a SHA256 hash
of the full environment body (whitespace-normalized). The TeX sources remain
the source of truth.

Usage:
  python tools/extract_glc_claims_tex.py \
    --glc1 /path/to/gaits1.tex \
    --glc2 /path/to/gaits2.tex \
    --glc3 /path/to/gaits3.tex \
    --glc4 /path/to/gaits4.tex \
    --glc5 /path/to/gaits5.tex \
    --out  atlas/glc/claims

Tip:
  If you want longer previews, pass --preview-chars 2000 (or similar).
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple


ENV_KIND_RULES = [
    ("definition", lambda env: env.startswith("def")),
    ("theorem", lambda env: "thm" in env),
    ("lemma", lambda env: "lem" in env),
    ("proposition", lambda env: env.startswith("prop")),
    ("corollary", lambda env: env.startswith("cor")),
    ("conjecture", lambda env: "conj" in env),
    ("axiom", lambda env: env == "ax"),
    ("remark", lambda env: env == "rem"),
    ("question", lambda env: env == "quest"),
    ("claim", lambda env: env == "claim"),
    ("observation", lambda env: env == "obs"),
    ("hypothesis", lambda env: env == "hypoth"),
    ("example", lambda env: env == "example"),
]


def env_to_kind(env: str) -> str:
    for kind, pred in ENV_KIND_RULES:
        if pred(env):
            return kind
    return env


def normalize_ws(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def sha256_text(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8", errors="ignore")).hexdigest()


def strip_comments_preserve_newlines(tex: str) -> str:
    """
    Remove TeX comments starting with unescaped %, preserving newline structure.
    """
    out_lines: List[str] = []
    for line in tex.splitlines(True):  # keepends
        i = 0
        cut: Optional[int] = None
        while True:
            j = line.find("%", i)
            if j == -1:
                break
            if j > 0 and line[j - 1] == "\\":
                i = j + 1
                continue
            cut = j
            break
        if cut is not None:
            # preserve newline if it existed
            out_lines.append(line[:cut] + ("\n" if line.endswith("\n") else ""))
        else:
            out_lines.append(line)
    return "".join(out_lines)


def extract_newtheorem_envs(tex: str) -> List[str]:
    pat = re.compile(r"\\newtheorem\{([^\}]+)\}")
    return pat.findall(tex)


@dataclass
class Claim:
    claim_id: str
    paper_key: str
    env: str
    kind: str
    opt_title: Optional[str]
    label: Optional[str]
    section: Optional[str]
    subsection: Optional[str]
    subsubsection: Optional[str]
    tex_file: str
    line_start: int
    line_end: int
    statement_preview: str
    statement_sha256: str

    def to_json(self) -> Dict:
        return {
            "claim_id": self.claim_id,
            "paper_key": self.paper_key,
            "env": self.env,
            "kind": self.kind,
            "opt_title": self.opt_title,
            "label": self.label,
            "section": self.section,
            "subsection": self.subsection,
            "subsubsection": self.subsubsection,
            "source": {
                "tex_file": self.tex_file,
                "line_start": self.line_start,
                "line_end": self.line_end,
            },
            "statement_preview": self.statement_preview,
            "statement_sha256": self.statement_sha256,
        }


def extract_claims_from_tex(tex_path: Path, paper_key: str, preview_chars: int) -> List[Claim]:
    raw = tex_path.read_text(encoding="utf-8", errors="ignore")
    cleaned = strip_comments_preserve_newlines(raw)

    # Start scanning after \begin{document}
    doc_token = r"\begin{document}"
    doc_start = cleaned.find(doc_token)
    if doc_start != -1:
        scan_text = cleaned[doc_start + len(doc_token) :]
        scan_offset = doc_start + len(doc_token)
    else:
        scan_text = cleaned
        scan_offset = 0

    envs = sorted(set(extract_newtheorem_envs(cleaned)))
    if not envs:
        return []

    heading_pat = re.compile(r"\\(section|subsection|subsubsection)\*?\{")
    begin_pat = re.compile(
        r"\\begin\{(" + "|".join(map(re.escape, envs)) + r")\}(?:\[(.*?)\])?"
    )

    events: List[Tuple[int, str, Dict]] = []

    # headings (best-effort; handles nested braces)
    for m in heading_pat.finditer(scan_text):
        cmd = m.group(1)
        brace_start = m.end()
        depth = 1
        i = brace_start
        while i < len(scan_text) and depth > 0:
            ch = scan_text[i]
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
            i += 1
        title = scan_text[brace_start : i - 1] if depth == 0 else scan_text[brace_start:i]
        events.append((m.start(), "heading", {"level": cmd, "title": normalize_ws(title)}))

    # theorem-like begins
    for m in begin_pat.finditer(scan_text):
        env = m.group(1)
        opt_title = normalize_ws(m.group(2)) if m.group(2) else None
        events.append((m.start(), "begin", {"env": env, "opt_title": opt_title, "begin_end": m.end()}))

    events.sort(key=lambda x: x[0])

    current = {"section": None, "subsection": None, "subsubsection": None}
    seq = 0
    claims: List[Claim] = []

    for pos, typ, data in events:
        if typ == "heading":
            level = data["level"]
            if level == "section":
                current["section"] = data["title"]
                current["subsection"] = None
                current["subsubsection"] = None
            elif level == "subsection":
                current["subsection"] = data["title"]
                current["subsubsection"] = None
            else:
                current["subsubsection"] = data["title"]
            continue

        # begin event
        env = data["env"]
        kind = env_to_kind(env)
        begin_end = data["begin_end"]

        end_pat = re.compile(r"\\end\{" + re.escape(env) + r"\}")
        end_m = end_pat.search(scan_text, begin_end)
        if not end_m:
            continue

        content = scan_text[begin_end : end_m.start()]
        abs_begin = scan_offset + pos
        abs_end = scan_offset + end_m.end()
        line_start = cleaned[:abs_begin].count("\n") + 1
        line_end = cleaned[:abs_end].count("\n") + 1

        label_m = re.search(r"\\label\{([^}]+)\}", content)
        label = label_m.group(1).strip() if label_m else None

        body_norm = normalize_ws(content)
        preview = body_norm if len(body_norm) <= preview_chars else body_norm[:preview_chars].rstrip() + "…"
        body_hash = sha256_text(body_norm)

        seq += 1
        claim_id = f"{paper_key}:{kind}:{label}" if label else f"{paper_key}:{kind}:auto{seq:04d}@L{line_start}"

        claims.append(
            Claim(
                claim_id=claim_id,
                paper_key=paper_key,
                env=env,
                kind=kind,
                opt_title=data["opt_title"],
                label=label,
                section=current["section"],
                subsection=current["subsection"],
                subsubsection=current["subsubsection"],
                tex_file=tex_path.name,
                line_start=line_start,
                line_end=line_end,
                statement_preview=preview,
                statement_sha256=body_hash,
            )
        )

    return claims


def count_by_kind(claims: List[Claim]) -> Dict[str, int]:
    out: Dict[str, int] = {}
    for c in claims:
        out[c.kind] = out.get(c.kind, 0) + 1
    # sort by count desc then key
    return dict(sorted(out.items(), key=lambda kv: (-kv[1], kv[0])))


def write_jsonl(path: Path, claims: List[Claim]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for c in claims:
            f.write(json.dumps(c.to_json(), ensure_ascii=False) + "\n")


def write_csv(path: Path, claims: List[Claim]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "claim_id",
        "paper_key",
        "env",
        "kind",
        "opt_title",
        "label",
        "section",
        "subsection",
        "subsubsection",
        "tex_file",
        "line_start",
        "line_end",
        "statement_preview",
        "statement_sha256",
    ]
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for c in claims:
            w.writerow(
                {
                    "claim_id": c.claim_id,
                    "paper_key": c.paper_key,
                    "env": c.env,
                    "kind": c.kind,
                    "opt_title": c.opt_title,
                    "label": c.label,
                    "section": c.section,
                    "subsection": c.subsection,
                    "subsubsection": c.subsubsection,
                    "tex_file": c.tex_file,
                    "line_start": c.line_start,
                    "line_end": c.line_end,
                    "statement_preview": c.statement_preview,
                    "statement_sha256": c.statement_sha256,
                }
            )


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--glc1", required=True, type=Path)
    ap.add_argument("--glc2", required=True, type=Path)
    ap.add_argument("--glc3", required=True, type=Path)
    ap.add_argument("--glc4", required=True, type=Path)
    ap.add_argument("--glc5", required=True, type=Path)
    ap.add_argument("--out", required=True, type=Path)
    ap.add_argument("--preview-chars", default=280, type=int)
    args = ap.parse_args()

    paper_inputs = {
        "GLC1": args.glc1,
        "GLC2": args.glc2,
        "GLC3": args.glc3,
        "GLC4": args.glc4,
        "GLC5": args.glc5,
    }

    all_claims: List[Claim] = []
    stats: Dict[str, Dict] = {}

    for key, path in paper_inputs.items():
        claims = extract_claims_from_tex(path, key, preview_chars=args.preview_chars)
        all_claims.extend(claims)
        stats[key] = {
            "tex_file": path.name,
            "n_claims": len(claims),
            "counts_by_kind": count_by_kind(claims),
        }
        write_jsonl(args.out / f"{key}.index.jsonl", claims)

    write_csv(args.out / "all_claims.csv", all_claims)
    (args.out / "stats.json").write_text(json.dumps(stats, indent=2, ensure_ascii=False), encoding="utf-8")

    print("Wrote:")
    for key in paper_inputs.keys():
        print(f"  - {args.out / (key + '.index.jsonl')}")
    print(f"  - {args.out / 'all_claims.csv'}")
    print(f"  - {args.out / 'stats.json'}")


if __name__ == "__main__":
    main()
