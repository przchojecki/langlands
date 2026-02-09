# GLC5 claim atlas

- Back to [GLC atlas index](../INDEX.md)
- JSONL with deps: [`GLC5.index.with_deps.jsonl`](./GLC5.index.with_deps.jsonl)

Claims in this file: **74**


## Introduction

<a id="glc5-remark-auto0001-l981-dbc71e6a"></a>
### Remark `auto0001@L981`
- **Claim ID:** `GLC5:remark:auto0001@L981`
- **Location:** `gaits5.tex` lines 981-997
- **Context:** Introduction
- **Dependencies (outgoing):** 4 — [`GLC5:corollary:c:sc`](./GLC5.md#glc5-corollary-c-sc-3f0b64e6), [`GLC5:remark:r:not 1 aff`](./GLC5.md#glc5-remark-r-not-1-aff-d3fe47b5), [`GLC5:theorem:t:Hecke Z 0`](./GLC5.md#glc5-theorem-t-hecke-z-0-c6bfb40f), [`GLC5:theorem:t:Hecke Z 1`](./GLC5.md#glc5-theorem-t-hecke-z-1-35bfd3aa)
- **Used by (incoming):** 0 — _(none)_

- **Unresolved `\*ref{…}` targets (not claims):** 15

```tex
The outline above uses a special feature of the de Rham setting. By contrast, Betti or \'etale moduli stacks of local systems have infinite dimensional algebras of global functions, while the de Rham moduli stack has very few global functions. For this reason, our strategy does n…
```

---


## Summary of the preceding results

<a id="glc5-conjecture-c-glc-b694423d"></a>
### Conjecture `c:GLC`
- **Claim ID:** `GLC5:conjecture:c:GLC`
- **Location:** `gaits5.tex` lines 1517-1519
- **Context:** Summary of the preceding results
- **Dependencies (outgoing):** 0 — _(none found by label-scan)_
- **Used by (incoming):** 0 — _(none)_

- **Unresolved `\*ref{…}` targets (not claims):** 7

```tex
\label{c:GLC} The functor $\BL_G$ is an equivalence.
```

---


## Reduction to the case when \texorpdfstring{$G$}{G} is almost simple and simply-connected

<a id="glc5-proposition-p-alm-isogeny-1efac726"></a>
### Proposition `p:alm isogeny`
- **Claim ID:** `GLC5:proposition:p:alm isogeny`
- **Location:** `gaits5.tex` lines 1724-1734
- **Context:** Reduction to the case when \texorpdfstring{$G$}{G} is almost simple and simply-connected
- **Dependencies (outgoing):** 0 — _(none found by label-scan)_
- **Used by (incoming):** 1 — [`GLC5:remark:auto0004@L1964`](./GLC5.md#glc5-remark-auto0004-l1964-65a517e9)

- **Unresolved `\*ref{…}` targets (not claims):** 7

```tex
\label{p:alm isogeny} The following diagram of functors commutes \begin{equation} \label{e:alm isogeny} \CD \Dmod_{\frac{1}{2}}(\Bun_{G_1}) @>{\BL_{G_1}}>> \IndCoh_\Nilp(\LS_{\cG_1}) \\ @A{\phi^!}AA @A{(\phi^\vee)^\IndCoh_*}AA \\ \Dmod_{\frac{1}{2}}(\Bun_{G_2}) @>{\BL_{G_2}}>> \I…
```

---

<a id="glc5-remark-auto0004-l1964-65a517e9"></a>
### Remark `auto0004@L1964`
- **Claim ID:** `GLC5:remark:auto0004@L1964`
- **Location:** `gaits5.tex` lines 1964-1972
- **Context:** Reduction to the case when \texorpdfstring{$G$}{G} is almost simple and simply-connected
- **Dependencies (outgoing):** 1 — [`GLC5:proposition:p:alm isogeny`](./GLC5.md#glc5-proposition-p-alm-isogeny-1efac726)
- **Used by (incoming):** 0 — _(none)_

- **Unresolved `\*ref{…}` targets (not claims):** 4

```tex
Note that the functor $'\!\phi_!$ is \emph{not} the left adjoint of $'\!\phi^!$: the latter would involve an additional step of !-averaging from $\fL^+(G_1)$-equivariance to $\fL^+(G_2)$-equivariance. \medskip Note also that the functor $'\!\phi_!$ is \emph{not} monoidal.
```

---

<a id="glc5-proposition-p-change-group-1-8c14b4cb"></a>
### Proposition `p:change group 1`
- **Claim ID:** `GLC5:proposition:p:change group 1`
- **Location:** `gaits5.tex` lines 2083-2087
- **Context:** Reduction to the case when \texorpdfstring{$G$}{G} is almost simple and simply-connected
- **Dependencies (outgoing):** 0 — _(none found by label-scan)_
- **Used by (incoming):** 1 — [`GLC5:theorem:t:change group 2`](./GLC5.md#glc5-theorem-t-change-group-2-ba87572e)

- **Unresolved `\*ref{…}` targets (not claims):** 1

```tex
\label{p:change group 1} The functor $$\QCoh(\LS_{\cG_2})\underset{\QCoh(\LS_{\cG_1})}\otimes \IndCoh_\Nilp(\LS_{\cG_1})\to \IndCoh_\Nilp(\LS_{\cG_2})$$ is an equivalence.
```

---

<a id="glc5-theorem-t-change-group-2-ba87572e"></a>
### Theorem `t:change group 2`
- **Claim ID:** `GLC5:theorem:t:change group 2`
- **Location:** `gaits5.tex` lines 2096-2102
- **Context:** Reduction to the case when \texorpdfstring{$G$}{G} is almost simple and simply-connected
- **Dependencies (outgoing):** 1 — [`GLC5:proposition:p:change group 1`](./GLC5.md#glc5-proposition-p-change-group-1-8c14b4cb)
- **Used by (incoming):** 2 — [`GLC5:corollary:c:sc`](./GLC5.md#glc5-corollary-c-sc-3f0b64e6), [`GLC5:proposition:p:neutral`](./GLC5.md#glc5-proposition-p-neutral-7b391fb7)

```tex
\label{t:change group 2} The functor \begin{equation} \label{e:change group 2} \QCoh(\LS_{\cG_2})\underset{\QCoh(\LS_{\cG_1})}\otimes \Dmod_{\frac{1}{2}}(\Bun_{G_1}) \to \Dmod_{\frac{1}{2}}(\Bun_{G_2}) \end{equation} is an equivalence.
```

---

<a id="glc5-corollary-c-change-group-73ce2540"></a>
### Corollary `c:change group`
- **Claim ID:** `GLC5:corollary:c:change group`
- **Location:** `gaits5.tex` lines 2108-2110
- **Context:** Reduction to the case when \texorpdfstring{$G$}{G} is almost simple and simply-connected
- **Dependencies (outgoing):** 0 — _(none found by label-scan)_
- **Used by (incoming):** 0 — _(none)_

```tex
\label{c:change group} Suppose that the functor $\BL_{G_1}$ is an equivalence. Then so is $\BL_{G_2}$.
```

---

<a id="glc5-corollary-c-prel-sc-8172113d"></a>
### Corollary `c:prel sc`
- **Claim ID:** `GLC5:corollary:c:prel sc`
- **Location:** `gaits5.tex` lines 2120-2122
- **Context:** Reduction to the case when \texorpdfstring{$G$}{G} is almost simple and simply-connected
- **Dependencies (outgoing):** 0 — _(none found by label-scan)_
- **Used by (incoming):** 0 — _(none)_

```tex
\label{c:prel sc} If GLC holds for $G_{\on{sc}}$, then it also holds for $G$.
```

---

<a id="glc5-corollary-c-sc-3f0b64e6"></a>
### Corollary `c:sc`
- **Claim ID:** `GLC5:corollary:c:sc`
- **Location:** `gaits5.tex` lines 2143-2146
- **Context:** Reduction to the case when \texorpdfstring{$G$}{G} is almost simple and simply-connected
- **Dependencies (outgoing):** 1 — [`GLC5:theorem:t:change group 2`](./GLC5.md#glc5-theorem-t-change-group-2-ba87572e)
- **Used by (incoming):** 3 — [`GLC5:proposition:p:A irred`](./GLC5.md#glc5-proposition-p-a-irred-bf95b8c0), [`GLC5:proposition:p:neutral`](./GLC5.md#glc5-proposition-p-neutral-7b391fb7), [`GLC5:remark:auto0001@L981`](./GLC5.md#glc5-remark-auto0001-l981-dbc71e6a)

- **Unresolved `\*ref{…}` targets (not claims):** 4

```tex
\label{c:sc} If GLC holds for all $G$ that are almost simple and simply-connected, then it holds for any reductive $G$.
```

---

<a id="glc5-lemma-l-comps-that-arise-55f9470a"></a>
### Lemma `l:comps that arise`
- **Claim ID:** `GLC5:lemma:l:comps that arise`
- **Location:** `gaits5.tex` lines 2296-2299
- **Context:** Reduction to the case when \texorpdfstring{$G$}{G} is almost simple and simply-connected
- **Dependencies (outgoing):** 1 — [`GLC5:theorem:t:Hecke Z 0`](./GLC5.md#glc5-theorem-t-hecke-z-0-c6bfb40f)
- **Used by (incoming):** 0 — _(none)_

- **Unresolved `\*ref{…}` targets (not claims):** 3

```tex
\label{l:comps that arise} $$\Dmod_{\frac{1}{2}}(\Bun_{G_1})'= \underset{\alpha}\oplus\, \Dmod_{\frac{1}{2}}(\Bun_{G_1})_\alpha,$$ where $\alpha$ runs over the subset consisting of those characters that vanish on $\Gamma$.
```

---

<a id="glc5-proposition-p-neutral-7b391fb7"></a>
### Proposition `p:neutral`
- **Claim ID:** `GLC5:proposition:p:neutral`
- **Location:** `gaits5.tex` lines 2376-2381
- **Context:** Reduction to the case when \texorpdfstring{$G$}{G} is almost simple and simply-connected
- **Dependencies (outgoing):** 2 — [`GLC5:corollary:c:sc`](./GLC5.md#glc5-corollary-c-sc-3f0b64e6), [`GLC5:theorem:t:change group 2`](./GLC5.md#glc5-theorem-t-change-group-2-ba87572e)
- **Used by (incoming):** 1 — [`GLC5:proposition:p:semistab`](./GLC5.md#glc5-proposition-p-semistab-5c2f242e)

- **Unresolved `\*ref{…}` targets (not claims):** 6

```tex
\label{p:neutral} The full subcategory $$\Dmod_{\frac{1}{2}}(\Bun_{G_1})' \subset \Dmod_{\frac{1}{2}}(\Bun_{G_1})$$ equals $$\QCoh(\LS'_{\cG_1})\underset{\QCoh(\LS_{\cG_1})}\otimes \Dmod_{\frac{1}{2}}(\Bun_{G_1}).$$
```

---


## Low genus cases

<a id="glc5-proposition-p-genus-1-5cd66628"></a>
### Proposition `p:genus 1`
- **Claim ID:** `GLC5:proposition:p:genus 1`
- **Location:** `gaits5.tex` lines 2525-2528
- **Context:** Low genus cases
- **Dependencies (outgoing):** 1 — [`GLC5:theorem:t:pi 1 LS`](./GLC5.md#glc5-theorem-t-pi-1-ls-11ae4b8d)
- **Used by (incoming):** 0 — _(none)_

- **Unresolved `\*ref{…}` targets (not claims):** 1

```tex
\label{p:genus 1} Let $\sG$ be an adjoint group different from $PGL_n$. Then for a curve of genus $1$, we have $\LS_\sG^{\on{irred}}=\emptyset$.
```

---


## Calculation of the fundamental group

<a id="glc5-remark-auto0013-l2622-61904c0b"></a>
### Remark `auto0013@L2622`
- **Claim ID:** `GLC5:remark:auto0013@L2622`
- **Location:** `gaits5.tex` lines 2622-2625
- **Context:** Calculation of the fundamental group
- **Dependencies (outgoing):** 0 — _(none found by label-scan)_
- **Used by (incoming):** 0 — _(none)_

- **Unresolved `\*ref{…}` targets (not claims):** 1

```tex
The map \eqref{e:to gerbes} means that to a $\cG$-bundle we can canonically associate an \'etale $\pi_1(\cG)$-gerbe. Namely, this is the gerbe of \'etale-local lifts of our bundle to the simply-connected cover of $\cG$.
```

---

<a id="glc5-proposition-p-pi-1-bun-195b3da2"></a>
### Proposition `p:pi 1 Bun`
- **Claim ID:** `GLC5:proposition:p:pi 1 Bun`
- **Location:** `gaits5.tex` lines 2643-2646
- **Context:** Calculation of the fundamental group
- **Dependencies (outgoing):** 0 — _(none found by label-scan)_
- **Used by (incoming):** 4 — [`GLC5:corollary:auto0037@L3429`](./GLC5.md#glc5-corollary-auto0037-l3429-c4ca40e2), [`GLC5:lemma:l:every torsor`](./GLC5.md#glc5-lemma-l-every-torsor-998c4a9c), [`GLC5:remark:auto0019@L2803`](./GLC5.md#glc5-remark-auto0019-l2803-343787c8), [`GLC5:theorem:t:pi 1 LS`](./GLC5.md#glc5-theorem-t-pi-1-ls-11ae4b8d)

- **Unresolved `\*ref{…}` targets (not claims):** 6

```tex
\label{p:pi 1 Bun} The map \eqref{e:to gerbes} defines an isomorphism of $\tau_{\leq 1}$ truncations of \'etale homotopy types.
```

---

<a id="glc5-lemma-l-every-torsor-998c4a9c"></a>
### Lemma `l:every torsor`
- **Claim ID:** `GLC5:lemma:l:every torsor`
- **Location:** `gaits5.tex` lines 2728-2731
- **Context:** Calculation of the fundamental group
- **Dependencies (outgoing):** 1 — [`GLC5:proposition:p:pi 1 Bun`](./GLC5.md#glc5-proposition-p-pi-1-bun-195b3da2)
- **Used by (incoming):** 0 — _(none)_

- **Unresolved `\*ref{…}` targets (not claims):** 1

```tex
\label{l:every torsor} Every $\mu_\infty$-torsor on every connected component of $\on{Ge}_{\pi_1(\cG)}(X)$ is the restriction of $\CL_{\CP_{Z_G}}$ for some $\CP_{Z_G}$.
```

---

<a id="glc5-theorem-t-pi-1-ls-11ae4b8d"></a>
### Theorem `t:pi 1 LS`
- **Claim ID:** `GLC5:theorem:t:pi 1 LS`
- **Location:** `gaits5.tex` lines 2774-2778
- **Context:** Calculation of the fundamental group
- **Dependencies (outgoing):** 1 — [`GLC5:proposition:p:pi 1 Bun`](./GLC5.md#glc5-proposition-p-pi-1-bun-195b3da2)
- **Used by (incoming):** 5 — [`GLC5:corollary:c:pi 1 LS`](./GLC5.md#glc5-corollary-c-pi-1-ls-25540784), [`GLC5:proposition:p:compl 1`](./GLC5.md#glc5-proposition-p-compl-1-f9d03fc2), [`GLC5:proposition:p:conn on stable bundles`](./GLC5.md#glc5-proposition-p-conn-on-stable-bundles-ae68f4b6), [`GLC5:proposition:p:genus 1`](./GLC5.md#glc5-proposition-p-genus-1-5cd66628), [`GLC5:remark:auto0019@L2803`](./GLC5.md#glc5-remark-auto0019-l2803-343787c8)

- **Unresolved `\*ref{…}` targets (not claims):** 2

```tex
\label{t:pi 1 LS} Assume that $g\geq 2$, and if $g=2$, then its root system does not have $A_1$ factors. Then the map \eqref{e:LS irred to Bun} induces an isomorphism on the $\tau_{\leq 1}$ truncations of \'etale homotopy types.
```

---

<a id="glc5-corollary-c-pi-1-ls-25540784"></a>
### Corollary `c:pi 1 LS`
- **Claim ID:** `GLC5:corollary:c:pi 1 LS`
- **Location:** `gaits5.tex` lines 2783-2788
- **Context:** Calculation of the fundamental group
- **Dependencies (outgoing):** 1 — [`GLC5:theorem:t:pi 1 LS`](./GLC5.md#glc5-theorem-t-pi-1-ls-11ae4b8d)
- **Used by (incoming):** 1 — [`GLC5:proposition:p:A irred`](./GLC5.md#glc5-proposition-p-a-irred-bf95b8c0)

```tex
\label{c:pi 1 LS} For every connected component of $\LS_\cG^{\on{irred}}$, every \'etale local system of $k$-vector spaces on it splits as a direct sum of 1-dimensional ones. Each of the latter is isomorphic to the restriction of $\CL_{\CP_{Z_G}}$ for some $\CP_{Z_G}\in \Bun_{Z_G…
```

---

<a id="glc5-proposition-p-compl-1-f9d03fc2"></a>
### Proposition `p:compl 1`
- **Claim ID:** `GLC5:proposition:p:compl 1`
- **Location:** `gaits5.tex` lines 2798-2801
- **Context:** Calculation of the fundamental group
- **Dependencies (outgoing):** 1 — [`GLC5:theorem:t:pi 1 LS`](./GLC5.md#glc5-theorem-t-pi-1-ls-11ae4b8d)
- **Used by (incoming):** 4 — [`GLC5:corollary:auto0037@L3429`](./GLC5.md#glc5-corollary-auto0037-l3429-c4ca40e2), [`GLC5:proposition:p:conn on stable bundles`](./GLC5.md#glc5-proposition-p-conn-on-stable-bundles-ae68f4b6), [`GLC5:remark:auto0019@L2803`](./GLC5.md#glc5-remark-auto0019-l2803-343787c8), [`GLC5:remark:auto0038@L3851`](./GLC5.md#glc5-remark-auto0038-l3851-827f1224)

```tex
\label{p:compl 1} Under the assumptions on $G$ and $g$ specified in \thmref{t:pi 1 LS}, the complement of $\Bun_\cG^{\on{stbl}}$ in $\Bun_\cG$ has codimension $\geq 2$.
```

---

<a id="glc5-remark-auto0019-l2803-343787c8"></a>
### Remark `auto0019@L2803`
- **Claim ID:** `GLC5:remark:auto0019@L2803`
- **Location:** `gaits5.tex` lines 2803-2813
- **Context:** Calculation of the fundamental group
- **Dependencies (outgoing):** 3 — [`GLC5:proposition:p:compl 1`](./GLC5.md#glc5-proposition-p-compl-1-f9d03fc2), [`GLC5:proposition:p:pi 1 Bun`](./GLC5.md#glc5-proposition-p-pi-1-bun-195b3da2), [`GLC5:theorem:t:pi 1 LS`](./GLC5.md#glc5-theorem-t-pi-1-ls-11ae4b8d)
- **Used by (incoming):** 0 — _(none)_

- **Unresolved `\*ref{…}` targets (not claims):** 1

```tex
Statements of this type are classical in the literature of $\Bun_G$; they begin with \cite[Sect. 9]{NR}. The literature we found concerned coarse moduli spaces instead of moduli stacks, so we include the argument for \propref{p:compl 1} in \secref{ss:proof of compl 1}. There are…
```

---

<a id="glc5-proposition-p-conn-on-stable-bundles-ae68f4b6"></a>
### Proposition `p:conn on stable bundles`
- **Claim ID:** `GLC5:proposition:p:conn on stable bundles`
- **Location:** `gaits5.tex` lines 2835-2840
- **Context:** Calculation of the fundamental group
- **Dependencies (outgoing):** 4 — [`GLC5:corollary:c:compl 2`](./GLC5.md#glc5-corollary-c-compl-2-1015dc92), [`GLC5:proposition:p:compl 1`](./GLC5.md#glc5-proposition-p-compl-1-f9d03fc2), [`GLC5:theorem:t:end Poinc vac b`](./GLC5.md#glc5-theorem-t-end-poinc-vac-b-36a7465c), [`GLC5:theorem:t:pi 1 LS`](./GLC5.md#glc5-theorem-t-pi-1-ls-11ae4b8d)
- **Used by (incoming):** 2 — [`GLC5:corollary:auto0037@L3429`](./GLC5.md#glc5-corollary-auto0037-l3429-c4ca40e2), [`GLC5:corollary:auto0043@L4010`](./GLC5.md#glc5-corollary-auto0043-l4010-80244576)

- **Unresolved `\*ref{…}` targets (not claims):** 6

```tex
\label{p:conn on stable bundles} The map $$\LS_\cG^{\on{stbl}}\to \Bun_\cG^{\on{stbl}}$$ is smooth and surjective. The fibers of this map are affine spaces.
```

---


## The core of the proof

<a id="glc5-theorem-t-hecke-z-0-c6bfb40f"></a>
### Theorem `t:Hecke Z 0`
- **Claim ID:** `GLC5:theorem:t:Hecke Z 0`
- **Location:** `gaits5.tex` lines 3000-3005
- **Context:** The core of the proof
- **Dependencies (outgoing):** 0 — _(none found by label-scan)_
- **Used by (incoming):** 7 — [`GLC5:corollary:c:FM L`](./GLC5.md#glc5-corollary-c-fm-l-a0d18fe7), [`GLC5:lemma:auto0056@L4813`](./GLC5.md#glc5-lemma-auto0056-l4813-3ce5c0c3), [`GLC5:lemma:l:comps that arise`](./GLC5.md#glc5-lemma-l-comps-that-arise-55f9470a), [`GLC5:proposition:p:semistab`](./GLC5.md#glc5-proposition-p-semistab-5c2f242e), [`GLC5:remark:auto0001@L981`](./GLC5.md#glc5-remark-auto0001-l981-dbc71e6a), [`GLC5:remark:auto0033@L3238`](./GLC5.md#glc5-remark-auto0033-l3238-da9d6bd9), [`GLC5:remark:auto0044@L4138`](./GLC5.md#glc5-remark-auto0044-l4138-8af9469e)

- **Unresolved `\*ref{…}` targets (not claims):** 1

```tex
\label{t:Hecke Z 0} For $\alpha\in (Z_G)^\vee$ as above, the idempotent $$\CO_{\LS_{\cG,\alpha}}\otimes (-):\Dmod_{\frac{1}{2}}(\Bun_G)\to \Dmod_{\frac{1}{2}}(\Bun_G),$$ where $\otimes$ denotes the spectral action of $\QCoh(\LS_\cG)$ on $\Dmod_{\frac{1}{2}}(\Bun_G)$, identifies c…
```

---

<a id="glc5-theorem-t-hecke-z-1-35bfd3aa"></a>
### Theorem `t:Hecke Z 1`
- **Claim ID:** `GLC5:theorem:t:Hecke Z 1`
- **Location:** `gaits5.tex` lines 3011-3017
- **Context:** The core of the proof
- **Dependencies (outgoing):** 0 — _(none found by label-scan)_
- **Used by (incoming):** 6 — [`GLC5:corollary:c:FM L`](./GLC5.md#glc5-corollary-c-fm-l-a0d18fe7), [`GLC5:lemma:auto0056@L4813`](./GLC5.md#glc5-lemma-auto0056-l4813-3ce5c0c3), [`GLC5:proposition:p:semistab`](./GLC5.md#glc5-proposition-p-semistab-5c2f242e), [`GLC5:remark:auto0001@L981`](./GLC5.md#glc5-remark-auto0001-l981-dbc71e6a), [`GLC5:remark:auto0033@L3238`](./GLC5.md#glc5-remark-auto0033-l3238-da9d6bd9), [`GLC5:remark:auto0044@L4138`](./GLC5.md#glc5-remark-auto0044-l4138-8af9469e)

- **Unresolved `\*ref{…}` targets (not claims):** 3

```tex
\label{t:Hecke Z 1} For $\CP_{Z_G}\in \Bun_{Z_G}$ and the corresponding $\CL_{\CP_{Z_G}}\in \QCoh(\LS_\cG)$, the functor $$\CL^{\otimes -1}_{\CP_{Z_G}}\otimes(-):\Dmod_{\frac{1}{2}}(\Bun_G)\to \Dmod_{\frac{1}{2}}(\Bun_G),$$ where $\otimes$ denotes the spectral action of $\QCoh(\L…
```

---

<a id="glc5-theorem-t-end-poinc-vac-a-e869fc66"></a>
### Theorem `t:end Poinc vac a`
- **Claim ID:** `GLC5:theorem:t:end Poinc vac a`
- **Location:** `gaits5.tex` lines 3045-3049
- **Context:** The core of the proof
- **Dependencies (outgoing):** 0 — _(none found by label-scan)_
- **Used by (incoming):** 4 — [`GLC5:corollary:auto0037@L3429`](./GLC5.md#glc5-corollary-auto0037-l3429-c4ca40e2), [`GLC5:remark:auto0033@L3238`](./GLC5.md#glc5-remark-auto0033-l3238-da9d6bd9), [`GLC5:theorem:t:end Poinc vac a'`](./GLC5.md#glc5-theorem-t-end-poinc-vac-a-e869fc66), [`GLC5:theorem:t:end Poinc vac b`](./GLC5.md#glc5-theorem-t-end-poinc-vac-b-36a7465c)

```tex
\label{t:end Poinc vac a} For every $\alpha$, the map $$k\to H^0(\CEnd(\on{Poinc}^{\on{Vac}}_{G,!,\alpha}))$$ is an isomorphism.
```

---

<a id="glc5-theorem-t-end-poinc-vac-a-e869fc66"></a>
### Theorem `t:end Poinc vac a'`
- **Claim ID:** `GLC5:theorem:t:end Poinc vac a'`
- **Location:** `gaits5.tex` lines 3054-3056
- **Context:** The core of the proof
- **Dependencies (outgoing):** 1 — [`GLC5:theorem:t:end Poinc vac a`](./GLC5.md#glc5-theorem-t-end-poinc-vac-a-e869fc66)
- **Used by (incoming):** 2 — [`GLC5:corollary:auto0037@L3429`](./GLC5.md#glc5-corollary-auto0037-l3429-c4ca40e2), [`GLC5:remark:auto0033@L3238`](./GLC5.md#glc5-remark-auto0033-l3238-da9d6bd9)

```tex
\label{t:end Poinc vac a'} $H^i(\CEnd(\on{Poinc}^{\on{Vac,glob}}_{G,!}))=0$ for $i\neq 0$.
```

---

<a id="glc5-corollary-c-end-poinc-vac-a-162aab2c"></a>
### Corollary `c:end Poinc vac a`
- **Claim ID:** `GLC5:corollary:c:end Poinc vac a`
- **Location:** `gaits5.tex` lines 3060-3062
- **Context:** The core of the proof
- **Dependencies (outgoing):** 0 — _(none found by label-scan)_
- **Used by (incoming):** 1 — [`GLC5:remark:auto0033@L3238`](./GLC5.md#glc5-remark-auto0033-l3238-da9d6bd9)

- **Unresolved `\*ref{…}` targets (not claims):** 1

```tex
\label{c:end Poinc vac a} $\dim\left(H^0(\CEnd(\on{Poinc}^{\on{Vac,glob}}_{G,!}))\right)=|Z_G|$.
```

---

<a id="glc5-theorem-t-end-poinc-vac-b-36a7465c"></a>
### Theorem `t:end Poinc vac b`
- **Claim ID:** `GLC5:theorem:t:end Poinc vac b`
- **Location:** `gaits5.tex` lines 3068-3071
- **Context:** The core of the proof
- **Dependencies (outgoing):** 1 — [`GLC5:theorem:t:end Poinc vac a`](./GLC5.md#glc5-theorem-t-end-poinc-vac-a-e869fc66)
- **Used by (incoming):** 3 — [`GLC5:corollary:auto0037@L3429`](./GLC5.md#glc5-corollary-auto0037-l3429-c4ca40e2), [`GLC5:proposition:p:conn on stable bundles`](./GLC5.md#glc5-proposition-p-conn-on-stable-bundles-ae68f4b6), [`GLC5:remark:auto0033@L3238`](./GLC5.md#glc5-remark-auto0033-l3238-da9d6bd9)

```tex
\label{t:end Poinc vac b} For a non-trivial $\CP_{Z_G}\in \Dmod_{\frac{1}{2}}(\Bun_G)$, $$H^0\left(\CHom(\on{Poinc}^{\on{Vac,glob}}_{G,!},\CP_{Z_G}\cdot \on{Poinc}^{\on{Vac,glob}}_{G,!})\right)=0.$$
```

---

<a id="glc5-theorem-t-end-poinc-vac-b-36a7465c"></a>
### Theorem `t:end Poinc vac b'`
- **Claim ID:** `GLC5:theorem:t:end Poinc vac b'`
- **Location:** `gaits5.tex` lines 3076-3079
- **Context:** The core of the proof
- **Dependencies (outgoing):** 0 — _(none found by label-scan)_
- **Used by (incoming):** 2 — [`GLC5:corollary:auto0037@L3429`](./GLC5.md#glc5-corollary-auto0037-l3429-c4ca40e2), [`GLC5:remark:auto0036@L3420`](./GLC5.md#glc5-remark-auto0036-l3420-3da82452)

```tex
\label{t:end Poinc vac b'} For a non-trivial $\CP_{Z_G}\in \Dmod_{\frac{1}{2}}(\Bun_G)$, $$\CHom(\on{Poinc}^{\on{Vac,glob}}_{G,!},\CP_{Z_G}\cdot \on{Poinc}^{\on{Vac,glob}}_{G,!})=0.$$
```

---

<a id="glc5-theorem-t-ls-cm-14225ab2"></a>
### Theorem `t:LS CM`
- **Claim ID:** `GLC5:theorem:t:LS CM`
- **Location:** `gaits5.tex` lines 3089-3092
- **Context:** The core of the proof
- **Dependencies (outgoing):** 0 — _(none found by label-scan)_
- **Used by (incoming):** 1 — [`GLC5:remark:auto0038@L3851`](./GLC5.md#glc5-remark-auto0038-l3851-827f1224)

```tex
\label{t:LS CM} The stack $\LS_\cG$ is a classical locally complete intersection of dimension $$\dim(\fg)\cdot 2(g-1).$$
```

---

<a id="glc5-corollary-c-ls-cm-15261889"></a>
### Corollary `c:LS CM`
- **Claim ID:** `GLC5:corollary:c:LS CM`
- **Location:** `gaits5.tex` lines 3094-3096
- **Context:** The core of the proof
- **Dependencies (outgoing):** 0 — _(none found by label-scan)_
- **Used by (incoming):** 2 — [`GLC5:proposition:p:A irred`](./GLC5.md#glc5-proposition-p-a-irred-bf95b8c0), [`GLC5:proposition:p:compl 2`](./GLC5.md#glc5-proposition-p-compl-2-2188ef85)

```tex
\label{c:LS CM} The stack $\LS_\cG$ is Cohen-Macaulay of dimension $\dim(\fg)\cdot 2(g-1)$.
```

---

<a id="glc5-proposition-p-compl-2-2188ef85"></a>
### Proposition `p:compl 2`
- **Claim ID:** `GLC5:proposition:p:compl 2`
- **Location:** `gaits5.tex` lines 3102-3105
- **Context:** The core of the proof
- **Dependencies (outgoing):** 1 — [`GLC5:corollary:c:LS CM`](./GLC5.md#glc5-corollary-c-ls-cm-15261889)
- **Used by (incoming):** 6 — [`GLC5:corollary:auto0037@L3429`](./GLC5.md#glc5-corollary-auto0037-l3429-c4ca40e2), [`GLC5:corollary:c:LS P estim`](./GLC5.md#glc5-corollary-c-ls-p-estim-ace2761e), [`GLC5:corollary:c:compl 2`](./GLC5.md#glc5-corollary-c-compl-2-1015dc92), [`GLC5:proposition:p:A irred`](./GLC5.md#glc5-proposition-p-a-irred-bf95b8c0), [`GLC5:remark:auto0038@L3851`](./GLC5.md#glc5-remark-auto0038-l3851-827f1224), [`GLC5:remark:auto0041@L3950`](./GLC5.md#glc5-remark-auto0041-l3950-e259f8e5)

- **Unresolved `\*ref{…}` targets (not claims):** 1

```tex
\label{p:compl 2} Excluding the case of $g=2$ with the root system of $G$ containing an $A_1$ factor, the complement to $\LS_\cG^{\on{irred}}$ in $\LS_\cG$ has codimension $\geq 2$.
```

---

<a id="glc5-corollary-c-compl-2-1015dc92"></a>
### Corollary `c:compl 2`
- **Claim ID:** `GLC5:corollary:c:compl 2`
- **Location:** `gaits5.tex` lines 3113-3116
- **Context:** The core of the proof
- **Dependencies (outgoing):** 1 — [`GLC5:proposition:p:compl 2`](./GLC5.md#glc5-proposition-p-compl-2-2188ef85)
- **Used by (incoming):** 1 — [`GLC5:proposition:p:conn on stable bundles`](./GLC5.md#glc5-proposition-p-conn-on-stable-bundles-ae68f4b6)

- **Unresolved `\*ref{…}` targets (not claims):** 1

```tex
\label{c:compl 2} The embedding $\LS^{\on{irred}}_\cG\hookrightarrow \LS_\cG$ induces a bijection between the sets of connected components.
```

---

<a id="glc5-proposition-p-a-irred-bf95b8c0"></a>
### Proposition `p:A irred`
- **Claim ID:** `GLC5:proposition:p:A irred`
- **Location:** `gaits5.tex` lines 3129-3133
- **Context:** The core of the proof
- **Dependencies (outgoing):** 4 — [`GLC5:corollary:c:LS CM`](./GLC5.md#glc5-corollary-c-ls-cm-15261889), [`GLC5:corollary:c:pi 1 LS`](./GLC5.md#glc5-corollary-c-pi-1-ls-25540784), [`GLC5:corollary:c:sc`](./GLC5.md#glc5-corollary-c-sc-3f0b64e6), [`GLC5:proposition:p:compl 2`](./GLC5.md#glc5-proposition-p-compl-2-2188ef85)
- **Used by (incoming):** 0 — _(none)_

- **Unresolved `\*ref{…}` targets (not claims):** 7

```tex
\label{p:A irred} The restriction of $\CA_{G,\on{irred}}$ to every connected component is isomorphic to a direct sum of lines bundles, each of which is a restriction of some $\CL_{\CP_{Z_G}}$ (see \secref{sss:L P Z G}).
```

---

<a id="glc5-remark-auto0033-l3238-da9d6bd9"></a>
### Remark `auto0033@L3238`
- **Claim ID:** `GLC5:remark:auto0033@L3238`
- **Location:** `gaits5.tex` lines 3238-3242
- **Context:** The core of the proof
- **Dependencies (outgoing):** 6 — [`GLC5:corollary:c:end Poinc vac a`](./GLC5.md#glc5-corollary-c-end-poinc-vac-a-162aab2c), [`GLC5:theorem:t:Hecke Z 0`](./GLC5.md#glc5-theorem-t-hecke-z-0-c6bfb40f), [`GLC5:theorem:t:Hecke Z 1`](./GLC5.md#glc5-theorem-t-hecke-z-1-35bfd3aa), [`GLC5:theorem:t:end Poinc vac a`](./GLC5.md#glc5-theorem-t-end-poinc-vac-a-e869fc66), [`GLC5:theorem:t:end Poinc vac a'`](./GLC5.md#glc5-theorem-t-end-poinc-vac-a-e869fc66), [`GLC5:theorem:t:end Poinc vac b`](./GLC5.md#glc5-theorem-t-end-poinc-vac-b-36a7465c)
- **Used by (incoming):** 0 — _(none)_

- **Unresolved `\*ref{…}` targets (not claims):** 5

```tex
Note that the last step in the above argument shows that the map $$\CO_{\LS_\cG} \to \jmath_*(\CO_{\LS^{\on{irred}}_\cG})$$ also induces an isomorphism at the level of $H^0(\Gamma(\LS_\cG,-))$.
```

---

<a id="glc5-corollary-c-o-on-ls-0657123a"></a>
### Corollary `c:O on LS`
- **Claim ID:** `GLC5:corollary:c:O on LS`
- **Location:** `gaits5.tex` lines 3409-3413
- **Context:** The core of the proof
- **Dependencies (outgoing):** 0 — _(none found by label-scan)_
- **Used by (incoming):** 2 — [`GLC5:remark:auto0035@L3415`](./GLC5.md#glc5-remark-auto0035-l3415-aa3f6c03), [`GLC5:remark:auto0036@L3420`](./GLC5.md#glc5-remark-auto0036-l3420-3da82452)

```tex
\label{c:O on LS} For $g\geq 2$, for every connected component $\alpha$ of $\LS_\cG$, the map $$k\to \Gamma(\LS_{\cG,\alpha},\CO_{\LS_{\cG,\alpha}})$$ is an isomorphism.
```

---

<a id="glc5-remark-auto0035-l3415-aa3f6c03"></a>
### Remark `auto0035@L3415`
- **Claim ID:** `GLC5:remark:auto0035@L3415`
- **Location:** `gaits5.tex` lines 3415-3418
- **Context:** The core of the proof
- **Dependencies (outgoing):** 1 — [`GLC5:corollary:c:O on LS`](./GLC5.md#glc5-corollary-c-o-on-ls-0657123a)
- **Used by (incoming):** 0 — _(none)_

```tex
One can prove \corref{c:O on LS} directly by a deformation argument using \cite[Theorem 4.2]{FT}.
```

---

<a id="glc5-remark-auto0036-l3420-3da82452"></a>
### Remark `auto0036@L3420`
- **Claim ID:** `GLC5:remark:auto0036@L3420`
- **Location:** `gaits5.tex` lines 3420-3423
- **Context:** The core of the proof
- **Dependencies (outgoing):** 2 — [`GLC5:corollary:c:O on LS`](./GLC5.md#glc5-corollary-c-o-on-ls-0657123a), [`GLC5:theorem:t:end Poinc vac b'`](./GLC5.md#glc5-theorem-t-end-poinc-vac-b-36a7465c)
- **Used by (incoming):** 0 — _(none)_

```tex
We remark that Corollary \ref{c:O on LS} is a special feature of the de Rham setting; there are many more global functions on the Betti moduli stack.
```

---

<a id="glc5-corollary-auto0037-l3429-c4ca40e2"></a>
### Corollary `auto0037@L3429`
- **Claim ID:** `GLC5:corollary:auto0037@L3429`
- **Location:** `gaits5.tex` lines 3429-3431
- **Context:** The core of the proof
- **Dependencies (outgoing):** 8 — [`GLC5:proposition:p:compl 1`](./GLC5.md#glc5-proposition-p-compl-1-f9d03fc2), [`GLC5:proposition:p:compl 2`](./GLC5.md#glc5-proposition-p-compl-2-2188ef85), [`GLC5:proposition:p:conn on stable bundles`](./GLC5.md#glc5-proposition-p-conn-on-stable-bundles-ae68f4b6), [`GLC5:proposition:p:pi 1 Bun`](./GLC5.md#glc5-proposition-p-pi-1-bun-195b3da2), [`GLC5:theorem:t:end Poinc vac a`](./GLC5.md#glc5-theorem-t-end-poinc-vac-a-e869fc66), [`GLC5:theorem:t:end Poinc vac a'`](./GLC5.md#glc5-theorem-t-end-poinc-vac-a-e869fc66), [`GLC5:theorem:t:end Poinc vac b`](./GLC5.md#glc5-theorem-t-end-poinc-vac-b-36a7465c), [`GLC5:theorem:t:end Poinc vac b'`](./GLC5.md#glc5-theorem-t-end-poinc-vac-b-36a7465c)
- **Used by (incoming):** 0 — _(none)_

- **Unresolved `\*ref{…}` targets (not claims):** 10

```tex
For $g\geq 2$, for a non-trivial $\CP_{Z_G}$, we have $\Gamma(\LS_\cG,\CL_{\CP_{Z_G}})=0$.
```

---


## Geometry of \texorpdfstring{$\Bun_G$}{geomBunG}

<a id="glc5-remark-auto0038-l3851-827f1224"></a>
### Remark `auto0038@L3851`
- **Claim ID:** `GLC5:remark:auto0038@L3851`
- **Location:** `gaits5.tex` lines 3851-3855
- **Context:** Geometry of \texorpdfstring{$\Bun_G$}{geomBunG}
- **Dependencies (outgoing):** 3 — [`GLC5:proposition:p:compl 1`](./GLC5.md#glc5-proposition-p-compl-1-f9d03fc2), [`GLC5:proposition:p:compl 2`](./GLC5.md#glc5-proposition-p-compl-2-2188ef85), [`GLC5:theorem:t:LS CM`](./GLC5.md#glc5-theorem-t-ls-cm-14225ab2)
- **Used by (incoming):** 0 — _(none)_

```tex
Note that the assertion of \propref{p:compl 1} is false for $G=SL_2$ and $g=2$: in this case the dimension of the semi-stable but unstable locus is $2$, which is $>$ than $$1=3-2=\dim(\Bun_G)-2.$$
```

---

<a id="glc5-lemma-l-ls-p-estim-42c64cc9"></a>
### Lemma `l:LS P estim`
- **Claim ID:** `GLC5:lemma:l:LS P estim`
- **Location:** `gaits5.tex` lines 3891-3903
- **Context:** Geometry of \texorpdfstring{$\Bun_G$}{geomBunG}
- **Dependencies (outgoing):** 0 — _(none found by label-scan)_
- **Used by (incoming):** 2 — [`GLC5:corollary:auto0043@L4010`](./GLC5.md#glc5-corollary-auto0043-l4010-80244576), [`GLC5:remark:auto0041@L3950`](./GLC5.md#glc5-remark-auto0041-l3950-e259f8e5)

- **Unresolved `\*ref{…}` targets (not claims):** 1

```tex
\hfill \label{l:LS P estim} \smallskip \noindent{\em(a)} Each fiber of the map $\sfq$ has dimension $\leq \dim(\fn(P))\cdot (2g-1)$. \smallskip \noindent{\em(b)} There exists a dense open substack of $\LS_M$ over which $\sfq$ is smooth.
```

---

<a id="glc5-corollary-c-ls-p-estim-ace2761e"></a>
### Corollary `c:LS P estim`
- **Claim ID:** `GLC5:corollary:c:LS P estim`
- **Location:** `gaits5.tex` lines 3914-3918
- **Context:** Geometry of \texorpdfstring{$\Bun_G$}{geomBunG}
- **Dependencies (outgoing):** 1 — [`GLC5:proposition:p:compl 2`](./GLC5.md#glc5-proposition-p-compl-2-2188ef85)
- **Used by (incoming):** 0 — _(none)_

- **Unresolved `\*ref{…}` targets (not claims):** 1

```tex
\label{c:LS P estim} $\dim(\LS_P) \leq \dim(\LS_M) + \dim(\fn(P))\cdot (2g-1) - 1$.
```

---

<a id="glc5-remark-auto0041-l3950-e259f8e5"></a>
### Remark `auto0041@L3950`
- **Claim ID:** `GLC5:remark:auto0041@L3950`
- **Location:** `gaits5.tex` lines 3950-3954
- **Context:** Geometry of \texorpdfstring{$\Bun_G$}{geomBunG}
- **Dependencies (outgoing):** 2 — [`GLC5:lemma:l:LS P estim`](./GLC5.md#glc5-lemma-l-ls-p-estim-42c64cc9), [`GLC5:proposition:p:compl 2`](./GLC5.md#glc5-proposition-p-compl-2-2188ef85)
- **Used by (incoming):** 0 — _(none)_

- **Unresolved `\*ref{…}` targets (not claims):** 1

```tex
Note that the assertion of \propref{p:compl 2} is false for $G=SL_2$ and $g=2$: in this case the dimension of the reducible locus is $5$, which is greater than $$4=6-2=\dim(\LS_G)-2.$$
```

---

<a id="glc5-lemma-auto0042-l3991-ecf508f2"></a>
### Lemma `auto0042@L3991`
- **Claim ID:** `GLC5:lemma:auto0042@L3991`
- **Location:** `gaits5.tex` lines 3991-3998
- **Context:** Geometry of \texorpdfstring{$\Bun_G$}{geomBunG}
- **Dependencies (outgoing):** 0 — _(none found by label-scan)_
- **Used by (incoming):** 0 — _(none)_

```tex
Let $Y$ be a quasi-smooth scheme of virtual dimension $d$. Suppose that $m$ is an integer such that for all field-valued points $y\in Y$ we have $$\dim(H^{-1}(T^*_y(Y)))\leq m.$$ Then $\dim(Y)\leq d+m$.
```

---

<a id="glc5-corollary-auto0043-l4010-80244576"></a>
### Corollary `auto0043@L4010`
- **Claim ID:** `GLC5:corollary:auto0043@L4010`
- **Location:** `gaits5.tex` lines 4010-4019
- **Context:** Geometry of \texorpdfstring{$\Bun_G$}{geomBunG}
- **Dependencies (outgoing):** 2 — [`GLC5:lemma:l:LS P estim`](./GLC5.md#glc5-lemma-l-ls-p-estim-42c64cc9), [`GLC5:proposition:p:conn on stable bundles`](./GLC5.md#glc5-proposition-p-conn-on-stable-bundles-ae68f4b6)
- **Used by (incoming):** 0 — _(none)_

- **Unresolved `\*ref{…}` targets (not claims):** 3

```tex
Let $\CY$ be a quasi-smooth algebraic stack of virtual dimension\footnote{Recall that for a quasi-smooth algebraic stack $\CY$, its dimension/virtual dimension are defined as follows: for a smooth cover $Y\to \CY$ with $Y$ a scheme, the dimension/virtual dimension of $\CY$ equals…
```

---

<a id="glc5-remark-auto0044-l4138-8af9469e"></a>
### Remark `auto0044@L4138`
- **Claim ID:** `GLC5:remark:auto0044@L4138`
- **Location:** `gaits5.tex` lines 4138-4148
- **Context:** Geometry of \texorpdfstring{$\Bun_G$}{geomBunG}
- **Dependencies (outgoing):** 2 — [`GLC5:theorem:t:Hecke Z 0`](./GLC5.md#glc5-theorem-t-hecke-z-0-c6bfb40f), [`GLC5:theorem:t:Hecke Z 1`](./GLC5.md#glc5-theorem-t-hecke-z-1-35bfd3aa)
- **Used by (incoming):** 0 — _(none)_

- **Unresolved `\*ref{…}` targets (not claims):** 6

```tex
The above argument can be refined to prove the following criterion (originally due to A.~Weil) for a $G$-bundle $\CP_G$ to admit a connection: \medskip This happens if and only if, for every reduction of $\CP_G$ to a \emph{Levi subgroup} $M$, this reduction, viewed as an $M$-bund…
```

---


## 2-Fourier-Mukai transform of the automorphic category

<a id="glc5-remark-r-not-1-aff-d3fe47b5"></a>
### Remark `r:not 1 aff`
- **Claim ID:** `GLC5:remark:r:not 1 aff`
- **Location:** `gaits5.tex` lines 4279-4295
- **Context:** 2-Fourier-Mukai transform of the automorphic category
- **Dependencies (outgoing):** 0 — _(none found by label-scan)_
- **Used by (incoming):** 1 — [`GLC5:remark:auto0001@L981`](./GLC5.md#glc5-remark-auto0001-l981-dbc71e6a)

- **Unresolved `\*ref{…}` targets (not claims):** 3

```tex
\label{r:not 1 aff} The central players in the paper \cite{Ga3} are prestacks that are \emph{1-affine}, i.e., those for each the functor of \emph{enhanced} global sections \begin{equation} \label{e:glob sect shv categ} \on{ShvCat}(\CY)\overset{\bGamma^{\on{enh}}(\CY,-)}\longright…
```

---

<a id="glc5-lemma-l-invol-2652941e"></a>
### Lemma `l:invol`
- **Claim ID:** `GLC5:lemma:l:invol`
- **Location:** `gaits5.tex` lines 4363-4367
- **Context:** 2-Fourier-Mukai transform of the automorphic category
- **Dependencies (outgoing):** 0 — _(none found by label-scan)_
- **Used by (incoming):** 1 — [`GLC5:theorem:t:Verdier FM`](./GLC5.md#glc5-theorem-t-verdier-fm-6f3d0708)

- **Unresolved `\*ref{…}` targets (not claims):** 2

```tex
\label{l:invol} Under the above circumstances, if $\on{2-FM}_{\CY_1\to \CY_2}$ is an equivalence, then so is $\on{2-FM}_{\CY_2\to \CY_1}$, and $$\on{2-FM}_{\CY_2\to \CY_1}\circ \on{2-FM}_{\CY_1\to \CY_2}\simeq \on{Id}.$$
```

---

<a id="glc5-lemma-l-hecke-1-abs-gen-ddd5008b"></a>
### Lemma `l:Hecke 1 abs gen`
- **Claim ID:** `GLC5:lemma:l:Hecke 1 abs gen`
- **Location:** `gaits5.tex` lines 4424-4427
- **Context:** 2-Fourier-Mukai transform of the automorphic category
- **Dependencies (outgoing):** 0 — _(none found by label-scan)_
- **Used by (incoming):** 1 — [`GLC5:lemma:l:Hecke 0 abs`](./GLC5.md#glc5-lemma-l-hecke-0-abs-9e5a7f1c)

- **Unresolved `\*ref{…}` targets (not claims):** 1

```tex
\label{l:Hecke 1 abs gen} Under the identification of \eqref{e:fiber FM gen zero}, the action of $a$ on $\bC_2|_{\zero_{\CH_2}}$ corresponds to the endofunctor of $\bC_1$, given by tensoring wity $\CL_a$.
```

---

<a id="glc5-lemma-l-hecke-0-abs-gen-b690a551"></a>
### Lemma `l:Hecke 0 abs gen`
- **Claim ID:** `GLC5:lemma:l:Hecke 0 abs gen`
- **Location:** `gaits5.tex` lines 4451-4456
- **Context:** 2-Fourier-Mukai transform of the automorphic category
- **Dependencies (outgoing):** 0 — _(none found by label-scan)_
- **Used by (incoming):** 1 — [`GLC5:lemma:l:sgrp`](./GLC5.md#glc5-lemma-l-sgrp-74e8f846)

- **Unresolved `\*ref{…}` targets (not claims):** 2

```tex
\label{l:Hecke 0 abs gen} Under the identification of \eqref{e:fiber FM gen zero}, the direct summand $$\bC_{1,\omega}:=\Gamma((\CH_1)_\omega,\ul\bC_1)\subset \Gamma(\CH_1,\ul\bC_1)=\bC_1$$ corresponds to the direct summand $$(\ul\bC_2|_{\one_{\CH_2}})_\omega \subset \ul\bC_2|_{\…
```

---

<a id="glc5-lemma-l-fiber-and-global-sects-gen-0e8b35d5"></a>
### Lemma `l:fiber and global sects gen`
- **Claim ID:** `GLC5:lemma:l:fiber and global sects gen`
- **Location:** `gaits5.tex` lines 4462-4493
- **Context:** 2-Fourier-Mukai transform of the automorphic category
- **Dependencies (outgoing):** 0 — _(none found by label-scan)_
- **Used by (incoming):** 1 — [`GLC5:lemma:l:Hecke 1 abs`](./GLC5.md#glc5-lemma-l-hecke-1-abs-1823b3dd)

- **Unresolved `\*ref{…}` targets (not claims):** 2

```tex
\label{l:fiber and global sects gen} For $\ul\bC_1\in \ShvCat(\CH_1)$, the following diagram commutes: $$ \CD \bGamma(\CH_2,\on{2-FM}_{\CH_1\to \CH_2}(\ul\bC_1)) @>{\on{ev}|_{h_2}}>> \on{2-FM}_{\CH_2\to \CH_1}(\ul\bC_1)|_{h_2} \\ @A{\text{\eqref{e:fiber FM gen zero}}}A{\sim}A \\…
```

---

<a id="glc5-theorem-t-verdier-fm-6f3d0708"></a>
### Theorem `t:Verdier FM`
- **Claim ID:** `GLC5:theorem:t:Verdier FM`
- **Location:** `gaits5.tex` lines 4528-4530
- **Context:** 2-Fourier-Mukai transform of the automorphic category
- **Dependencies (outgoing):** 1 — [`GLC5:lemma:l:invol`](./GLC5.md#glc5-lemma-l-invol-2652941e)
- **Used by (incoming):** 0 — _(none)_

- **Unresolved `\*ref{…}` targets (not claims):** 7

```tex
\label{t:Verdier FM} The pairing \eqref{e:Verdier pairing Gamma} is of 2-Fourier-Mukai type.
```

---

<a id="glc5-corollary-c-verdier-fm-invol-91f8010c"></a>
### Corollary `c:Verdier FM invol`
- **Claim ID:** `GLC5:corollary:c:Verdier FM invol`
- **Location:** `gaits5.tex` lines 4596-4603
- **Context:** 2-Fourier-Mukai transform of the automorphic category
- **Dependencies (outgoing):** 0 — _(none found by label-scan)_
- **Used by (incoming):** 1 — [`GLC5:theorem:t:FM L`](./GLC5.md#glc5-theorem-t-fm-l-22521c74)

- **Unresolved `\*ref{…}` targets (not claims):** 4

```tex
\label{c:Verdier FM invol} The composition $$\on{2-FM}_{\on{Ge}_{\Gamma^\vee(1)}(X)\to \on{Ge}_{\Gamma}(X)}\circ \on{2-FM}_{\on{Ge}_{\Gamma}(X)\to \on{Ge}_{\Gamma^\vee(1)}(X)}$$ is the involution of $\on{ShvCat}(\on{Ge}_{\Gamma}(X))$ coming from the inversion on $\Gamma$, $$(\Gam…
```

---

<a id="glc5-lemma-l-sgrp-74e8f846"></a>
### Lemma `l:sgrp`
- **Claim ID:** `GLC5:lemma:l:sgrp`
- **Location:** `gaits5.tex` lines 4664-4668
- **Context:** 2-Fourier-Mukai transform of the automorphic category
- **Dependencies (outgoing):** 1 — [`GLC5:lemma:l:Hecke 0 abs gen`](./GLC5.md#glc5-lemma-l-hecke-0-abs-gen-b690a551)
- **Used by (incoming):** 1 — [`GLC5:corollary:c:twisted GLC 1`](./GLC5.md#glc5-corollary-c-twisted-glc-1-468ef1d0)

- **Unresolved `\*ref{…}` targets (not claims):** 2

```tex
\label{l:sgrp} There is a canonical equivalence $$\bGamma\left(\on{Ge}_{\Gamma_1}(X), (\ul\bC_\Gamma|_{\on{Ge}_{\Gamma_1}(X)})_{\CG_{\fG_{\Gamma_1^\vee(1)}}}\right) \simeq \bGamma\biggl(\on{Ge}_{\Gamma^\vee(1)}(X)\underset{\on{Ge}_{\Gamma_1^\vee(1)}(X)}\times \{\fG_{\Gamma_1^\vee…
```

---

<a id="glc5-lemma-l-hecke-0-abs-9e5a7f1c"></a>
### Lemma `l:Hecke 0 abs`
- **Claim ID:** `GLC5:lemma:l:Hecke 0 abs`
- **Location:** `gaits5.tex` lines 4706-4710
- **Context:** 2-Fourier-Mukai transform of the automorphic category
- **Dependencies (outgoing):** 1 — [`GLC5:lemma:l:Hecke 1 abs gen`](./GLC5.md#glc5-lemma-l-hecke-1-abs-gen-ddd5008b)
- **Used by (incoming):** 1 — [`GLC5:corollary:c:FM L`](./GLC5.md#glc5-corollary-c-fm-l-a0d18fe7)

- **Unresolved `\*ref{…}` targets (not claims):** 2

```tex
\label{l:Hecke 0 abs} Under the identification \eqref{e:fib glob sect neutral}, the action of $\CO_{\on{Ge}_{\Gamma}(X),\alpha}$ on $\bC_\Gamma$ corresponds to the action of $\sP_\alpha$ on $\ul\bC_{\Gamma^\vee(1)}|_{\fG^0_{\Gamma^\vee(1)}}$.
```

---

<a id="glc5-lemma-l-hecke-1-abs-1823b3dd"></a>
### Lemma `l:Hecke 1 abs`
- **Claim ID:** `GLC5:lemma:l:Hecke 1 abs`
- **Location:** `gaits5.tex` lines 4733-4736
- **Context:** 2-Fourier-Mukai transform of the automorphic category
- **Dependencies (outgoing):** 1 — [`GLC5:lemma:l:fiber and global sects gen`](./GLC5.md#glc5-lemma-l-fiber-and-global-sects-gen-0e8b35d5)
- **Used by (incoming):** 1 — [`GLC5:corollary:c:FM L`](./GLC5.md#glc5-corollary-c-fm-l-a0d18fe7)

- **Unresolved `\*ref{…}` targets (not claims):** 1

```tex
\label{l:Hecke 1 abs} Under the identification \eqref{e:fib glob sect neutral}, the action of $\CL^{\otimes -1}_{\CP_{\Gamma^\vee(1)}}$ on $\bC_\Gamma$ corresponds to the action of $\CP_{\Gamma^\vee(1)}$ on $\ul\bC_{\Gamma^\vee(1)}|_{\fG^0_{\Gamma^\vee(1)}}$.
```

---

<a id="glc5-lemma-l-fiber-and-global-sects-77592914"></a>
### Lemma `l:fiber and global sects`
- **Claim ID:** `GLC5:lemma:l:fiber and global sects`
- **Location:** `gaits5.tex` lines 4767-4776
- **Context:** 2-Fourier-Mukai transform of the automorphic category
- **Dependencies (outgoing):** 0 — _(none found by label-scan)_
- **Used by (incoming):** 1 — [`GLC5:proposition:p:key local`](./GLC5.md#glc5-proposition-p-key-local-b3851f6b)

- **Unresolved `\*ref{…}` targets (not claims):** 3

```tex
\label{l:fiber and global sects} The following diagram commutes: $$ \CD \bC_{\Gamma^\vee(1)} @>{\on{ev}|_{\fG_{\Gamma^\vee(1)}}}>> (\ul\bC_{\Gamma^\vee(1)})|_{\fG_{\Gamma^\vee(1)}} \\ @A{\text{\eqref{e:glob fib sect neutral}}}A{\sim}A @A{\sim}A{\text{\eqref{e:fib glob sect 1}}}A…
```

---

<a id="glc5-lemma-auto0056-l4813-3ce5c0c3"></a>
### Lemma `auto0056@L4813`
- **Claim ID:** `GLC5:lemma:auto0056@L4813`
- **Location:** `gaits5.tex` lines 4813-4817
- **Context:** 2-Fourier-Mukai transform of the automorphic category
- **Dependencies (outgoing):** 3 — [`GLC5:theorem:t:FM L`](./GLC5.md#glc5-theorem-t-fm-l-22521c74), [`GLC5:theorem:t:Hecke Z 0`](./GLC5.md#glc5-theorem-t-hecke-z-0-c6bfb40f), [`GLC5:theorem:t:Hecke Z 1`](./GLC5.md#glc5-theorem-t-hecke-z-1-35bfd3aa)
- **Used by (incoming):** 0 — _(none)_

- **Unresolved `\*ref{…}` targets (not claims):** 2

```tex
With respect to the equivalence $\on{2-FM}_{\on{Ge}_{\Gamma}(X)\to \on{Ge}_{\Gamma^\vee(1)}(X)}$, the objects $$\ul\QCoh^\Gamma(\Bun_T) \text{ and } \ul\QCoh^{\Gamma^\vee(1)}(\Bun_{T^\vee_1})$$ correspond to one another.
```

---

<a id="glc5-remark-r-twisted-groups-e70fc576"></a>
### Remark `r:twisted groups`
- **Claim ID:** `GLC5:remark:r:twisted groups`
- **Location:** `gaits5.tex` lines 4923-4938
- **Context:** 2-Fourier-Mukai transform of the automorphic category
- **Dependencies (outgoing):** 0 — _(none found by label-scan)_
- **Used by (incoming):** 1 — [`GLC5:remark:auto0066@L5559`](./GLC5.md#glc5-remark-auto0066-l5559-f45174e3)

```tex
\label{r:twisted groups} We can think $\Bun_{G,\fG_{Z_G}}$ as follows: pick a $G_{\on{ad}}$-torsor $\CP_{G_{\on{ad}}}$ that maps to $\fG_{Z_G}$, and let $$G_{\CP_{G_{\on{ad}}}}$$ be the corresponding (non-pure) inner form of the constant group-scheme with fiber $G$. \medskip Then…
```

---

<a id="glc5-theorem-t-fm-l-22521c74"></a>
### Theorem `t:FM L`
- **Claim ID:** `GLC5:theorem:t:FM L`
- **Location:** `gaits5.tex` lines 4976-4982
- **Context:** 2-Fourier-Mukai transform of the automorphic category
- **Dependencies (outgoing):** 1 — [`GLC5:corollary:c:Verdier FM invol`](./GLC5.md#glc5-corollary-c-verdier-fm-invol-91f8010c)
- **Used by (incoming):** 4 — [`GLC5:corollary:c:FM L`](./GLC5.md#glc5-corollary-c-fm-l-a0d18fe7), [`GLC5:corollary:c:twisted GLC 1`](./GLC5.md#glc5-corollary-c-twisted-glc-1-468ef1d0), [`GLC5:lemma:auto0056@L4813`](./GLC5.md#glc5-lemma-auto0056-l4813-3ce5c0c3), [`GLC5:lemma:l:L FM glob sect`](./GLC5.md#glc5-lemma-l-l-fm-glob-sect-577a5e37)

```tex
\label{t:FM L} Under the identification $\pi_1(\cG)\simeq (Z_G)^\vee(1)$, we have $$\on{2-FM}_{\on{Ge}_{Z_G}(X)\to \on{Ge}_{\pi_1(\cG)}(X)}\left(\ul{\Dmod}^{Z_G}_{\frac{1}{2}}(\Bun_{G_{\on{ad}}})\right)\simeq \ul{\Dmod}^{\pi_1(\cG)}_{\frac{1}{2}}(\Bun_G),$$ up to the inversion in…
```

---

<a id="glc5-corollary-c-fm-l-a0d18fe7"></a>
### Corollary `c:FM L`
- **Claim ID:** `GLC5:corollary:c:FM L`
- **Location:** `gaits5.tex` lines 4986-4990
- **Context:** 2-Fourier-Mukai transform of the automorphic category
- **Dependencies (outgoing):** 5 — [`GLC5:lemma:l:Hecke 0 abs`](./GLC5.md#glc5-lemma-l-hecke-0-abs-9e5a7f1c), [`GLC5:lemma:l:Hecke 1 abs`](./GLC5.md#glc5-lemma-l-hecke-1-abs-1823b3dd), [`GLC5:theorem:t:FM L`](./GLC5.md#glc5-theorem-t-fm-l-22521c74), [`GLC5:theorem:t:Hecke Z 0`](./GLC5.md#glc5-theorem-t-hecke-z-0-c6bfb40f), [`GLC5:theorem:t:Hecke Z 1`](./GLC5.md#glc5-theorem-t-hecke-z-1-35bfd3aa)
- **Used by (incoming):** 1 — [`GLC5:remark:auto0066@L5559`](./GLC5.md#glc5-remark-auto0066-l5559-f45174e3)

- **Unresolved `\*ref{…}` targets (not claims):** 4

```tex
\label{c:FM L} Under the identification $Z_G\simeq (\pi_1(\cG)^\vee)(1)$, we have: $$\on{2-FM}_{\on{Ge}_{\pi_1(\cG)}(X)\to \on{Ge}_{Z_G}(X)}\left(\ul{\Dmod}^{\pi_1(\cG)}_{\frac{1}{2}}(\Bun_G)\right) \simeq \ul{\Dmod}^{Z_G}_{\frac{1}{2}}(\Bun_{G_{\on{ad}}}).$$
```

---

<a id="glc5-proposition-p-key-local-b3851f6b"></a>
### Proposition `p:key local`
- **Claim ID:** `GLC5:proposition:p:key local`
- **Location:** `gaits5.tex` lines 5096-5115
- **Context:** 2-Fourier-Mukai transform of the automorphic category
- **Dependencies (outgoing):** 1 — [`GLC5:lemma:l:fiber and global sects`](./GLC5.md#glc5-lemma-l-fiber-and-global-sects-77592914)
- **Used by (incoming):** 3 — [`GLC5:lemma:auto0065@L5363`](./GLC5.md#glc5-lemma-auto0065-l5363-86080e7f), [`GLC5:lemma:l:L FM glob sect`](./GLC5.md#glc5-lemma-l-l-fm-glob-sect-577a5e37), [`GLC5:remark:auto0066@L5559`](./GLC5.md#glc5-remark-auto0066-l5559-f45174e3)

- **Unresolved `\*ref{…}` targets (not claims):** 4

```tex
\label{p:key local} There is a canonically defined action of the monoidal category $\Rep(\cG_{\on{sc}})_{\Ran,\fG^{\otimes -1}_{\pi_1(\cG)}}$ on $\Dmod_{\frac{1}{2}}(\Bun_{G_{\on{ad}}})_{\CG_{\fG_{\pi_1(\cG)}}}$. Moreover, the following properties hold: \smallskip \noindent{\em(a…
```

---

<a id="glc5-lemma-l-l-fm-glob-sect-577a5e37"></a>
### Lemma `l:L FM glob sect`
- **Claim ID:** `GLC5:lemma:l:L FM glob sect`
- **Location:** `gaits5.tex` lines 5137-5153
- **Context:** 2-Fourier-Mukai transform of the automorphic category
- **Dependencies (outgoing):** 2 — [`GLC5:proposition:p:key local`](./GLC5.md#glc5-proposition-p-key-local-b3851f6b), [`GLC5:theorem:t:FM L`](./GLC5.md#glc5-theorem-t-fm-l-22521c74)
- **Used by (incoming):** 0 — _(none)_

- **Unresolved `\*ref{…}` targets (not claims):** 7

```tex
\label{l:L FM glob sect} The functor \begin{multline} \label{e:FM L glob} \bGamma\left(\on{Ge}_{\pi_1(\cG)}(X),\ul{\Dmod}^{\pi_1(\cG)}_{\frac{1}{2}}(\Bun_G)\right)\to \\ \to \bGamma\left(\on{Ge}_{\pi_1(\cG)}(X),\on{2-FM}_{\on{Ge}_{Z_G}(X)\to \on{Ge}_{\pi_1(\cG)}(X)}\left(\ul{\Dmo…
```

---

<a id="glc5-remark-e-gamma-gr-f4a80f75"></a>
### Remark `e:Gamma gr`
- **Claim ID:** `GLC5:remark:e:Gamma gr`
- **Location:** `gaits5.tex` lines 5244-5272
- **Context:** 2-Fourier-Mukai transform of the automorphic category
- **Dependencies (outgoing):** 0 — _(none found by label-scan)_
- **Used by (incoming):** 1 — [`GLC5:lemma:auto0065@L5363`](./GLC5.md#glc5-lemma-auto0065-l5363-86080e7f)

- **Unresolved `\*ref{…}` targets (not claims):** 2

```tex
Here is an explicit description of the spaces $\on{Ge}_\Gamma(\cD_{\ul{x}})$, $\on{Ge}_\Gamma(\cD^\times_{\ul{x}})$ and $\on{Ge}_\Gamma(\cD_{\ul{x}})_{\ul{x}}$: \medskip Write $\Gamma$ as the kernel of a homomorphism of two tori $T_0\to T_1$. Then $$\on{Ge}_\Gamma(\cD_{\ul{x}})=B…
```

---

<a id="glc5-remark-auto0063-l5287-ef93eec7"></a>
### Remark `auto0063@L5287`
- **Claim ID:** `GLC5:remark:auto0063@L5287`
- **Location:** `gaits5.tex` lines 5287-5292
- **Context:** 2-Fourier-Mukai transform of the automorphic category
- **Dependencies (outgoing):** 0 — _(none found by label-scan)_
- **Used by (incoming):** 0 — _(none)_

- **Unresolved `\*ref{…}` targets (not claims):** 2

```tex
Although we do not need it in what follows, we remark that the pairing \eqref{e:Verdier pairing Gamma loc} is also of Fourier-Mukai type. When $\ul{x}=x$ is a singleton, this follows immediately from the identifications $$\on{Ge}_\Gamma(\cD_{\ul{x}})_{\ul{x}} \simeq \Gamma(-1) \t…
```

---

<a id="glc5-remark-auto0064-l5334-5e44c4c0"></a>
### Remark `auto0064@L5334`
- **Claim ID:** `GLC5:remark:auto0064@L5334`
- **Location:** `gaits5.tex` lines 5334-5337
- **Context:** 2-Fourier-Mukai transform of the automorphic category
- **Dependencies (outgoing):** 0 — _(none found by label-scan)_
- **Used by (incoming):** 0 — _(none)_

- **Unresolved `\*ref{…}` targets (not claims):** 2

```tex
Note that the map \eqref{e:loc Hecke to gerbes} induces a bijection on the sets of connected components when $G$ is simply-connected.
```

---

<a id="glc5-lemma-auto0065-l5363-86080e7f"></a>
### Lemma `auto0065@L5363`
- **Claim ID:** `GLC5:lemma:auto0065@L5363`
- **Location:** `gaits5.tex` lines 5363-5367
- **Context:** 2-Fourier-Mukai transform of the automorphic category
- **Dependencies (outgoing):** 2 — [`GLC5:proposition:p:key local`](./GLC5.md#glc5-proposition-p-key-local-b3851f6b), [`GLC5:remark:e:Gamma gr`](./GLC5.md#glc5-remark-e-gamma-gr-f4a80f75)
- **Used by (incoming):** 0 — _(none)_

- **Unresolved `\*ref{…}` targets (not claims):** 6

```tex
There exists a monoidal functor $$\Sat^{\on{nv}}_{G_{\on{ad}},\fG^{\on{loc}}_{\pi_1(\cG)}}: \Rep(\cG_{\on{sc}})_{\ul{x},\fG^{\otimes -1}_{\pi_1(\cG)}}\to \Sph(G_{\on{ad}})_{\ul{x},\CG_{\fG^{\on{loc}}_{\pi_1(\cG)}}}.$$
```

---

<a id="glc5-remark-auto0066-l5559-f45174e3"></a>
### Remark `auto0066@L5559`
- **Claim ID:** `GLC5:remark:auto0066@L5559`
- **Location:** `gaits5.tex` lines 5559-5600
- **Context:** 2-Fourier-Mukai transform of the automorphic category
- **Dependencies (outgoing):** 3 — [`GLC5:corollary:c:FM L`](./GLC5.md#glc5-corollary-c-fm-l-a0d18fe7), [`GLC5:proposition:p:key local`](./GLC5.md#glc5-proposition-p-key-local-b3851f6b), [`GLC5:remark:r:twisted groups`](./GLC5.md#glc5-remark-r-twisted-groups-e70fc576)
- **Used by (incoming):** 0 — _(none)_

- **Unresolved `\*ref{…}` targets (not claims):** 2

```tex
We claim that $\Op^{\on{mon-free}}_{\cG,x}$ maps in fact to a twisted form of the affine Grassmannian of the group $\cG$, so that \eqref{e:mon-free opers to Ge} factors via this map\footnote{This remark is inessential for the sequel and the reader may choose to skip it.}. \medski…
```

---

<a id="glc5-corollary-c-twisted-bung-125d669b"></a>
### Corollary `c:twisted BunG`
- **Claim ID:** `GLC5:corollary:c:twisted BunG`
- **Location:** `gaits5.tex` lines 5657-5663
- **Context:** 2-Fourier-Mukai transform of the automorphic category
- **Dependencies (outgoing):** 0 — _(none found by label-scan)_
- **Used by (incoming):** 0 — _(none)_

- **Unresolved `\*ref{…}` targets (not claims):** 1

```tex
\label{c:twisted BunG} For a $Z_G$-gerbe $\fG_{Z_G}$ on $X$, we have a canonical equivalence: $$\Dmod_{\frac{1}{2}}(\Bun_{G,\fG^{-1}_{Z_G}}) \simeq \Dmod_{\frac{1}{2}}(\Bun_{G})\underset{\QCoh(\LS_\cG)}\otimes \QCoh(\LS_\cG)_{\CG_{\fG_{Z_G}}},$$ where $\QCoh(\LS_\cG)_{\CG_{\fG_{Z…
```

---

<a id="glc5-corollary-c-twisted-glc-1-468ef1d0"></a>
### Corollary `c:twisted GLC 1`
- **Claim ID:** `GLC5:corollary:c:twisted GLC 1`
- **Location:** `gaits5.tex` lines 5667-5671
- **Context:** 2-Fourier-Mukai transform of the automorphic category
- **Dependencies (outgoing):** 2 — [`GLC5:lemma:l:sgrp`](./GLC5.md#glc5-lemma-l-sgrp-74e8f846), [`GLC5:theorem:t:FM L`](./GLC5.md#glc5-theorem-t-fm-l-22521c74)
- **Used by (incoming):** 1 — [`GLC5:remark:auto0071@L5716`](./GLC5.md#glc5-remark-auto0071-l5716-54f7d848)

```tex
\label{c:twisted GLC 1} There is a canonical equivalence: $$\Dmod_{\frac{1}{2}}(\Bun_{G,\fG^{-1}_{Z_G}}) \simeq \IndCoh_\Nilp(\LS_\cG) \underset{\QCoh(\LS_\cG)}\otimes \QCoh(\LS_\cG)_{\CG_{\fG_{Z_G}}}.$$
```

---

<a id="glc5-corollary-c-twisted-ls-26c5feef"></a>
### Corollary `c:twisted LS`
- **Claim ID:** `GLC5:corollary:c:twisted LS`
- **Location:** `gaits5.tex` lines 5703-5707
- **Context:** 2-Fourier-Mukai transform of the automorphic category
- **Dependencies (outgoing):** 0 — _(none found by label-scan)_
- **Used by (incoming):** 0 — _(none)_

```tex
\label{c:twisted LS} For a $Z_\cG$-gerbe $\fG_{Z_{\cG}}$ on $X$, there is a canonical equivalence $$\Dmod_{\frac{1}{2}}(\Bun_G)_{\CG_{\fG_{Z_{\cG}}}} \simeq \Dmod_{\frac{1}{2}}(\Bun_{G_{\on{sc}}}) \underset{\QCoh(\LS_{\cG_{\on{ad}}})}\otimes \QCoh(\LS_{\cG,\fG_{Z_{\cG}}}).$$
```

---

<a id="glc5-corollary-c-twisted-glc-2-9e3c7504"></a>
### Corollary `c:twisted GLC 2`
- **Claim ID:** `GLC5:corollary:c:twisted GLC 2`
- **Location:** `gaits5.tex` lines 5711-5714
- **Context:** 2-Fourier-Mukai transform of the automorphic category
- **Dependencies (outgoing):** 0 — _(none found by label-scan)_
- **Used by (incoming):** 1 — [`GLC5:remark:auto0071@L5716`](./GLC5.md#glc5-remark-auto0071-l5716-54f7d848)

```tex
\label{c:twisted GLC 2} For $\fG_{Z_{\cG}}\in \on{Ge}_{Z_\cG}(X)$ there is a canonical equivalence $$\Dmod_{\frac{1}{2}}(\Bun_G)_{\CG_{\fG_{Z_{\cG}}}} \simeq \IndCoh_\Nilp(\LS_{\cG,\fG_{Z_{\cG}}}).$$
```

---

<a id="glc5-remark-auto0071-l5716-54f7d848"></a>
### Remark `auto0071@L5716`
- **Claim ID:** `GLC5:remark:auto0071@L5716`
- **Location:** `gaits5.tex` lines 5716-5721
- **Context:** 2-Fourier-Mukai transform of the automorphic category
- **Dependencies (outgoing):** 2 — [`GLC5:corollary:c:twisted GLC 1`](./GLC5.md#glc5-corollary-c-twisted-glc-1-468ef1d0), [`GLC5:corollary:c:twisted GLC 2`](./GLC5.md#glc5-corollary-c-twisted-glc-2-9e3c7504)
- **Used by (incoming):** 0 — _(none)_

- **Unresolved `\*ref{…}` targets (not claims):** 5

```tex
We expect that equivalences parallel to Corollaries \ref{c:twisted GLC 1} and \ref{c:twisted GLC 2} also take place in the framework of Fargues-Scholze theory of \cite{FS}.
```

---


## Review of (semi-)stability for \texorpdfstring{$G$}{stb}-bundles

<a id="glc5-definition-auto0072-l5864-c2fe5771"></a>
### Definition `auto0072@L5864`
- **Claim ID:** `GLC5:definition:auto0072@L5864`
- **Location:** `gaits5.tex` lines 5864-5878
- **Context:** Review of (semi-)stability for \texorpdfstring{$G$}{stb}-bundles / Definition of (semi-)stability
- **Dependencies (outgoing):** 0 — _(none found by label-scan)_
- **Used by (incoming):** 0 — _(none)_

```tex
A $G$-bundle $\CP_G$ on $X$ is \emph{semi-stable} (resp. \emph{stable}) if for every maximal (proper) parabolic subgroup $P \subsetneq G$ and every reduction $\CP_P$ of $\CP_G$ to $P$, we have \[ \langle 2\rhoch_P,\deg(\CP_P)\rangle \leq 0 \,\,\,\, \text{(resp. $< 0$)}. \] \noind…
```

---

<a id="glc5-example-auto0073-l5883-dd2b091c"></a>
### Example `auto0073@L5883`
- **Claim ID:** `GLC5:example:auto0073@L5883`
- **Location:** `gaits5.tex` lines 5883-5898
- **Context:** Review of (semi-)stability for \texorpdfstring{$G$}{stb}-bundles / Definition of (semi-)stability
- **Dependencies (outgoing):** 0 — _(none found by label-scan)_
- **Used by (incoming):** 0 — _(none)_

```tex
This definition is rigged to recover the usual one for $G = GL_n$. \medskip Indeed, suppose $\CE$ has rank $n$ and $P$ is the maximal parabolic whose reductions correspond to subbundles $\CE_0 \subset \CE$ of rank $m$. Then a straightforward calculation yields \[ \langle 2\rhoch_…
```

---

<a id="glc5-proposition-p-semistab-5c2f242e"></a>
### Proposition `p:semistab`
- **Claim ID:** `GLC5:proposition:p:semistab`
- **Location:** `gaits5.tex` lines 5906-5932
- **Context:** Review of (semi-)stability for \texorpdfstring{$G$}{stb}-bundles / A characterization of (semi-)stability
- **Dependencies (outgoing):** 3 — [`GLC5:proposition:p:neutral`](./GLC5.md#glc5-proposition-p-neutral-7b391fb7), [`GLC5:theorem:t:Hecke Z 0`](./GLC5.md#glc5-theorem-t-hecke-z-0-c6bfb40f), [`GLC5:theorem:t:Hecke Z 1`](./GLC5.md#glc5-theorem-t-hecke-z-1-35bfd3aa)
- **Used by (incoming):** 0 — _(none)_

- **Unresolved `\*ref{…}` targets (not claims):** 22

```tex
\label{p:semistab} For a $G$-bundle $\CP_G$ on $X$, the following conditions are equivalent. \medskip \noindent{\em(a)} $\CP_G$ is semi-stable (resp. stable). \noindent{\em(b)} For every proper parabolic subgroup $P \subsetneq G$ (possibly not of corank 1) and every reduction $\C…
```

---

