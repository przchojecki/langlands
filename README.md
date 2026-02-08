# Langlands Program with AI

A research repository for **LLM-assisted proof engineering** across three tightly related goals in Langlands Program:

1. **Validate + formalize the Gaitsgory(-Raskin et al.) proof of the (categorical, unramified) Geometric Langlands conjecture** (GLC).
2. **Transfer the proof architecture/techniques to local ℓ-adic Langlands** in the **Fargues–Scholze** setting (ℓ ≠ p) using the attached blueprint (ladicgeom.tex).
3. **Prototype a parallel path toward p-adic local Langlands** (ℓ = p) using the attached blueprint (padicgeom.tex).

> **Status:** research / pre-alpha.  
> **Non-goal:** “LLMs prove Langlands.” The goal is **structured validation, dependency tracking, formalization scaffolding, and human-auditable workflows**.

---

## Why this exists

The relevant proofs and frameworks are:
- **long** (hundreds of pages),
- **highly interdependent** (definitions/lemmas migrate across papers),
- **notation-heavy**,
- **spread across multiple formalisms** (D-modules / Betti sheaves / v-stacks / diamonds / IndCoh / singular support / spectral actions),
- **centerpiece** of modern mathematics.

LLMs are not trusted oracles here. We use them as:
- a *parser* (TeX → structured claims),
- a *librarian* (indexing + cross-referencing),
- a *refactoring assistant* (notation unification + “same statement, different paper” detection),
- a *formalization copilot* (Lean/Coq stubs + interface-level lemmas),
- and a *red-team tool* (spotting missing hypotheses, hidden uses of finiteness/adjointness, etc.).

Ideally we would arrive at formalization (e.g. in Lean), that would validate first Gaitsgory proof and then also show new results in local adic context.

---

## Core sources for Goal 1 (Gaitsgory proof series)

The “proof of GLC” is organized by Gaitsgory’s project page and a **five-paper series**:

- Project page (index):  
  https://people.mpim-bonn.mpg.de/gaitsgde/GLC/

- **GLC I: Construction of the functor**  
  MPIM PDF: https://people.mpim-bonn.mpg.de/gaitsgde/GLC/functor.pdf  
  arXiv: https://arxiv.org/abs/2405.03599

- **GLC II: Kac–Moody localization and the FLE**  
  MPIM PDF: https://people.mpim-bonn.mpg.de/gaitsgde/GLC/Loc.pdf  
  arXiv: https://arxiv.org/abs/2405.03648

- **GLC III: Compatibility with parabolic induction**  
  MPIM PDF: https://people.mpim-bonn.mpg.de/gaitsgde/GLC/Eis.pdf  
  arXiv: https://arxiv.org/abs/2409.07051

- **GLC IV: Ambidexterity**  
  MPIM PDF: https://people.mpim-bonn.mpg.de/gaitsgde/GLC/ambidex.pdf  
  arXiv: https://arxiv.org/abs/2409.08670

- **GLC V: The multiplicity one theorem**  
  MPIM PDF: https://people.mpim-bonn.mpg.de/gaitsgde/GLC/multone.pdf  
  arXiv: https://arxiv.org/abs/2409.09856

Helpful “nearby” references we’ll treat as part of the dependency cloud:
- Arinkin–Gaitsgory, *Singular support of coherent sheaves, and the geometric Langlands conjecture* (nilpotent singular support):  
  https://arxiv.org/abs/1201.6343
- Gaitsgory, *Outline of the proof … for GL(2)* (a compact “proof-architecture” prototype):  
  https://arxiv.org/abs/1302.2506

---

## Goal 2 blueprint (local ℓ-adic Langlands, ℓ ≠ p)

This repo includes a TeX blueprint that aims to **port the GLC proof architecture** (spectral action, Whittaker generator, compactness/monadicity/gluing patterns) into the **Fargues–Scholze** setting on the Fargues–Fontaine curve.

**File:** `blueprints/ladicgeom.tex`

The blueprint centers the Fargues–Scholze **categorical geometrization conjecture**:
- Automorphic side: ℓ-adic sheaves on `Bun_G` (v-stack).
- Spectral side: coherent sheaves with **nilpotent singular support** on a parameter stack.
- Bridge: a **spectral action** and a **Whittaker generator**, mirroring the Gaitsgory strategy.

Key sections (high-level):
- `Bun_G` and stratification
- automorphic categories (`D_lis(Bun_G, Λ)`)
- spectral parameters (`LocSys_{\check G}`) and nilpotent support
- Hecke / Satake / spectral action
- Whittaker object and Whittaker-generated subcategory
- parabolic functors + gluing
- a “checklist of inputs and where they enter” (turning proofs into a dependency DAG)

---

## Goal 3 blueprint (p-adic local Langlands, ℓ = p)

This repo includes a TeX blueprint proposing an **axiom/conjecture package** for a “geometric” approach to p-adic local Langlands that parallels the structural path above, but with **p-adic coefficient sheaf theories** and the **derived Emerton–Gee stack** on the spectral side.

**File:** `blueprints/padicgeom.tex`

Main components (as currently formulated in the blueprint):
- conjectural automorphic category at ℓ=p on `Bun_G`
- Hecke/Satake formalism at ℓ=p
- spectral action of perfect complexes on the (derived) Emerton–Gee parameter stack
- a kernel/eigensheaf formalism for the correspondence
- parabolic functors + gluing forcing the correct support condition
- test case: `G = GL_2(Q_p)` as a sanity check/anchor

