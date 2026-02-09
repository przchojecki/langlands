# GLC Proof Atlas (Task 3: dependency edges)
This folder turns the extracted **Task 2 claim index** into a *navigable atlas* by adding **syntactic dependency edges** between claims.
⚠️ **Interpretation note.** Dependencies are inferred by scanning each claim’s *local region* in the TeX source (the claim environment + the intervening text up to the next claim) for `\*ref{...}` style references whose targets are also extracted claims. This is a **reference graph**, not a verified logical proof graph.
## Quick links
- [GLC1](./claims/GLC1.md)
- [GLC2](./claims/GLC2.md)
- [GLC3](./claims/GLC3.md)
- [GLC4](./claims/GLC4.md)
- [GLC5](./claims/GLC5.md)

## Atlas statistics
- Claims: **947**
- Dependency edges (label-based): **1128**

### Per-paper counts
| Paper | #claims | avg deps/claim | outgoing edges |
|---|---:|---:|---:|
| GLC1 | 60 | 1.13 | 68 |
| GLC2 | 470 | 1.10 | 518 |
| GLC3 | 265 | 1.38 | 365 |
| GLC4 | 78 | 1.18 | 92 |
| GLC5 | 74 | 1.15 | 85 |

## Graph exports
- CSV edge list: [`graphs/claim_dependency_edges.csv`](./graphs/claim_dependency_edges.csv)
- JSONL edge list: [`graphs/claim_dependency_edges.jsonl`](./graphs/claim_dependency_edges.jsonl)
- Graph stats: [`graphs/graph_stats.json`](./graphs/graph_stats.json)
- Claims + deps CSV: [`claims/all_claims_with_deps.csv`](./claims/all_claims_with_deps.csv)

