# GLC proof atlas (Task 2 output)

This folder contains **metadata-first claim indices** extracted from the uploaded TeX sources for Gaitsgory's
*Proof of the Geometric Langlands Conjecture* series (Parts I–V).

## Files

- `claims/GLC1.index.jsonl` … `claims/GLC5.index.jsonl`  
  One JSON object per claim (Definition/Lemma/Theorem/…); includes:
  - environment name and normalized kind
  - `\label{...}` when present
  - section/subsection context (best-effort heuristic)
  - TeX provenance: file + line range
  - `statement_preview` (truncated) + `statement_sha256`

- `claims/all_claims.csv`  
  Spreadsheet-friendly aggregate.

- `claims/stats.json`  
  Counts by paper/kind.

- `claims/GLC*.md`  
  Human-readable “claim cards” (metadata + preview).

## Notes / limitations

- Only theorem-like environments defined via `\newtheorem{...}` are extracted in this pass.
  Many definitions in the GLC papers appear inline and will be handled in later tasks.
- `statement_preview` is intentionally truncated; the TeX files themselves remain the source of truth.