---

## Repository layout (suggested)

This project is designed to grow into something like:

.
├── blueprints/
│   ├── ladicgeom.tex          # ℓ ≠ p transfer blueprint (Fargues–Scholze track)
│   └── padicgeom.tex          # ℓ = p conjectural framework blueprint
├── sources/
│   ├── glc/                   # bibliographic + retrieval metadata for GLC I–V
│   └── bib/                   # BibTeX / CSL / citation normalization
├── atlas/
│   ├── glc/                   # “proof atlas”: theorem/lemma cards + dependency graph
│   ├── fs/                    # local ℓ-adic atlas (FS conjecture → subclaims)
│   └── padic/                 # p-adic conjecture package atlas
├── formal/
│   ├── lean/                  # Lean 4 formalization experiments (interface-level first)
│   └── coq/                   # optional
├── tools/
│   ├── tex2claims/            # TeX → structured claims extraction
│   ├── dedupe/                # “same lemma” detection across papers
│   ├── citation-check/        # enforce provenance + exact pointers
│   └── eval/                  # regression tests for LLM outputs
└── prompts/
├── extraction.md
├── normalization.md
├── formalization.md
└── redteam.md

If you fork this repo and don’t want the above structure, feel free to simplify — the **core** is the three workstreams.

---

## How we use LLMs (discipline + guardrails)

### Provenance-first rule
Every generated “claim” must include:
- **source**: (paper / section / theorem number / page-range)
- **exact statement**: copied or near-verbatim (then normalized)
- **dependencies**: explicit list of prerequisites
- **confidence**: what is verified vs inferred

If an LLM can’t point to where something appears, we treat it as a hypothesis, not a fact.

### Typical workflows
- **Chunk + index** TeX/PDF sources into a retrieval corpus.
- **Extract** theorem/lemma/definition statements into structured YAML/JSON.
- **Normalize** notation across papers (name resolution: “same object, different symbols”).
- **Build a dependency DAG** (proof as a graph, not a wall of text).
- **Validate locally**:
  - consistency checks (missing hypotheses, functor directions, variance)
  - “proof sketch sanity” checks (does step X actually imply Y?)
- **Formalize selectively**:
  - start with *interface lemmas* (monadicity patterns, adjunction packages, compact generation),
  - then move toward deeper geometric content as libraries permit.

### What “formalize” means here
Given current proof assistant ecosystems, we expect a staged approach:
1. **Interface-level formalization** (∞-categories, adjunctions, monads, compactness patterns).
2. **Structured pseudo-formalization** for derived AG content (typed definitions + dependency-checked lemmas).
3. **Full formalization** only where the ecosystem supports it.

---

## Building the blueprints locally

If you have TeX installed:

```bash
# from repo root
latexmk -pdf -interaction=nonstopmode -halt-on-error blueprints/ladicgeom.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error blueprints/padicgeom.tex
````

(We recommend `latexmk` to avoid manual reruns.)

---

## Roadmap (high-level)

### Milestone A — GLC proof atlas (Goal 1)

* [ ] Canonical bibliography + download scripts (arXiv + MPIM PDFs)
* [ ] Claim extraction for GLC I–V (defs/lemmas/thms)
* [ ] Dependency DAG per paper + merged DAG across the series
* [ ] “Gap list”: where a lemma uses technology outside the series (and where)

### Milestone B — FS categorical geometrization blueprint → task graph (Goal 2)

* [ ] Convert `ladicgeom.tex` into a machine-readable checklist of claims
* [ ] Map each claim to a known input (FS, DHKM, etc.) or mark as open
* [ ] Identify the *local analogs* of GLC proof steps (Whittaker, monadicity, gluing)

### Milestone C — p-adic package stabilization (Goal 3)

* [ ] Turn axioms/conjectures in `padicgeom.tex` into a minimal consistent “package”
* [ ] Cross-check compatibility with Emerton–Gee–Hellmann expectations
* [ ] Work out GL₂(Qₚ) test case: what would the conjectural kernel predict?

---

## Contributing

Contributions are welcome in three modes:

1. **Math contributions:**

   * Add a lemma card, dependency edge, or “where-used” annotation.
   * Provide exact pointers (paper/section/theorem/page).

2. **Engineering contributions:**

   * TeX → structured extraction, citation normalization, tooling.
   * DAG visualization, regression tests, reproducibility.

3. **Formalization contributions:**

   * Interface lemmas (adjunctions/monads/compact generation).
   * “Proof skeleton” formalizations that can later be refined.

### Minimal PR standards

* No new claim without a source pointer.
* No rewritten theorem statement without the original quoted in the PR discussion.
* If an LLM is used, include the prompt + model/output in the PR (or a link to it).

---

## Disclaimer

This is a research-driven project.
All mathematical content derived from LLM assistance is **subject to error** and must be independently verified.
Nothing here should be treated as a substitute for the original sources or expert review.

---

## License

Recommended: dual-license

* code under **MIT** or **Apache-2.0**
* notes/blueprints under **CC-BY 4.0** (unless you prefer a different arrangement)

(Choose what matches your intended usage and attribution preferences.)


