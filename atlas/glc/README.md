# GLC proof atlas

This directory is a **machine-generated atlas** for the 5-paper series *“Proof of the geometric Langlands conjecture”* (GLC I–V).

## What’s inside

- `INDEX.md`: the atlas landing page (stats + hubs)
- `claims/`: per-paper claim listings (Task 2) **augmented with Task 3 dependency edges**
- `graphs/`: edge lists + summary stats

## Task 3: dependency edges (current method)

For each claim, we define a **local region** in the TeX source:

> from the `\begin{...}` of the claim environment up to (but not including) the next extracted claim’s `\begin{...}`.

We scan that region for TeX reference macros of the form `\*ref{LABEL}` (e.g. `\thmref{...}`, `\lemref{...}`, `\ref{...}`, `\Cref{...}`) and keep only those `LABEL`s that match a known extracted claim label.

### What this gives you

- A *reference graph* good for “where is this used?” navigation.
- A starting point for refining into a proof DAG (manual or semi-automatic).

### What it does not yet do

- It does **not** resolve dependencies expressed only via citations like `\cite[Proposition 17.2.2]{GLC2}`.
- It does **not** separate statement-only vs proof-only references.
- It does **not** verify correctness.

## Formats

- Claim records: `claims/GLCk.index.with_deps.jsonl`
  - one JSON object per claim; includes `dependencies`, `used_by_count`, and an `atlas.anchor` slug.
- Edge list: `graphs/claim_dependency_edges.csv`

## Reproducibility

This atlas can be regenerated from TeX sources by re-running Task 2 extraction and then re-running the Task 3 dependency scan.