## Most-referenced claims (highest in-degree)
| Rank | Claim | in-degree | kind | section |
|---:|---|---:|---|---|
| 1 | [`GLC3:theorem:t:semiinf geom Satake`](./claims/GLC3.md#glc3-theorem-t-semiinf-geom-satake-8f7ac0f0) | 16 | theorem | Spectral semi-infinite category/ies |
| 2 | [`GLC3:theorem:t:CT compat`](./claims/GLC3.md#glc3-theorem-t-ct-compat-531db125) | 12 | theorem | Langlands functor and constant terms |
| 3 | [`GLC3:theorem:t:CT co of Poinc`](./claims/GLC3.md#glc3-theorem-t-ct-co-of-poinc-3db8357f) | 10 | theorem | Interaction of parabolic induction with the Whittaker model |
| 4 | [`GLC2:proposition:p:IndCoh Op via fact almost`](./claims/GLC2.md#glc2-proposition-p-indcoh-op-via-fact-almost-40720ab0) | 9 | proposition | Digression: \texorpdfstring{$\IndCoh^*$}{IndCoh*} via factorization algebras |
| 5 | [`GLC2:theorem:t:ins vac reg`](./claims/GLC2.md#glc2-theorem-t-ins-vac-reg-eedd43e2) | 9 | theorem | The Hecke eigen-property of critical localization |
| 6 | [`GLC3:theorem:t:main`](./claims/GLC3.md#glc3-theorem-t-main-f7b41490) | 9 | theorem | The Langlands functor is an equivalence on the Eisenstein part(s) |
| 7 | [`GLC3:theorem:t:semiinf CS`](./claims/GLC3.md#glc3-theorem-t-semiinf-cs-6d1ae71f) | 9 | theorem | Spectral semi-infinite category/ies |
| 8 | [`GLC2:theorem:t:critical FLE`](./claims/GLC2.md#glc2-theorem-t-critical-fle-3a31764e) | 8 | theorem | The critical FLE |
| 9 | [`GLC3:theorem:t:local Jacquet dual enh`](./claims/GLC3.md#glc3-theorem-t-local-jacquet-dual-enh-f9a3d431) | 8 | theorem | Compatibility of the FLE with the Jacquet functors |
| 10 | [`GLC3:theorem:t:L and Eis`](./claims/GLC3.md#glc3-theorem-t-l-and-eis-25dc3e99) | 8 | theorem | Langlands functor and Eisenstein series |
| 11 | [`GLC1:theorem:t:compact to bdd below dr`](./claims/GLC1.md#glc1-theorem-t-compact-to-bdd-below-dr-5be9504c) | 7 | theorem | Construction of the Langlands functor (de Rham context) |
| 12 | [`GLC2:theorem:t:FLE and Sat`](./claims/GLC2.md#glc2-theorem-t-fle-and-sat-8cc2bea4) | 7 | theorem | The critical FLE |
| 13 | [`GLC3:theorem:t:Omega comp`](./claims/GLC3.md#glc3-theorem-t-omega-comp-da30bbb9) | 7 | theorem | Proof of semi-infinite Casselman-Shalika |
| 14 | [`GLC4:theorem:t:BG via Op`](./claims/GLC4.md#glc4-theorem-t-bg-via-op-e0ad90d6) | 7 | theorem | The expression for \texorpdfstring{$\CA_{G,\on{irred}}$}{AGirred} via opers |
| 15 | [`GLC5:theorem:t:Hecke Z 0`](./claims/GLC5.md#glc5-theorem-t-hecke-z-0-c6bfb40f) | 7 | theorem | The core of the proof |

## Most-dependent claims (highest out-degree)
| Rank | Claim | out-degree | kind | section |
|---:|---|---:|---|---|
| 1 | [`GLC2:lemma:l:IndCoh on Gr const`](./claims/GLC2.md#glc2-lemma-l-indcoh-on-gr-const-6eb324fd) | 13 | lemma | The spectral spherical category |
| 2 | [`GLC3:remark:auto0001@L941`](./claims/GLC3.md#glc3-remark-auto0001-l941-218591a7) | 11 | remark | Introduction |
| 3 | [`GLC3:corollary:c:kill Eis again`](./claims/GLC3.md#glc3-corollary-c-kill-eis-again-445ed307) | 11 | corollary | Langlands functor and constant terms |
| 4 | [`GLC2:proposition:p:match fact structures`](./claims/GLC2.md#glc2-proposition-p-match-fact-structures-008ead58) | 8 | proposition | From module categories over \texorpdfstring{$\QCoh(\LS^\mer_\cG)$}{QCohLS} to factorization module categories over \texorpdfstring{$\Rep(\cG)$}{RepG} |
| 5 | [`GLC3:proposition:p:!* forth`](./claims/GLC3.md#glc3-proposition-p-forth-18a32a51) | 8 | proposition | The Langlands functor is an equivalence on the Eisenstein part(s) |
| 6 | [`GLC3:corollary:c:Omega to Omega spec`](./claims/GLC3.md#glc3-corollary-c-omega-to-omega-spec-a7ce0ec0) | 8 | corollary | Proof of semi-infinite geometric Satake |
| 7 | [`GLC4:proposition:p:dual of Poinc`](./claims/GLC4.md#glc4-proposition-p-dual-of-poinc-cec7228a) | 8 | proposition | Right adjoint as the dual |
| 8 | [`GLC5:corollary:auto0037@L3429`](./claims/GLC5.md#glc5-corollary-auto0037-l3429-c4ca40e2) | 8 | corollary | The core of the proof |
| 9 | [`GLC1:theorem:t:cc-intro`](./claims/GLC1.md#glc1-theorem-t-cc-intro-dff5600b) | 7 | theorem | Introduction |
| 10 | [`GLC1:remark:auto0041@L3103`](./claims/GLC1.md#glc1-remark-auto0041-l3103-e003d67f) | 7 | remark | Proof of \thmref{t:compact to bdd below Betti} |
| 11 | [`GLC2:corollary:c:coaction homotopy`](./claims/GLC2.md#glc2-corollary-c-coaction-homotopy-04f8fcc1) | 7 | corollary | Digression: \texorpdfstring{$\IndCoh^*$}{IndCoh*} via factorization algebras |
| 12 | [`GLC2:remark:auto0119@L8942`](./claims/GLC2.md#glc2-remark-auto0119-l8942-174fb748) | 7 | remark | Proof of the pointwise version of the critical FLE |
| 13 | [`GLC3:corollary:c:coeff of Eis ! enh`](./claims/GLC3.md#glc3-corollary-c-coeff-of-eis-enh-e3b1a982) | 7 | corollary | Interaction of parabolic induction with the Whittaker model |
| 14 | [`GLC2:remark:r:spectral action`](./claims/GLC2.md#glc2-remark-r-spectral-action-8df8455d) | 6 | remark | Introduction |
| 15 | [`GLC2:corollary:c:FLE t exact`](./claims/GLC2.md#glc2-corollary-c-fle-t-exact-8cbe082f) | 6 | corollary | The critical FLE |

## What’s next (not yet automatic)
- Resolve cross-paper references that currently appear only as `\cite[Prop/Theorem ...]{GLCk}` (these do not carry TeX labels).
- Refine “dependency scope” (e.g. *statement-only* vs *proof-only* edges).
- Add equation-level and section-level nodes (optional), to reduce “unresolved ref labels”.
