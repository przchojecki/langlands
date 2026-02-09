# GLC4 claim atlas

- Back to [GLC atlas index](../INDEX.md)
- JSONL with deps: [`GLC4.index.with_deps.jsonl`](./GLC4.index.with_deps.jsonl)

Claims in this file: **78**


## Introduction

<a id="glc4-remark-e-fcd-quant-46f0c8fb"></a>
### Remark `e:FCD quant`
- **Claim ID:** `GLC4:remark:e:FCD quant`
- **Location:** `gaits4.tex` lines 859-877
- **Context:** Introduction
- **Dependencies (outgoing):** 2 — [`GLC4:theorem:t:BG via Op`](./GLC4.md#glc4-theorem-t-bg-via-op-e0ad90d6), [`GLC4:theorem:t:up and down opers`](./GLC4.md#glc4-theorem-t-up-and-down-opers-48b5f333)
- **Used by (incoming):** 0 — _(none)_

- **Unresolved `\*ref{…}` targets (not claims):** 19

```tex
In fact, \eqref{e:FCD} is a special case at levels ($\crit$ for $G$, $\infty$ for $\cG$) of an analogous diagram that is expected to exist in the quantum case: \begin{equation} \label{e:FCD quant} \CD \Whit^!(G)_{\kappa,\Ran} @>{\FLE_{\cG,\check\kappa}^\vee}>{\sim}> \KL(\cG)_{-\c…
```

---


## Summary of the Langlands functor

<a id="glc4-proposition-p-gamma-ff-64870d2e"></a>
### Proposition `p:Gamma ff`
- **Claim ID:** `GLC4:proposition:p:Gamma ff`
- **Location:** `gaits4.tex` lines 1212-1216
- **Context:** Summary of the Langlands functor
- **Dependencies (outgoing):** 0 — _(none found by label-scan)_
- **Used by (incoming):** 4 — [`GLC4:corollary:c:L ff on cusp`](./GLC4.md#glc4-corollary-c-l-ff-on-cusp-605bd325), [`GLC4:corollary:c:loc unital bis`](./GLC4.md#glc4-corollary-c-loc-unital-bis-f5615e0f), [`GLC4:remark:auto0027@L2298`](./GLC4.md#glc4-remark-auto0027-l2298-73a9b1a2), [`GLC4:theorem:t:left adj as dual`](./GLC4.md#glc4-theorem-t-left-adj-as-dual-1e5171bf)

```tex
\label{p:Gamma ff} The functor $$\Gamma^{\on{spec}}_\cG:\QCoh(\LS_\cG)\to \Rep(\cG)_\Ran$$ is fully faithful.
```

---

<a id="glc4-remark-auto0003-l1234-d4df2eee"></a>
### Remark `auto0003@L1234`
- **Claim ID:** `GLC4:remark:auto0003@L1234`
- **Location:** `gaits4.tex` lines 1234-1239
- **Context:** Summary of the Langlands functor
- **Dependencies (outgoing):** 0 — _(none found by label-scan)_
- **Used by (incoming):** 0 — _(none)_

- **Unresolved `\*ref{…}` targets (not claims):** 4

```tex
The commutation of \eqref{e:L and coeff} is the point of departure for any of the constructions of the Langlands functor.
```

---

<a id="glc4-theorem-t-equiv-on-eis-c6ebff6d"></a>
### Theorem `t:equiv on Eis`
- **Claim ID:** `GLC4:theorem:t:equiv on Eis`
- **Location:** `gaits4.tex` lines 1338-1340
- **Context:** Summary of the Langlands functor
- **Dependencies (outgoing):** 0 — _(none found by label-scan)_
- **Used by (incoming):** 3 — [`GLC4:corollary:c:reduce to A irred`](./GLC4.md#glc4-corollary-c-reduce-to-a-irred-52a3101a), [`GLC4:corollary:e:LL cusp diagram in`](./GLC4.md#glc4-corollary-e-ll-cusp-diagram-in-7eb5ff55), [`GLC4:theorem:t:L is cons`](./GLC4.md#glc4-theorem-t-l-is-cons-a81cfa81)

- **Unresolved `\*ref{…}` targets (not claims):** 5

```tex
\label{t:equiv on Eis} The adjoint functors in \eqref{e:L and LL on Eis} are (mutually inverse) equivalences.
```

---

<a id="glc4-proposition-p-ll-preserves-cusp-8b2c657b"></a>
### Proposition `p:LL preserves cusp`
- **Claim ID:** `GLC4:proposition:p:LL preserves cusp`
- **Location:** `gaits4.tex` lines 1439-1441
- **Context:** Summary of the Langlands functor
- **Dependencies (outgoing):** 0 — _(none found by label-scan)_
- **Used by (incoming):** 2 — [`GLC4:corollary:c:reduce to cusp`](./GLC4.md#glc4-corollary-c-reduce-to-cusp-a9bdd208), [`GLC4:theorem:t:cusp is irred`](./GLC4.md#glc4-theorem-t-cusp-is-irred-6dce0e94)

- **Unresolved `\*ref{…}` targets (not claims):** 1

```tex
\label{p:LL preserves cusp} The functor $\BL^L_G$ sends $\IndCoh_\Nilp(\LS^{\on{irred}}_\cG)$ to $\Dmod_{\frac{1}{2}}(\Bun_G)_{\on{cusp}}$.
```

---

<a id="glc4-corollary-e-ll-cusp-diagram-in-7eb5ff55"></a>
### Corollary `e:LL cusp diagram in`
- **Claim ID:** `GLC4:corollary:e:LL cusp diagram in`
- **Location:** `gaits4.tex` lines 1449-1458
- **Context:** Summary of the Langlands functor
- **Dependencies (outgoing):** 1 — [`GLC4:theorem:t:equiv on Eis`](./GLC4.md#glc4-theorem-t-equiv-on-eis-c6ebff6d)
- **Used by (incoming):** 0 — _(none)_

```tex
The following diagram commutes: \begin{equation} \label{e:LL cusp diagram in} \CD \Dmod_{\frac{1}{2}}(\Bun_G) @<{\BL^L_G}<< \IndCoh_\Nilp(\LS_\cG) \\ @A{\be}AA @AA{\jmath_*}A \\ \Dmod_{\frac{1}{2}}(\Bun_G)_{\on{cusp}} @<{\BL^L_{G,\on{cusp}}}<< \IndCoh_\Nilp(\LS^{\on{irred}}_\cG).…
```

---

<a id="glc4-corollary-c-reduce-to-cusp-a9bdd208"></a>
### Corollary `c:reduce to cusp`
- **Claim ID:** `GLC4:corollary:c:reduce to cusp`
- **Location:** `gaits4.tex` lines 1464-1466
- **Context:** Summary of the Langlands functor
- **Dependencies (outgoing):** 1 — [`GLC4:proposition:p:LL preserves cusp`](./GLC4.md#glc4-proposition-p-ll-preserves-cusp-8b2c657b)
- **Used by (incoming):** 1 — [`GLC4:theorem:t:L is cons`](./GLC4.md#glc4-theorem-t-l-is-cons-a81cfa81)

- **Unresolved `\*ref{…}` targets (not claims):** 4

```tex
\label{c:reduce to cusp} The functor $\BL_G$ is an equivalence if and only if so is the functor $\BL_{G,\on{cusp}}$.
```

---

<a id="glc4-proposition-p-eis-is-red-bbc242b2"></a>
### Proposition `p:Eis is red`
- **Claim ID:** `GLC4:proposition:p:Eis is red`
- **Location:** `gaits4.tex` lines 1567-1574
- **Context:** Summary of the Langlands functor
- **Dependencies (outgoing):** 0 — _(none found by label-scan)_
- **Used by (incoming):** 1 — [`GLC4:theorem:t:cusp is irred`](./GLC4.md#glc4-theorem-t-cusp-is-irred-6dce0e94)

- **Unresolved `\*ref{…}` targets (not claims):** 1

```tex
\label{p:Eis is red} With respect to the $\QCoh(\LS_\cG)$-action on $\Dmod_{\frac{1}{2}}(\Bun_G)$, the full subcategory $$\Dmod_{\frac{1}{2}}(\Bun_G)_{\Eis}\subset \Dmod_{\frac{1}{2}}(\Bun_G)$$ is set-theoretically supported on $\LS_\cG^{\on{red}}$, i.e., \begin{equation} \label{…
```

---

<a id="glc4-corollary-c-irrred-is-cusp-46d07f3e"></a>
### Corollary `c:irrred is cusp`
- **Claim ID:** `GLC4:corollary:c:irrred is cusp`
- **Location:** `gaits4.tex` lines 1582-1589
- **Context:** Summary of the Langlands functor
- **Dependencies (outgoing):** 0 — _(none found by label-scan)_
- **Used by (incoming):** 2 — [`GLC4:proposition:p:dual of Poinc`](./GLC4.md#glc4-proposition-p-dual-of-poinc-cec7228a), [`GLC4:theorem:t:cusp is irred`](./GLC4.md#glc4-theorem-t-cusp-is-irred-6dce0e94)

- **Unresolved `\*ref{…}` targets (not claims):** 1

```tex
\label{c:irrred is cusp} We have an inclusion \begin{equation} \label{e:irred is cusp} \Dmod_{\frac{1}{2}}(\Bun_G)\underset{\QCoh(\LS_\cG)}\otimes \QCoh(\LS^{\on{irred}}_\cG) \subset \Dmod_{\frac{1}{2}}(\Bun_G)_{\on{cusp}} \end{equation} as full subcategories of $\Dmod_{\frac{1}{…
```

---

<a id="glc4-theorem-t-cusp-is-irred-6dce0e94"></a>
### Theorem `t:cusp is irred`
- **Claim ID:** `GLC4:theorem:t:cusp is irred`
- **Location:** `gaits4.tex` lines 1593-1595
- **Context:** Summary of the Langlands functor
- **Dependencies (outgoing):** 3 — [`GLC4:corollary:c:irrred is cusp`](./GLC4.md#glc4-corollary-c-irrred-is-cusp-46d07f3e), [`GLC4:proposition:p:Eis is red`](./GLC4.md#glc4-proposition-p-eis-is-red-bbc242b2), [`GLC4:proposition:p:LL preserves cusp`](./GLC4.md#glc4-proposition-p-ll-preserves-cusp-8b2c657b)
- **Used by (incoming):** 1 — [`GLC4:theorem:t:L is cons`](./GLC4.md#glc4-theorem-t-l-is-cons-a81cfa81)

- **Unresolved `\*ref{…}` targets (not claims):** 1

```tex
\label{t:cusp is irred} The inclusion \eqref{e:irred is cusp} is an equality.
```

---

<a id="glc4-theorem-t-cusp-cons-e5bedcfa"></a>
### Theorem `t:cusp cons`
- **Claim ID:** `GLC4:theorem:t:cusp cons`
- **Location:** `gaits4.tex` lines 1659-1661
- **Context:** Summary of the Langlands functor
- **Dependencies (outgoing):** 0 — _(none found by label-scan)_
- **Used by (incoming):** 2 — [`GLC4:remark:auto0012@L1663`](./GLC4.md#glc4-remark-auto0012-l1663-5f67982d), [`GLC4:theorem:t:L is cons`](./GLC4.md#glc4-theorem-t-l-is-cons-a81cfa81)

```tex
\label{t:cusp cons} The functor $\BL_{G,\on{cusp}}$ is conservative.
```

---

<a id="glc4-remark-auto0012-l1663-5f67982d"></a>
### Remark `auto0012@L1663`
- **Claim ID:** `GLC4:remark:auto0012@L1663`
- **Location:** `gaits4.tex` lines 1663-1666
- **Context:** Summary of the Langlands functor
- **Dependencies (outgoing):** 2 — [`GLC4:theorem:t:coeff ff on cusp`](./GLC4.md#glc4-theorem-t-coeff-ff-on-cusp-4f0c4b31), [`GLC4:theorem:t:cusp cons`](./GLC4.md#glc4-theorem-t-cusp-cons-e5bedcfa)
- **Used by (incoming):** 0 — _(none)_

```tex
Note that in the case when $G=GL_n$, the assertion of \thmref{t:cusp cons} follows immediately from (the much more elementary) \thmref{t:coeff ff on cusp} below.
```

---

<a id="glc4-theorem-t-l-is-cons-a81cfa81"></a>
### Theorem `t:L is cons`
- **Claim ID:** `GLC4:theorem:t:L is cons`
- **Location:** `gaits4.tex` lines 1672-1674
- **Context:** Summary of the Langlands functor
- **Dependencies (outgoing):** 4 — [`GLC4:corollary:c:reduce to cusp`](./GLC4.md#glc4-corollary-c-reduce-to-cusp-a9bdd208), [`GLC4:theorem:t:cusp cons`](./GLC4.md#glc4-theorem-t-cusp-cons-e5bedcfa), [`GLC4:theorem:t:cusp is irred`](./GLC4.md#glc4-theorem-t-cusp-is-irred-6dce0e94), [`GLC4:theorem:t:equiv on Eis`](./GLC4.md#glc4-theorem-t-equiv-on-eis-c6ebff6d)
- **Used by (incoming):** 0 — _(none)_

- **Unresolved `\*ref{…}` targets (not claims):** 4

```tex
\label{t:L is cons} The functor $\BL_G$ is conservative.
```

---

<a id="glc4-corollary-c-reduce-to-a-irred-52a3101a"></a>
### Corollary `c:reduce to A irred`
- **Claim ID:** `GLC4:corollary:c:reduce to A irred`
- **Location:** `gaits4.tex` lines 1753-1756
- **Context:** Summary of the Langlands functor
- **Dependencies (outgoing):** 1 — [`GLC4:theorem:t:equiv on Eis`](./GLC4.md#glc4-theorem-t-equiv-on-eis-c6ebff6d)
- **Used by (incoming):** 2 — [`GLC4:corollary:auto0040@L3166`](./GLC4.md#glc4-corollary-auto0040-l3166-d8892f13), [`GLC4:remark:auto0017@L1815`](./GLC4.md#glc4-remark-auto0017-l1815-4cc68c4d)

- **Unresolved `\*ref{…}` targets (not claims):** 1

```tex
\label{c:reduce to A irred} The functor $\BL_G$ is an equivalence if and only if the map \eqref{e:unit map A} is an isomorphism in $\QCoh(\LS^{\on{irred}}_\cG)$.
```

---

<a id="glc4-theorem-t-coeff-ff-on-cusp-4f0c4b31"></a>
### Theorem `t:coeff ff on cusp`
- **Claim ID:** `GLC4:theorem:t:coeff ff on cusp`
- **Location:** `gaits4.tex` lines 1766-1770
- **Context:** Summary of the Langlands functor
- **Dependencies (outgoing):** 0 — _(none found by label-scan)_
- **Used by (incoming):** 2 — [`GLC4:remark:auto0012@L1663`](./GLC4.md#glc4-remark-auto0012-l1663-5f67982d), [`GLC4:remark:auto0017@L1815`](./GLC4.md#glc4-remark-auto0017-l1815-4cc68c4d)

```tex
\label{t:coeff ff on cusp} The restriction of the functor $\on{coeff}_G$ to the subcategory $$\Dmod_{\frac{1}{2}}(\Bun_G)_{\on{cusp}}\subset \Dmod_{\frac{1}{2}}(\Bun_G)$$ is fully faithful.
```

---

<a id="glc4-corollary-c-l-ff-on-cusp-605bd325"></a>
### Corollary `c:L ff on cusp`
- **Claim ID:** `GLC4:corollary:c:L ff on cusp`
- **Location:** `gaits4.tex` lines 1776-1778
- **Context:** Summary of the Langlands functor
- **Dependencies (outgoing):** 1 — [`GLC4:proposition:p:Gamma ff`](./GLC4.md#glc4-proposition-p-gamma-ff-64870d2e)
- **Used by (incoming):** 1 — [`GLC4:remark:auto0017@L1815`](./GLC4.md#glc4-remark-auto0017-l1815-4cc68c4d)

- **Unresolved `\*ref{…}` targets (not claims):** 3

```tex
\label{c:L ff on cusp} The functor $\BL_{G,\on{cusp}}$ is fully faithful.
```

---

<a id="glc4-remark-auto0017-l1815-4cc68c4d"></a>
### Remark `auto0017@L1815`
- **Claim ID:** `GLC4:remark:auto0017@L1815`
- **Location:** `gaits4.tex` lines 1815-1819
- **Context:** Summary of the Langlands functor
- **Dependencies (outgoing):** 3 — [`GLC4:corollary:c:L ff on cusp`](./GLC4.md#glc4-corollary-c-l-ff-on-cusp-605bd325), [`GLC4:corollary:c:reduce to A irred`](./GLC4.md#glc4-corollary-c-reduce-to-a-irred-52a3101a), [`GLC4:theorem:t:coeff ff on cusp`](./GLC4.md#glc4-theorem-t-coeff-ff-on-cusp-4f0c4b31)
- **Used by (incoming):** 0 — _(none)_

- **Unresolved `\*ref{…}` targets (not claims):** 2

```tex
Note that the proof of \corref{c:L ff on cusp} shows that it is actually logically equivalent to \thmref{t:coeff ff on cusp}. Hence, once we establish GLC, we will know that \thmref{t:coeff ff on cusp} also holds for any $G$.
```

---

<a id="glc4-remark-auto0018-l1861-1526032f"></a>
### Remark `auto0018@L1861`
- **Claim ID:** `GLC4:remark:auto0018@L1861`
- **Location:** `gaits4.tex` lines 1861-1867
- **Context:** Summary of the Langlands functor
- **Dependencies (outgoing):** 0 — _(none found by label-scan)_
- **Used by (incoming):** 0 — _(none)_

- **Unresolved `\*ref{…}` targets (not claims):** 5

```tex
Alternatively, the proof of the existence of a non-zero Hecke eigensheaf for a given irreducible local system, valid for any $G$, follows by combining the \cite{BD1} construction of Hecke eigensheaves via localization at the critical level and the result of \cite{Ari}, which says…
```

---


## Left adjoint as the dual

<a id="glc4-theorem-t-simple-kevin-82f64555"></a>
### Theorem `t:simple Kevin`
- **Claim ID:** `GLC4:theorem:t:simple Kevin`
- **Location:** `gaits4.tex` lines 2053-2058
- **Context:** Left adjoint as the dual
- **Dependencies (outgoing):** 0 — _(none found by label-scan)_
- **Used by (incoming):** 2 — [`GLC4:proposition:p:dual of Poinc`](./GLC4.md#glc4-proposition-p-dual-of-poinc-cec7228a), [`GLC4:theorem:t:left adj as dual`](./GLC4.md#glc4-theorem-t-left-adj-as-dual-1e5171bf)

- **Unresolved `\*ref{…}` targets (not claims):** 1

```tex
\label{t:simple Kevin} The functors $$\be^L\circ \on{Poinc}_{G,!}\circ \Theta_{\Whit(G)} \text{ and } \be^L\circ \on{Ps-Id}^{\on{nv}} \circ \on{Poinc}_{G,*}[2\delta_{N_{\rho(\omega_X)}}],$$ $$\Whit_*(G)_\Ran\rightrightarrows \Dmod_{\frac{1}{2}}(\Bun_G)_{\on{cusp}}$$ are canonical…
```

---

<a id="glc4-lemma-l-loc-spec-and-dual-8f2002a0"></a>
### Lemma `l:Loc spec and dual`
- **Claim ID:** `GLC4:lemma:l:Loc spec and dual`
- **Location:** `gaits4.tex` lines 2092-2099
- **Context:** Left adjoint as the dual
- **Dependencies (outgoing):** 1 — [`GLC4:theorem:t:left adj as dual`](./GLC4.md#glc4-theorem-t-left-adj-as-dual-1e5171bf)
- **Used by (incoming):** 1 — [`GLC4:proposition:p:Loc crit is Loc`](./GLC4.md#glc4-proposition-p-loc-crit-is-loc-7db7c87a)

- **Unresolved `\*ref{…}` targets (not claims):** 3

```tex
\label{l:Loc spec and dual} With respect to the above self-dualities of $\QCoh(\LS_\cG)$ and $\Rep(\cG)_\Ran$, the functors $$\Loc_\cG^{\on{spec}}:\Rep(\cG)_\Ran \leftrightarrow \QCoh(\LS_\cG):\Gamma^{\on{spec}}_\cG$$ identify with each other's duals: $$(\Loc_\cG^{\on{spec}})^\ve…
```

---

<a id="glc4-theorem-t-left-adj-as-dual-1e5171bf"></a>
### Theorem `t:left adj as dual`
- **Claim ID:** `GLC4:theorem:t:left adj as dual`
- **Location:** `gaits4.tex` lines 2127-2129
- **Context:** Left adjoint as the dual
- **Dependencies (outgoing):** 2 — [`GLC4:proposition:p:Gamma ff`](./GLC4.md#glc4-proposition-p-gamma-ff-64870d2e), [`GLC4:theorem:t:simple Kevin`](./GLC4.md#glc4-theorem-t-simple-kevin-82f64555)
- **Used by (incoming):** 2 — [`GLC4:lemma:l:Loc spec and dual`](./GLC4.md#glc4-lemma-l-loc-spec-and-dual-8f2002a0), [`GLC4:theorem:t:right adj as dual`](./GLC4.md#glc4-theorem-t-right-adj-as-dual-7d895284)

- **Unresolved `\*ref{…}` targets (not claims):** 12

```tex
\label{t:left adj as dual} The functor $\Phi_{G,\on{cusp}}$ identifies canonically with $\BL^L_{G,\on{cusp}}$.
```

---


## Right adjoint as the dual

<a id="glc4-theorem-t-right-adj-as-dual-7d895284"></a>
### Theorem `t:right adj as dual`
- **Claim ID:** `GLC4:theorem:t:right adj as dual`
- **Location:** `gaits4.tex` lines 2258-2260
- **Context:** Right adjoint as the dual
- **Dependencies (outgoing):** 1 — [`GLC4:theorem:t:left adj as dual`](./GLC4.md#glc4-theorem-t-left-adj-as-dual-1e5171bf)
- **Used by (incoming):** 2 — [`GLC4:proposition:p:dual of Poinc`](./GLC4.md#glc4-proposition-p-dual-of-poinc-cec7228a), [`GLC4:remark:auto0027@L2298`](./GLC4.md#glc4-remark-auto0027-l2298-73a9b1a2)

```tex
\label{t:right adj as dual} The functor $\Phi_{G,\on{cusp}}$ identifies canonically with the right adjoint of $\BL_{G,\on{cusp}}$.
```

---

<a id="glc4-theorem-t-ambidex-4d339207"></a>
### Theorem `t:ambidex`
- **Claim ID:** `GLC4:theorem:t:ambidex`
- **Location:** `gaits4.tex` lines 2267-2269
- **Context:** Right adjoint as the dual
- **Dependencies (outgoing):** 0 — _(none found by label-scan)_
- **Used by (incoming):** 1 — [`GLC4:proposition:p:dual of Poinc`](./GLC4.md#glc4-proposition-p-dual-of-poinc-cec7228a)

```tex
\label{t:ambidex} The left and right adjoints of $\BL_{G,\on{cusp}}$ are isomorphic.
```

---

<a id="glc4-corollary-c-comp-self-adj-0b9eb1da"></a>
### Corollary `c:comp self-adj`
- **Claim ID:** `GLC4:corollary:c:comp self-adj`
- **Location:** `gaits4.tex` lines 2271-2275
- **Context:** Right adjoint as the dual
- **Dependencies (outgoing):** 0 — _(none found by label-scan)_
- **Used by (incoming):** 0 — _(none)_

- **Unresolved `\*ref{…}` targets (not claims):** 1

```tex
\label{c:comp self-adj} The endofunctor $$\BL_{G,\on{cusp}}\circ \BL^L_{G,\on{cusp}}$$ of $\QCoh(\LS^{\on{irred}}_\cG)$ is isomorphic to its own left and right adjoint.
```

---

<a id="glc4-corollary-c-a-g-irred-b83277ef"></a>
### Corollary `c:A G irred`
- **Claim ID:** `GLC4:corollary:c:A G irred`
- **Location:** `gaits4.tex` lines 2285-2288
- **Context:** Right adjoint as the dual
- **Dependencies (outgoing):** 0 — _(none found by label-scan)_
- **Used by (incoming):** 2 — [`GLC4:proposition:p:finite monodromy`](./GLC4.md#glc4-proposition-p-finite-monodromy-73225a7d), [`GLC4:remark:auto0034@L2986`](./GLC4.md#glc4-remark-auto0034-l2986-ada84eb4)

- **Unresolved `\*ref{…}` targets (not claims):** 1

```tex
\label{c:A G irred} The object $\CA_{G,\on{irred}}\in \QCoh(\LS^{\on{irred}}_\cG)$ is self-dual. In particular, it belongs to $\QCoh(\LS^{\on{irred}}_\cG)^{\on{perf}}$, i.e., it is compact.
```

---

<a id="glc4-theorem-t-a-g-irred-d1ec2835"></a>
### Theorem `t:A G irred`
- **Claim ID:** `GLC4:theorem:t:A G irred`
- **Location:** `gaits4.tex` lines 2292-2296
- **Context:** Right adjoint as the dual
- **Dependencies (outgoing):** 2 — [`GLC4:corollary:c:A=B Op`](./GLC4.md#glc4-corollary-c-a-b-op-48157763), [`GLC4:proposition:p:finite monodromy`](./GLC4.md#glc4-proposition-p-finite-monodromy-73225a7d)
- **Used by (incoming):** 3 — [`GLC4:corollary:c:BG is compact`](./GLC4.md#glc4-corollary-c-bg-is-compact-4a39443c), [`GLC4:proposition:p:dual of Poinc`](./GLC4.md#glc4-proposition-p-dual-of-poinc-cec7228a), [`GLC4:proposition:p:finite monodromy`](./GLC4.md#glc4-proposition-p-finite-monodromy-73225a7d)

```tex
\label{t:A G irred} The object $\CA_{G,\on{irred}}\in \QCoh(\LS^{\on{irred}}_\cG)$ is a classical vector bundle, which is equipped with a naturally defined flat connection\footnote{Note that \corref{c:A=B Op} and \propref{p:finite monodromy} imply that the resulting local system…
```

---

<a id="glc4-remark-auto0027-l2298-73a9b1a2"></a>
### Remark `auto0027@L2298`
- **Claim ID:** `GLC4:remark:auto0027@L2298`
- **Location:** `gaits4.tex` lines 2298-2302
- **Context:** Right adjoint as the dual
- **Dependencies (outgoing):** 2 — [`GLC4:proposition:p:Gamma ff`](./GLC4.md#glc4-proposition-p-gamma-ff-64870d2e), [`GLC4:theorem:t:right adj as dual`](./GLC4.md#glc4-theorem-t-right-adj-as-dual-7d895284)
- **Used by (incoming):** 0 — _(none)_

```tex
Note that it makes sense to talk about classical vector bundles on $\LS^{\on{irred}}_\cG$, since, under the assumption that $\cG$ is semi-simple, the stack $\LS^{\on{irred}}_\cG$ is classical and smooth.
```

---

<a id="glc4-proposition-p-loc-crit-is-loc-7db7c87a"></a>
### Proposition `p:Loc crit is Loc`
- **Claim ID:** `GLC4:proposition:p:Loc crit is Loc`
- **Location:** `gaits4.tex` lines 2327-2329
- **Context:** Right adjoint as the dual
- **Dependencies (outgoing):** 1 — [`GLC4:lemma:l:Loc spec and dual`](./GLC4.md#glc4-lemma-l-loc-spec-and-dual-8f2002a0)
- **Used by (incoming):** 2 — [`GLC4:proposition:p:Loc crit and dual`](./GLC4.md#glc4-proposition-p-loc-crit-and-dual-36872e7e), [`GLC4:proposition:p:dual of Poinc`](./GLC4.md#glc4-proposition-p-dual-of-poinc-cec7228a)

- **Unresolved `\*ref{…}` targets (not claims):** 4

```tex
\label{p:Loc crit is Loc} The functor $\Loc_{G,\on{cusp}}$ is Verdier quotient.
```

---

<a id="glc4-proposition-p-loc-crit-and-dual-36872e7e"></a>
### Proposition `p:Loc crit and dual`
- **Claim ID:** `GLC4:proposition:p:Loc crit and dual`
- **Location:** `gaits4.tex` lines 2359-2363
- **Context:** Right adjoint as the dual
- **Dependencies (outgoing):** 1 — [`GLC4:proposition:p:Loc crit is Loc`](./GLC4.md#glc4-proposition-p-loc-crit-is-loc-7db7c87a)
- **Used by (incoming):** 1 — [`GLC4:proposition:p:dual of Poinc`](./GLC4.md#glc4-proposition-p-dual-of-poinc-cec7228a)

- **Unresolved `\*ref{…}` targets (not claims):** 2

```tex
\label{p:Loc crit and dual} We have a canonical identification between $\Loc_{G,\on{cusp}}^\vee$ and $$\Loc_{G,\on{cusp}}^R\otimes \det(\Gamma(X,\CO_X)\otimes \fg)[\delta_G],$$ where $\delta_G=\dim(\Bun_G)$.
```

---

<a id="glc4-proposition-p-dual-of-poinc-cec7228a"></a>
### Proposition `p:dual of Poinc`
- **Claim ID:** `GLC4:proposition:p:dual of Poinc`
- **Location:** `gaits4.tex` lines 2463-2468
- **Context:** Right adjoint as the dual
- **Dependencies (outgoing):** 8 — [`GLC4:corollary:c:irrred is cusp`](./GLC4.md#glc4-corollary-c-irrred-is-cusp-46d07f3e), [`GLC4:proposition:p:Loc crit and dual`](./GLC4.md#glc4-proposition-p-loc-crit-and-dual-36872e7e), [`GLC4:proposition:p:Loc crit is Loc`](./GLC4.md#glc4-proposition-p-loc-crit-is-loc-7db7c87a), [`GLC4:remark:r:Nilp amb`](./GLC4.md#glc4-remark-r-nilp-amb-fe7e1f3b), [`GLC4:theorem:t:A G irred`](./GLC4.md#glc4-theorem-t-a-g-irred-d1ec2835), [`GLC4:theorem:t:ambidex`](./GLC4.md#glc4-theorem-t-ambidex-4d339207), [`GLC4:theorem:t:right adj as dual`](./GLC4.md#glc4-theorem-t-right-adj-as-dual-7d895284), [`GLC4:theorem:t:simple Kevin`](./GLC4.md#glc4-theorem-t-simple-kevin-82f64555)
- **Used by (incoming):** 0 — _(none)_

- **Unresolved `\*ref{…}` targets (not claims):** 19

```tex
\label{p:dual of Poinc} With respect to the self-dualities \eqref{e:opers self-dual} and \eqref{e:naive self-dual QCoh irred}, we have a canonical identification between the functor \emph{dual} to $\on{Poinc}^{\on{spec}}_{\cG,*,\on{irred}}$ and $$(\on{Poinc}^{\on{spec}}_{\cG,*,\o…
```

---

<a id="glc4-theorem-auto0031-l2892-37ac20eb"></a>
### Theorem `auto0031@L2892`
- **Claim ID:** `GLC4:theorem:auto0031@L2892`
- **Location:** `gaits4.tex` lines 2892-2897
- **Context:** Right adjoint as the dual
- **Dependencies (outgoing):** 0 — _(none found by label-scan)_
- **Used by (incoming):** 0 — _(none)_

```tex
For any $\CF'\in \Dmod_{\frac{1}{2},\Nilp}(\Bun_G)$ and any $\CF''\in \Dmod_{\frac{1}{2}}(\Bun_G)_{\on{co}}$, there is a canonical isomorphism $$\on{C}^\cdot_c(\Bun_G,\CF'\overset{*}\otimes \Mir_{\Bun_G}(\CF''))\simeq \on{C}^\cdot(\Bun_G,\CF'\sotimes \CF'').$$
```

---

<a id="glc4-remark-r-nilp-amb-fe7e1f3b"></a>
### Remark `r:Nilp amb`
- **Claim ID:** `GLC4:remark:r:Nilp amb`
- **Location:** `gaits4.tex` lines 2899-2908
- **Context:** Right adjoint as the dual
- **Dependencies (outgoing):** 0 — _(none found by label-scan)_
- **Used by (incoming):** 1 — [`GLC4:proposition:p:dual of Poinc`](./GLC4.md#glc4-proposition-p-dual-of-poinc-cec7228a)

- **Unresolved `\*ref{…}` targets (not claims):** 1

```tex
\label{r:Nilp amb} The above argument can be generalized so that it proves ambidexterity for the functor induced by $\BL_G$ $$\Dmod_{\frac{1}{2},\Nilp}(\Bun_G)_{\on{cusp}}\to \IndCoh(\LS^{\on{irred,restr}}_\cG),$$ where $$\Dmod_{\frac{1}{2},\Nilp}(\Bun_G)_{\on{cusp}}:=\Dmod_{\fra…
```

---


## The expression for \texorpdfstring{$\CA_{G,\on{irred}}$}{AGirred} via opers

<a id="glc4-theorem-t-bg-via-op-e0ad90d6"></a>
### Theorem `t:BG via Op`
- **Claim ID:** `GLC4:theorem:t:BG via Op`
- **Location:** `gaits4.tex` lines 2980-2984
- **Context:** The expression for \texorpdfstring{$\CA_{G,\on{irred}}$}{AGirred} via opers
- **Dependencies (outgoing):** 0 — _(none found by label-scan)_
- **Used by (incoming):** 7 — [`GLC4:corollary:c:A=B`](./GLC4.md#glc4-corollary-c-a-b-f86d6f0d), [`GLC4:proposition:p:finite monodromy`](./GLC4.md#glc4-proposition-p-finite-monodromy-73225a7d), [`GLC4:remark:auto0034@L2986`](./GLC4.md#glc4-remark-auto0034-l2986-ada84eb4), [`GLC4:remark:auto0046@L3226`](./GLC4.md#glc4-remark-auto0046-l3226-844357d4), [`GLC4:remark:e:FCD quant`](./GLC4.md#glc4-remark-e-fcd-quant-46f0c8fb), [`GLC4:remark:r:coalg`](./GLC4.md#glc4-remark-r-coalg-3bef2d80), [`GLC4:theorem:t:up and down opers`](./GLC4.md#glc4-theorem-t-up-and-down-opers-48b5f333)

```tex
\label{t:BG via Op} There exists a canonical isomorphism between $$\CB_{G,\on{irred}}\simeq \CB^{\Op}_{G,\on{irred}}$$ as plain objects of $\QCoh(\LS^{\on{irred}}_\cG)$.
```

---

<a id="glc4-remark-auto0034-l2986-ada84eb4"></a>
### Remark `auto0034@L2986`
- **Claim ID:** `GLC4:remark:auto0034@L2986`
- **Location:** `gaits4.tex` lines 2986-2989
- **Context:** The expression for \texorpdfstring{$\CA_{G,\on{irred}}$}{AGirred} via opers
- **Dependencies (outgoing):** 3 — [`GLC4:corollary:c:A G irred`](./GLC4.md#glc4-corollary-c-a-g-irred-b83277ef), [`GLC4:remark:r:coalg`](./GLC4.md#glc4-remark-r-coalg-3bef2d80), [`GLC4:theorem:t:BG via Op`](./GLC4.md#glc4-theorem-t-bg-via-op-e0ad90d6)
- **Used by (incoming):** 0 — _(none)_

```tex
One can show that the isomorphism of \thmref{t:BG via Op} respects the co-associative coalgebra structures on the two sides. However, we will neither prove\footnote{See, however, Remark \ref{r:coalg}.} nor use this.
```

---

<a id="glc4-corollary-c-a-b-f86d6f0d"></a>
### Corollary `c:A=B`
- **Claim ID:** `GLC4:corollary:c:A=B`
- **Location:** `gaits4.tex` lines 3009-3013
- **Context:** The expression for \texorpdfstring{$\CA_{G,\on{irred}}$}{AGirred} via opers
- **Dependencies (outgoing):** 1 — [`GLC4:theorem:t:BG via Op`](./GLC4.md#glc4-theorem-t-bg-via-op-e0ad90d6)
- **Used by (incoming):** 0 — _(none)_

```tex
\label{c:A=B} There is a canonical isomorphism $$\CA_{G,\on{irred}}\simeq \CB_{G,\on{irred}}$$ as objects of $\QCoh(\LS^{\on{irred}}_\cG)$.
```

---

<a id="glc4-corollary-c-a-b-op-48157763"></a>
### Corollary `c:A=B Op`
- **Claim ID:** `GLC4:corollary:c:A=B Op`
- **Location:** `gaits4.tex` lines 3019-3023
- **Context:** The expression for \texorpdfstring{$\CA_{G,\on{irred}}$}{AGirred} via opers
- **Dependencies (outgoing):** 0 — _(none found by label-scan)_
- **Used by (incoming):** 2 — [`GLC4:proposition:p:finite monodromy`](./GLC4.md#glc4-proposition-p-finite-monodromy-73225a7d), [`GLC4:theorem:t:A G irred`](./GLC4.md#glc4-theorem-t-a-g-irred-d1ec2835)

```tex
\label{c:A=B Op} There is a canonical isomorphism $$\CA_{G,\on{irred}}\simeq \CB^{\Op}_{G,\on{irred}}$$ as objects of $\QCoh(\LS^{\on{irred}}_\cG)$.
```

---

<a id="glc4-corollary-c-bg-is-compact-4a39443c"></a>
### Corollary `c:BG is compact`
- **Claim ID:** `GLC4:corollary:c:BG is compact`
- **Location:** `gaits4.tex` lines 3027-3029
- **Context:** The expression for \texorpdfstring{$\CA_{G,\on{irred}}$}{AGirred} via opers
- **Dependencies (outgoing):** 1 — [`GLC4:theorem:t:A G irred`](./GLC4.md#glc4-theorem-t-a-g-irred-d1ec2835)
- **Used by (incoming):** 0 — _(none)_

- **Unresolved `\*ref{…}` targets (not claims):** 1

```tex
\label{c:BG is compact} The object $\CB^{\Op}_{G,\on{irred}}\in \QCoh(\LS^{\on{irred}}_\cG)$ is compact.
```

---

<a id="glc4-proposition-p-finite-monodromy-73225a7d"></a>
### Proposition `p:finite monodromy`
- **Claim ID:** `GLC4:proposition:p:finite monodromy`
- **Location:** `gaits4.tex` lines 3047-3050
- **Context:** The expression for \texorpdfstring{$\CA_{G,\on{irred}}$}{AGirred} via opers
- **Dependencies (outgoing):** 4 — [`GLC4:corollary:c:A G irred`](./GLC4.md#glc4-corollary-c-a-g-irred-b83277ef), [`GLC4:corollary:c:A=B Op`](./GLC4.md#glc4-corollary-c-a-b-op-48157763), [`GLC4:theorem:t:A G irred`](./GLC4.md#glc4-theorem-t-a-g-irred-d1ec2835), [`GLC4:theorem:t:BG via Op`](./GLC4.md#glc4-theorem-t-bg-via-op-e0ad90d6)
- **Used by (incoming):** 1 — [`GLC4:theorem:t:A G irred`](./GLC4.md#glc4-theorem-t-a-g-irred-d1ec2835)

```tex
\label{p:finite monodromy} The local system $\ul\CB^{\Op}_{G,\on{irred}}$ has a finite monodromy, i.e., it trivializes over a finite \'etale cover of $\LS^{\on{irred}}_\cG$.
```

---

<a id="glc4-corollary-auto0039-l3159-c554f40a"></a>
### Corollary `auto0039@L3159`
- **Claim ID:** `GLC4:corollary:auto0039@L3159`
- **Location:** `gaits4.tex` lines 3159-3162
- **Context:** The expression for \texorpdfstring{$\CA_{G,\on{irred}}$}{AGirred} via opers
- **Dependencies (outgoing):** 0 — _(none found by label-scan)_
- **Used by (incoming):** 0 — _(none)_

```tex
The homology of the fibers of the map $\pi^{\on{irred}}_\Ran$ is acyclic off degree $0$.
```

---

<a id="glc4-corollary-auto0040-l3166-d8892f13"></a>
### Corollary `auto0040@L3166`
- **Claim ID:** `GLC4:corollary:auto0040@L3166`
- **Location:** `gaits4.tex` lines 3166-3168
- **Context:** The expression for \texorpdfstring{$\CA_{G,\on{irred}}$}{AGirred} via opers
- **Dependencies (outgoing):** 1 — [`GLC4:corollary:c:reduce to A irred`](./GLC4.md#glc4-corollary-c-reduce-to-a-irred-52a3101a)
- **Used by (incoming):** 0 — _(none)_

```tex
The connected components of the fibers of the map $\pi^{\on{irred}}_\Ran$ are homologically contractible.
```

---

<a id="glc4-corollary-c-conn-of-opers-01b443a8"></a>
### Corollary `c:conn of opers`
- **Claim ID:** `GLC4:corollary:c:conn of opers`
- **Location:** `gaits4.tex` lines 3174-3189
- **Context:** The expression for \texorpdfstring{$\CA_{G,\on{irred}}$}{AGirred} via opers
- **Dependencies (outgoing):** 0 — _(none found by label-scan)_
- **Used by (incoming):** 0 — _(none)_

```tex
\label{c:conn of opers} The following assertions are equivalent: \smallskip \noindent{\em(i)} The functor $\BL_G$ is equivalence. \smallskip \noindent{\em(ii)} The fibers of the map $\pi^{\on{irred}}_\Ran$ are connected. \smallskip \noindent{\em(iii)} The fibers of the map $\pi^{…
```

---

<a id="glc4-conjecture-c-oper-contr-bf86b849"></a>
### Conjecture `c:oper contr`
- **Claim ID:** `GLC4:conjecture:c:oper contr`
- **Location:** `gaits4.tex` lines 3195-3197
- **Context:** The expression for \texorpdfstring{$\CA_{G,\on{irred}}$}{AGirred} via opers
- **Dependencies (outgoing):** 0 — _(none found by label-scan)_
- **Used by (incoming):** 3 — [`GLC4:remark:auto0043@L3199`](./GLC4.md#glc4-remark-auto0043-l3199-a733813e), [`GLC4:remark:auto0044@L3205`](./GLC4.md#glc4-remark-auto0044-l3205-87f49483), [`GLC4:remark:auto0046@L3226`](./GLC4.md#glc4-remark-auto0046-l3226-844357d4)

```tex
\label{c:oper contr} The space of \emph{generic oper structures} on a given irreducible local system is homologically contractible.
```

---

<a id="glc4-remark-auto0043-l3199-a733813e"></a>
### Remark `auto0043@L3199`
- **Claim ID:** `GLC4:remark:auto0043@L3199`
- **Location:** `gaits4.tex` lines 3199-3203
- **Context:** The expression for \texorpdfstring{$\CA_{G,\on{irred}}$}{AGirred} via opers
- **Dependencies (outgoing):** 1 — [`GLC4:conjecture:c:oper contr`](./GLC4.md#glc4-conjecture-c-oper-contr-bf86b849)
- **Used by (incoming):** 0 — _(none)_

```tex
Note that the ``bottom" layer of \conjref{c:oper contr} says that the space of generic oper structures on a given irreducible local system is \emph{non-empty}. This statement is actually a theorem, thanks to \cite{Ari}.
```

---

<a id="glc4-remark-auto0044-l3205-87f49483"></a>
### Remark `auto0044@L3205`
- **Claim ID:** `GLC4:remark:auto0044@L3205`
- **Location:** `gaits4.tex` lines 3205-3214
- **Context:** The expression for \texorpdfstring{$\CA_{G,\on{irred}}$}{AGirred} via opers
- **Dependencies (outgoing):** 1 — [`GLC4:conjecture:c:oper contr`](./GLC4.md#glc4-conjecture-c-oper-contr-bf86b849)
- **Used by (incoming):** 0 — _(none)_

- **Unresolved `\*ref{…}` targets (not claims):** 1

```tex
The assertion of \conjref{c:oper contr} is easy for $G=GL_n$. In particular, in this way we obtain another proof of GLC in this case (i.e., one that is logically different from that in \secref{ss:GLn})\footnote{The difference between the two arguments is that one uses a fully fai…
```

---

<a id="glc4-theorem-t-glc-for-class-aed40230"></a>
### Theorem `t:GLC for class`
- **Claim ID:** `GLC4:theorem:t:GLC for class`
- **Location:** `gaits4.tex` lines 3222-3224
- **Context:** The expression for \texorpdfstring{$\CA_{G,\on{irred}}$}{AGirred} via opers
- **Dependencies (outgoing):** 0 — _(none found by label-scan)_
- **Used by (incoming):** 0 — _(none)_

```tex
\label{t:GLC for class} The geometric Langlands conjecture holds when $G$ is a classical group.
```

---

<a id="glc4-remark-auto0046-l3226-844357d4"></a>
### Remark `auto0046@L3226`
- **Claim ID:** `GLC4:remark:auto0046@L3226`
- **Location:** `gaits4.tex` lines 3226-3237
- **Context:** The expression for \texorpdfstring{$\CA_{G,\on{irred}}$}{AGirred} via opers
- **Dependencies (outgoing):** 2 — [`GLC4:conjecture:c:oper contr`](./GLC4.md#glc4-conjecture-c-oper-contr-bf86b849), [`GLC4:theorem:t:BG via Op`](./GLC4.md#glc4-theorem-t-bg-via-op-e0ad90d6)
- **Used by (incoming):** 0 — _(none)_

- **Unresolved `\*ref{…}` targets (not claims):** 2

```tex
Formally speaking, the main theorem of \cite{BKS} establishes \conjref{c:oper contr} for a slightly different notion of oper, namely, for $\cg$-opers, rather than $\cG$-opers (and it is the latter that appears in \conjref{c:oper contr}). In other words, \cite{BKS} implies \conjre…
```

---

<a id="glc4-theorem-t-up-and-down-opers-48b5f333"></a>
### Theorem `t:up and down opers`
- **Claim ID:** `GLC4:theorem:t:up and down opers`
- **Location:** `gaits4.tex` lines 3271-3274
- **Context:** The expression for \texorpdfstring{$\CA_{G,\on{irred}}$}{AGirred} via opers
- **Dependencies (outgoing):** 1 — [`GLC4:theorem:t:BG via Op`](./GLC4.md#glc4-theorem-t-bg-via-op-e0ad90d6)
- **Used by (incoming):** 3 — [`GLC4:proposition:p:Ran emb`](./GLC4.md#glc4-proposition-p-ran-emb-f5c363d4), [`GLC4:remark:e:FCD quant`](./GLC4.md#glc4-remark-e-fcd-quant-46f0c8fb), [`GLC4:remark:r:coalg`](./GLC4.md#glc4-remark-r-coalg-3bef2d80)

- **Unresolved `\*ref{…}` targets (not claims):** 5

```tex
\label{t:up and down opers} The comonad on $\QCoh(\LS^{\on{irred}}_\cG)$ corresponding to \eqref{e:Poinc spec adj again} is given by tensor product with $\CB^{\Op}_{G,\on{irred}}$.
```

---

<a id="glc4-remark-r-coalg-3bef2d80"></a>
### Remark `r:coalg`
- **Claim ID:** `GLC4:remark:r:coalg`
- **Location:** `gaits4.tex` lines 3321-3354
- **Context:** The expression for \texorpdfstring{$\CA_{G,\on{irred}}$}{AGirred} via opers
- **Dependencies (outgoing):** 4 — [`GLC4:proposition:p:Ran emb`](./GLC4.md#glc4-proposition-p-ran-emb-f5c363d4), [`GLC4:proposition:p:dr to plain`](./GLC4.md#glc4-proposition-p-dr-to-plain-b1fa242a), [`GLC4:theorem:t:BG via Op`](./GLC4.md#glc4-theorem-t-bg-via-op-e0ad90d6), [`GLC4:theorem:t:up and down opers`](./GLC4.md#glc4-theorem-t-up-and-down-opers-48b5f333)
- **Used by (incoming):** 1 — [`GLC4:remark:auto0034@L2986`](./GLC4.md#glc4-remark-auto0034-l2986-ada84eb4)

- **Unresolved `\*ref{…}` targets (not claims):** 1

```tex
\label{r:coalg} Note that \thmref{t:BG via Op} only says that $\CB_{G,\on{irred}}$ and $\CB^{\Op}_{G,\on{irred}}$ are isomorphic as objects of $\QCoh(\LS^{\on{irred}}_\cG)$, but not as co-associative co-algebras. One can upgrade the proof given above to an isomorphism of coalgebr…
```

---


## Proof of \thmref{t:up and down opers}

<a id="glc4-proposition-p-dr-to-plain-b1fa242a"></a>
### Proposition `p:dr to plain`
- **Claim ID:** `GLC4:proposition:p:dr to plain`
- **Location:** `gaits4.tex` lines 3386-3390
- **Context:** Proof of \thmref{t:up and down opers}
- **Dependencies (outgoing):** 0 — _(none found by label-scan)_
- **Used by (incoming):** 4 — [`GLC4:proposition:p:Ran emb`](./GLC4.md#glc4-proposition-p-ran-emb-f5c363d4), [`GLC4:remark:auto0050@L3392`](./GLC4.md#glc4-remark-auto0050-l3392-a424ecd0), [`GLC4:remark:r:QCoh* as a sheaf of cats`](./GLC4.md#glc4-remark-r-qcoh-as-a-sheaf-of-cats-d4d00a13), [`GLC4:remark:r:coalg`](./GLC4.md#glc4-remark-r-coalg-3bef2d80)

- **Unresolved `\*ref{…}` targets (not claims):** 1

```tex
\label{p:dr to plain} The natural transformation \eqref{e:dr to plain} is an isomorphism when evaluated on objects in the essential image of the functor $$\pi^!_\Ran:\Dmod(\LS_\cG)\to \Dmod(\Op^{\on{mon-free}}_\cG(X^{\on{gen}})_\Ran).$$
```

---

<a id="glc4-remark-auto0050-l3392-a424ecd0"></a>
### Remark `auto0050@L3392`
- **Claim ID:** `GLC4:remark:auto0050@L3392`
- **Location:** `gaits4.tex` lines 3392-3395
- **Context:** Proof of \thmref{t:up and down opers}
- **Dependencies (outgoing):** 1 — [`GLC4:proposition:p:dr to plain`](./GLC4.md#glc4-proposition-p-dr-to-plain-b1fa242a)
- **Used by (incoming):** 0 — _(none)_

```tex
For the validity of \propref{p:dr to plain}, it is essential that we work with the entire $\Ran$ and not a fixed $\ul{x}\in \Ran$.
```

---

<a id="glc4-proposition-p-ran-emb-f5c363d4"></a>
### Proposition `p:Ran emb`
- **Claim ID:** `GLC4:proposition:p:Ran emb`
- **Location:** `gaits4.tex` lines 3412-3418
- **Context:** Proof of \thmref{t:up and down opers}
- **Dependencies (outgoing):** 2 — [`GLC4:proposition:p:dr to plain`](./GLC4.md#glc4-proposition-p-dr-to-plain-b1fa242a), [`GLC4:theorem:t:up and down opers`](./GLC4.md#glc4-theorem-t-up-and-down-opers-48b5f333)
- **Used by (incoming):** 5 — [`GLC4:proposition:p:Ran emb abs abs`](./GLC4.md#glc4-proposition-p-ran-emb-abs-abs-07bea58f), [`GLC4:proposition:p:Ran emb abs rel`](./GLC4.md#glc4-proposition-p-ran-emb-abs-rel-9400f7ef), [`GLC4:proposition:p:ind oblv YZ`](./GLC4.md#glc4-proposition-p-ind-oblv-yz-a4cd0be2), [`GLC4:remark:r:QCoh* as a sheaf of cats`](./GLC4.md#glc4-remark-r-qcoh-as-a-sheaf-of-cats-d4d00a13), [`GLC4:remark:r:coalg`](./GLC4.md#glc4-remark-r-coalg-3bef2d80)

- **Unresolved `\*ref{…}` targets (not claims):** 3

```tex
\label{p:Ran emb} The natural transformation \eqref{e:Ran emb}, composed with the coarsening functor $$\Psi_{\LS_\cG}:\IndCoh(\LS_\cG)\to \QCoh(\LS_\cG),$$ is an isomorphism, when evaluated on objects in the essential image of the functor $$\pi^!_\Ran:\IndCoh(\LS_\cG)\to \IndCoh(…
```

---

<a id="glc4-proposition-p-dr-to-plain-rel-36991980"></a>
### Proposition `p:dr to plain rel`
- **Claim ID:** `GLC4:proposition:p:dr to plain rel`
- **Location:** `gaits4.tex` lines 3527-3530
- **Context:** Proof of \thmref{t:up and down opers}
- **Dependencies (outgoing):** 0 — _(none found by label-scan)_
- **Used by (incoming):** 0 — _(none)_

- **Unresolved `\*ref{…}` targets (not claims):** 2

```tex
\label{p:dr to plain rel} The natural transformation \eqref{e:dr to plain rel} is an isomorphism when evaluated on objects in the essential image of the functor \eqref{e:pullback to rel}.
```

---

<a id="glc4-proposition-p-ind-oblv-op-a4f0f2e0"></a>
### Proposition `p:ind oblv Op`
- **Claim ID:** `GLC4:proposition:p:ind oblv Op`
- **Location:** `gaits4.tex` lines 3534-3538
- **Context:** Proof of \thmref{t:up and down opers}
- **Dependencies (outgoing):** 0 — _(none found by label-scan)_
- **Used by (incoming):** 1 — [`GLC4:proposition:p:ind oblv YZ`](./GLC4.md#glc4-proposition-p-ind-oblv-yz-a4cd0be2)

- **Unresolved `\*ref{…}` targets (not claims):** 1

```tex
\label{p:ind oblv Op} The counit of the adjunction $$\ind^{\on{rel}}\circ \oblv^{\on{rel}}\to \on{Id}$$ is an isomorphism, when evaluated on objects in the essential image of the functor \eqref{e:pullback to rel}.
```

---

<a id="glc4-proposition-p-ind-oblv-yz-a4cd0be2"></a>
### Proposition `p:ind oblv YZ`
- **Claim ID:** `GLC4:proposition:p:ind oblv YZ`
- **Location:** `gaits4.tex` lines 3619-3624
- **Context:** Proof of \thmref{t:up and down opers}
- **Dependencies (outgoing):** 2 — [`GLC4:proposition:p:Ran emb`](./GLC4.md#glc4-proposition-p-ran-emb-f5c363d4), [`GLC4:proposition:p:ind oblv Op`](./GLC4.md#glc4-proposition-p-ind-oblv-op-a4f0f2e0)
- **Used by (incoming):** 2 — [`GLC4:lemma:l:str reflects`](./GLC4.md#glc4-lemma-l-str-reflects-9ab47eee), [`GLC4:proposition:p:Ran emb abs rel`](./GLC4.md#glc4-proposition-p-ran-emb-abs-rel-9400f7ef)

- **Unresolved `\*ref{…}` targets (not claims):** 1

```tex
\label{p:ind oblv YZ} The counit of the adjunction $$\ind^{\on{rel}}\circ \oblv^{\on{rel}}\to \on{Id}$$ is an isomorphism, when evaluated on objects in the essential image of the pullback functor $$(\pi_{\Ran,\dR^{\on{rel}}})^!:\IndCoh(\on{Sect}_\nabla(X,\CY))\to \IndCoh\left(\le…
```

---

<a id="glc4-remark-auto0055-l3672-9d32b280"></a>
### Remark `auto0055@L3672`
- **Claim ID:** `GLC4:remark:auto0055@L3672`
- **Location:** `gaits4.tex` lines 3672-3682
- **Context:** Proof of \thmref{t:up and down opers}
- **Dependencies (outgoing):** 0 — _(none found by label-scan)_
- **Used by (incoming):** 0 — _(none)_

- **Unresolved `\*ref{…}` targets (not claims):** 1

```tex
We do not know whether $\QCoh_{\on{co}}(\CW)$ is dualizable. However, $\QCoh_{\on{co}}(\CW)$ is tautologically the pre-dual of $\on{QCoh}(\CW)$, i.e., $$\on{QCoh}(\CW)\simeq \on{Funct}(\QCoh_{\on{co}}(\CW),\Vect),$$ where $\on{Funct}(-,-)$ is the category of colimit-preserving fu…
```

---

<a id="glc4-remark-r-qcoh-as-a-sheaf-of-cats-d4d00a13"></a>
### Remark `r:QCoh* as a sheaf of cats`
- **Claim ID:** `GLC4:remark:r:QCoh* as a sheaf of cats`
- **Location:** `gaits4.tex` lines 3772-3791
- **Context:** Proof of \thmref{t:up and down opers}
- **Dependencies (outgoing):** 2 — [`GLC4:proposition:p:Ran emb`](./GLC4.md#glc4-proposition-p-ran-emb-f5c363d4), [`GLC4:proposition:p:dr to plain`](./GLC4.md#glc4-proposition-p-dr-to-plain-b1fa242a)
- **Used by (incoming):** 0 — _(none)_

- **Unresolved `\*ref{…}` targets (not claims):** 7

```tex
\label{r:QCoh* as a sheaf of cats} The assignment $$S\rightsquigarrow \QCoh_{\on{co}}(\CW_\Ran\underset{\Ran}\times S)$$ naturally forms a sheaf of categories over $\Ran$, to be denoted $$\ul{\QCoh_{\on{co}}}(\CW)_\Ran.$$ The above definition of $\QCoh_{\on{co}}(\CW)_\Ran$ is a p…
```

---

<a id="glc4-proposition-p-ran-emb-abs-abs-07bea58f"></a>
### Proposition `p:Ran emb abs abs`
- **Claim ID:** `GLC4:proposition:p:Ran emb abs abs`
- **Location:** `gaits4.tex` lines 3927-3933
- **Context:** Proof of \thmref{t:up and down opers}
- **Dependencies (outgoing):** 1 — [`GLC4:proposition:p:Ran emb`](./GLC4.md#glc4-proposition-p-ran-emb-f5c363d4)
- **Used by (incoming):** 3 — [`GLC4:lemma:l:cofinal initial`](./GLC4.md#glc4-lemma-l-cofinal-initial-c82e0214), [`GLC4:proposition:p:Ran emb unital`](./GLC4.md#glc4-proposition-p-ran-emb-unital-5d7c115a), [`GLC4:proposition:p:diag cofinal`](./GLC4.md#glc4-proposition-p-diag-cofinal-4ba985e2)

- **Unresolved `\*ref{…}` targets (not claims):** 5

```tex
\label{p:Ran emb abs abs} The natural transformation $$\Gamma^{\IndCoh_\Ran}(\Sectna(X^{\on{gen}},\CZ)_\Ran,-)\circ (s_{\CZ,\Ran})^*\circ (s_{\CZ,\Ran})_*\to \Gamma^{\IndCoh_\Ran}(\Sectna(X^{\on{gen}},\CZ)_\Ran,-)$$ is an isomorphism, when evaluated on the image of $\omega_{\Sect…
```

---

<a id="glc4-remark-r-apply-paradigm-9fde8c72"></a>
### Remark `r:apply paradigm`
- **Claim ID:** `GLC4:remark:r:apply paradigm`
- **Location:** `gaits4.tex` lines 4038-4044
- **Context:** Proof of \thmref{t:up and down opers}
- **Dependencies (outgoing):** 0 — _(none found by label-scan)_
- **Used by (incoming):** 1 — [`GLC4:proposition:p:Ran emb abs rel`](./GLC4.md#glc4-proposition-p-ran-emb-abs-rel-9400f7ef)

```tex
\label{r:apply paradigm} For our applications, we will take $\CZ=\Op_\cG$ and $\CY=\on{pt}/\cG$ and $\CT:=\Op^{\on{mon-free}}_\cG$. In this case $\on{Sect}_\nabla(X,\CY)=\LS_\cG$, and $\CZ_{\on{Sect}_\nabla(X,\CY)}$ is the D-scheme parameterized by $\LS_\cG$ that classifies oper…
```

---

<a id="glc4-proposition-p-ran-emb-abs-rel-9400f7ef"></a>
### Proposition `p:Ran emb abs rel`
- **Claim ID:** `GLC4:proposition:p:Ran emb abs rel`
- **Location:** `gaits4.tex` lines 4056-4066
- **Context:** Proof of \thmref{t:up and down opers}
- **Dependencies (outgoing):** 3 — [`GLC4:proposition:p:Ran emb`](./GLC4.md#glc4-proposition-p-ran-emb-f5c363d4), [`GLC4:proposition:p:ind oblv YZ`](./GLC4.md#glc4-proposition-p-ind-oblv-yz-a4cd0be2), [`GLC4:remark:r:apply paradigm`](./GLC4.md#glc4-remark-r-apply-paradigm-9fde8c72)
- **Used by (incoming):** 2 — [`GLC4:proposition:p:diag cofinal`](./GLC4.md#glc4-proposition-p-diag-cofinal-4ba985e2), [`GLC4:remark:auto0076@L5873`](./GLC4.md#glc4-remark-auto0076-l5873-f2a84da9)

- **Unresolved `\*ref{…}` targets (not claims):** 5

```tex
\label{p:Ran emb abs rel} The natural transformation $$(\pi_\Ran)^{\IndCoh_\Ran}_*\circ (s_{\CT,\Ran})^*\circ (s_{\CT,\Ran})_*\to (\pi_\Ran)^{\IndCoh_\Ran}_*$$ is an isomorphism, when evaluated on objects that lie in the essential image of the functor \begin{multline} \label{e:Ra…
```

---


## Proof of \propref{p:ind oblv YZ}

<a id="glc4-lemma-l-str-reflects-9ab47eee"></a>
### Lemma `l:str reflects`
- **Claim ID:** `GLC4:lemma:l:str reflects`
- **Location:** `gaits4.tex` lines 4253-4262
- **Context:** Proof of \propref{p:ind oblv YZ}
- **Dependencies (outgoing):** 1 — [`GLC4:proposition:p:ind oblv YZ`](./GLC4.md#glc4-proposition-p-ind-oblv-yz-a4cd0be2)
- **Used by (incoming):** 1 — [`GLC4:lemma:l:cofinal`](./GLC4.md#glc4-lemma-l-cofinal-d5106ef5)

```tex
\label{l:str reflects} The natural diagram of categories $$ \xymatrix{ \IndCoh(\CX_{\dr})_{\on{str}} \ar[r]\ar[d] & \IndCoh(\CX)_{\on{str}} \ar[d]\\ \IndCoh(\CX_{\dr}) \ar[r] & \IndCoh(\CX) } $$ is a pullback square.
```

---

<a id="glc4-proposition-p-ind-oblv-untl-d46b2499"></a>
### Proposition `p:ind oblv untl`
- **Claim ID:** `GLC4:proposition:p:ind oblv untl`
- **Location:** `gaits4.tex` lines 4301-4307
- **Context:** Proof of \propref{p:ind oblv YZ}
- **Dependencies (outgoing):** 0 — _(none found by label-scan)_
- **Used by (incoming):** 0 — _(none)_

- **Unresolved `\*ref{…}` targets (not claims):** 3

```tex
\label{p:ind oblv untl} The counit of the adjunction $$\ind^{\on{rel}}\circ \oblv^{\on{rel}}\to \on{Id}$$ is an isomorphism, when evaluated on objects in the essential image along $\sft^!$ of $$\IndCoh\left(\left(\on{Sect}_\nabla(X^{\on{gen}},\CZ/\CY)_\Ranu\right)_{\dr^{\on{rel}}…
```

---

<a id="glc4-proposition-p-conn-autom-6e83eaa6"></a>
### Proposition `p:conn autom`
- **Claim ID:** `GLC4:proposition:p:conn autom`
- **Location:** `gaits4.tex` lines 4367-4372
- **Context:** Proof of \propref{p:ind oblv YZ}
- **Dependencies (outgoing):** 0 — _(none found by label-scan)_
- **Used by (incoming):** 3 — [`GLC4:lemma:l:cofinal`](./GLC4.md#glc4-lemma-l-cofinal-d5106ef5), [`GLC4:lemma:l:cofinal initial`](./GLC4.md#glc4-lemma-l-cofinal-initial-c82e0214), [`GLC4:theorem:t:Nick fam`](./GLC4.md#glc4-theorem-t-nick-fam-a05547c9)

- **Unresolved `\*ref{…}` targets (not claims):** 2

```tex
\label{p:conn autom} The functor $$\oblv^{\on{rel}}_{\on{untl,str}}: \left(\IndCoh\left((\on{Sect}_\nabla(X^{\on{gen}},\CZ/\CY)_\Ranu)_{\dr^{\on{rel}}}\right)\right)_{\on{str}}\to \left(\IndCoh\left(\on{Sect}_\nabla(X^{\on{gen}},\CZ/\CY)_\Ranu\right)\right)_{\on{str}}$$ is an equ…
```

---

<a id="glc4-theorem-t-nick-x-b96734f1"></a>
### Theorem `t:Nick x`
- **Claim ID:** `GLC4:theorem:t:Nick x`
- **Location:** `gaits4.tex` lines 4444-4453
- **Context:** Proof of \propref{p:ind oblv YZ}
- **Dependencies (outgoing):** 0 — _(none found by label-scan)_
- **Used by (incoming):** 2 — [`GLC4:lemma:l:cofinal initial`](./GLC4.md#glc4-lemma-l-cofinal-initial-c82e0214), [`GLC4:remark:auto0064@L4455`](./GLC4.md#glc4-remark-auto0064-l4455-c39353b7)

- **Unresolved `\*ref{…}` targets (not claims):** 1

```tex
\label{t:Nick x} The functor \begin{multline*} \IndCoh\left(\on{Sect}_\nabla(X-\ul{x},\CZ/\CY)_{\dr^{\on{rel}}}\right)\to \\ \to \IndCoh\left(\on{Sect}_\nabla(X-\ul{x},\CZ/\CY)\right)\underset{\IndCoh\left(\on{Sect}_\nabla(X-\ul{x},\CZ/\CY)\times \Ranu\right)}\times \IndCoh\left(…
```

---

<a id="glc4-remark-auto0064-l4455-c39353b7"></a>
### Remark `auto0064@L4455`
- **Claim ID:** `GLC4:remark:auto0064@L4455`
- **Location:** `gaits4.tex` lines 4455-4458
- **Context:** Proof of \propref{p:ind oblv YZ}
- **Dependencies (outgoing):** 1 — [`GLC4:theorem:t:Nick x`](./GLC4.md#glc4-theorem-t-nick-x-b96734f1)
- **Used by (incoming):** 0 — _(none)_

- **Unresolved `\*ref{…}` targets (not claims):** 1

```tex
In fact, this theorem is a particular case of \cite[Corollary 4.6.10]{Ro}: replace the original $\CZ$ by its restriction of scalars along $X-\ul{x}\to X$.
```

---

<a id="glc4-theorem-t-nick-fam-a05547c9"></a>
### Theorem `t:Nick fam`
- **Claim ID:** `GLC4:theorem:t:Nick fam`
- **Location:** `gaits4.tex` lines 4502-4514
- **Context:** Proof of \propref{p:ind oblv YZ}
- **Dependencies (outgoing):** 1 — [`GLC4:proposition:p:conn autom`](./GLC4.md#glc4-proposition-p-conn-autom-6e83eaa6)
- **Used by (incoming):** 2 — [`GLC4:lemma:l:cofinal`](./GLC4.md#glc4-lemma-l-cofinal-d5106ef5), [`GLC4:lemma:l:cofinal initial`](./GLC4.md#glc4-lemma-l-cofinal-initial-c82e0214)

- **Unresolved `\*ref{…}` targets (not claims):** 3

```tex
\label{t:Nick fam} The functor \begin{multline} \label{e:Nick fam} \IndCoh\left((\on{Sect}_\nabla(X^{\on{gen}},\CZ/\CY)_\Ranu)_{\dr^{\on{rel}}}\right) \to \\ \to \IndCoh\left(\on{Sect}_\nabla(X^{\on{gen}},\CZ/\CY)_\Ranu\right) \underset{\IndCoh\left(\on{Sect}_\nabla(X^{\on{gen}},…
```

---

<a id="glc4-lemma-l-cofinal-d5106ef5"></a>
### Lemma `l:cofinal`
- **Claim ID:** `GLC4:lemma:l:cofinal`
- **Location:** `gaits4.tex` lines 4538-4542
- **Context:** Proof of \propref{p:ind oblv YZ}
- **Dependencies (outgoing):** 3 — [`GLC4:lemma:l:str reflects`](./GLC4.md#glc4-lemma-l-str-reflects-9ab47eee), [`GLC4:proposition:p:conn autom`](./GLC4.md#glc4-proposition-p-conn-autom-6e83eaa6), [`GLC4:theorem:t:Nick fam`](./GLC4.md#glc4-theorem-t-nick-fam-a05547c9)
- **Used by (incoming):** 1 — [`GLC4:lemma:l:cofinal initial`](./GLC4.md#glc4-lemma-l-cofinal-initial-c82e0214)

- **Unresolved `\*ref{…}` targets (not claims):** 2

```tex
\label{l:cofinal} The functor $$\IndCoh\left(\on{Sect}_\nabla(X^{\on{gen}},\CZ/\CY)^\wedge_{\on{add}}\right)_{\on{str}}\to \IndCoh\left(\on{Sect}_\nabla(X^{\on{gen}},\CZ/\CY)_{\on{pr}_1}\right)_{\on{str}}$$ is an equivalence.
```

---

<a id="glc4-lemma-l-cofinal-initial-c82e0214"></a>
### Lemma `l:cofinal initial`
- **Claim ID:** `GLC4:lemma:l:cofinal initial`
- **Location:** `gaits4.tex` lines 4586-4592
- **Context:** Proof of \propref{p:ind oblv YZ}
- **Dependencies (outgoing):** 5 — [`GLC4:lemma:l:cofinal`](./GLC4.md#glc4-lemma-l-cofinal-d5106ef5), [`GLC4:proposition:p:Ran emb abs abs`](./GLC4.md#glc4-proposition-p-ran-emb-abs-abs-07bea58f), [`GLC4:proposition:p:conn autom`](./GLC4.md#glc4-proposition-p-conn-autom-6e83eaa6), [`GLC4:theorem:t:Nick fam`](./GLC4.md#glc4-theorem-t-nick-fam-a05547c9), [`GLC4:theorem:t:Nick x`](./GLC4.md#glc4-theorem-t-nick-x-b96734f1)
- **Used by (incoming):** 0 — _(none)_

- **Unresolved `\*ref{…}` targets (not claims):** 16

```tex
\label{l:cofinal initial} Let $\CW\to \Ranu\times \Ranu$ be a map of categorical prestacks, which is a value-wise co-Cartesian fibration. Then then the induced map $$\CW\underset{\Ranu\times \Ranu,\Delta}\times \Ranu\to \CW$$ induces an isomorphism $$\left(\CW\underset{\Ranu\time…
```

---


## Proof of \propref{p:Ran emb abs abs}

<a id="glc4-proposition-p-ran-emb-unital-5d7c115a"></a>
### Proposition `p:Ran emb unital`
- **Claim ID:** `GLC4:proposition:p:Ran emb unital`
- **Location:** `gaits4.tex` lines 5007-5012
- **Context:** Proof of \propref{p:Ran emb abs abs}
- **Dependencies (outgoing):** 1 — [`GLC4:proposition:p:Ran emb abs abs`](./GLC4.md#glc4-proposition-p-ran-emb-abs-abs-07bea58f)
- **Used by (incoming):** 1 — [`GLC4:proposition:p:Ran emb unital local`](./GLC4.md#glc4-proposition-p-ran-emb-unital-local-fe0fb232)

- **Unresolved `\*ref{…}` targets (not claims):** 9

```tex
\label{p:Ran emb unital} The natural transformation $$\Gamma^{\IndCoh_\Ran}(\Sectna(X^{\on{gen}},\CZ)_\Ran,-)\circ (s_{\CZ,\Ran})^*\circ (s_{\CZ,\Ran})_*\to \Gamma^{\IndCoh_\Ran}(\Sectna(X^{\on{gen}},\CZ)_\Ran,-)$$ is an isomorphism, when evaluated on the essential image of the f…
```

---

<a id="glc4-proposition-p-ran-emb-unital-local-fe0fb232"></a>
### Proposition `p:Ran emb unital local`
- **Claim ID:** `GLC4:proposition:p:Ran emb unital local`
- **Location:** `gaits4.tex` lines 5139-5149
- **Context:** Proof of \propref{p:Ran emb abs abs}
- **Dependencies (outgoing):** 1 — [`GLC4:proposition:p:Ran emb unital`](./GLC4.md#glc4-proposition-p-ran-emb-unital-5d7c115a)
- **Used by (incoming):** 4 — [`GLC4:lemma:l:inherit`](./GLC4.md#glc4-lemma-l-inherit-0d6dcdb9), [`GLC4:proposition:p:diag cofinal`](./GLC4.md#glc4-proposition-p-diag-cofinal-4ba985e2), [`GLC4:proposition:p:fact hom`](./GLC4.md#glc4-proposition-p-fact-hom-e741c7f6), [`GLC4:remark:auto0076@L5873`](./GLC4.md#glc4-remark-auto0076-l5873-f2a84da9)

- **Unresolved `\*ref{…}` targets (not claims):** 5

```tex
\label{p:Ran emb unital local} The natural transformation \begin{multline*} \Gamma^{\IndCoh_\Ran}(\fL_\nabla(\CZ)_\Ran,-) \to \Gamma^{\IndCoh_\Ran}(\fL_\nabla(\CZ)_\Ran,-) \circ (s_{\CZ,\Ran})_* \circ (s_{\CZ,\Ran})^* \simeq \\ \simeq \Gamma^{\IndCoh_\Ran}(\Sectna(X^{\on{gen}},\C…
```

---

<a id="glc4-proposition-p-fact-hom-e741c7f6"></a>
### Proposition `p:fact hom`
- **Claim ID:** `GLC4:proposition:p:fact hom`
- **Location:** `gaits4.tex` lines 5357-5400
- **Context:** Proof of \propref{p:Ran emb abs abs}
- **Dependencies (outgoing):** 1 — [`GLC4:proposition:p:Ran emb unital local`](./GLC4.md#glc4-proposition-p-ran-emb-unital-local-fe0fb232)
- **Used by (incoming):** 2 — [`GLC4:lemma:l:inherit`](./GLC4.md#glc4-lemma-l-inherit-0d6dcdb9), [`GLC4:remark:auto0076@L5873`](./GLC4.md#glc4-remark-auto0076-l5873-f2a84da9)

- **Unresolved `\*ref{…}` targets (not claims):** 5

```tex
\label{p:fact hom} \hfill \smallskip \noindent{\em(a)} The functor $$\QCoh(\fL^+_\nabla(\CZ))_\Ran \overset{(s_{\CZ,\Ran})^*}\longrightarrow \QCoh(\Sectna(X,\CZ))\otimes \IndCoh(\Ran) \overset{\Gamma(\Sectna(X,\CZ),-)\otimes \on{Id}}\longrightarrow \IndCoh(\Ran)$$ identifies cano…
```

---

<a id="glc4-lemma-l-inherit-0d6dcdb9"></a>
### Lemma `l:inherit`
- **Claim ID:** `GLC4:lemma:l:inherit`
- **Location:** `gaits4.tex` lines 5562-5571
- **Context:** Proof of \propref{p:Ran emb abs abs}
- **Dependencies (outgoing):** 2 — [`GLC4:proposition:p:Ran emb unital local`](./GLC4.md#glc4-proposition-p-ran-emb-unital-local-fe0fb232), [`GLC4:proposition:p:fact hom`](./GLC4.md#glc4-proposition-p-fact-hom-e741c7f6)
- **Used by (incoming):** 0 — _(none)_

- **Unresolved `\*ref{…}` targets (not claims):** 1

```tex
\label{l:inherit} The composite functor \begin{multline*} \QCoh_{\on{co}}(\fL_\nabla(\CZ))_\Ranu\overset{\sft^!}\to \QCoh_{\on{co}}(\fL_\nabla(\CZ))_\Ran \overset{\on{ins.unit}}\longrightarrow \\ \to \QCoh_{\on{co}}(\fL_\nabla(\CZ))_{\Ran^{\subseteq},\on{big}} \overset{(p_{\fL^+_…
```

---

<a id="glc4-proposition-p-diag-cofinal-4ba985e2"></a>
### Proposition `p:diag cofinal`
- **Claim ID:** `GLC4:proposition:p:diag cofinal`
- **Location:** `gaits4.tex` lines 5597-5606
- **Context:** Proof of \propref{p:Ran emb abs abs}
- **Dependencies (outgoing):** 3 — [`GLC4:proposition:p:Ran emb abs abs`](./GLC4.md#glc4-proposition-p-ran-emb-abs-abs-07bea58f), [`GLC4:proposition:p:Ran emb abs rel`](./GLC4.md#glc4-proposition-p-ran-emb-abs-rel-9400f7ef), [`GLC4:proposition:p:Ran emb unital local`](./GLC4.md#glc4-proposition-p-ran-emb-unital-local-fe0fb232)
- **Used by (incoming):** 0 — _(none)_

- **Unresolved `\*ref{…}` targets (not claims):** 6

```tex
\label{p:diag cofinal} The natural transformation \begin{multline*} \Gamma^{\IndCoh}(\Ran,-)\circ \on{diag}^! \simeq \Gamma^{\IndCoh}(\Ran,-)\circ (\on{pr}_{\on{small}})_*\circ \on{diag}_* \circ \on{diag}^! \to \\ \to \Gamma^{\IndCoh}(\Ran,-)\circ (\on{pr}_{\on{small}})_*\simeq \…
```

---


## Proof of \propref{p:Ran emb abs rel}

<a id="glc4-proposition-p-loc-unital-c7c052e4"></a>
### Proposition `p:loc unital`
- **Claim ID:** `GLC4:proposition:p:loc unital`
- **Location:** `gaits4.tex` lines 5824-5832
- **Context:** Proof of \propref{p:Ran emb abs rel}
- **Dependencies (outgoing):** 0 — _(none found by label-scan)_
- **Used by (incoming):** 1 — [`GLC4:remark:auto0076@L5873`](./GLC4.md#glc4-remark-auto0076-l5873-f2a84da9)

- **Unresolved `\*ref{…}` targets (not claims):** 2

```tex
\label{p:loc unital} Let $\CY$ be a D-prestack with an affine diagonal, satisfying the finiteness assumptions of \secref{sss:good D stacks} above. Then the natural transformation $$\Loc_\CY\circ (s_{\CY,\Ran})_*\simeq (\on{Id}\otimes \Gamma^{\IndCoh}(\Ran,-))\circ (s_{\CY,\Ran})^…
```

---

<a id="glc4-proposition-p-loc-unital-fund-659c1067"></a>
### Proposition `p:loc unital fund`
- **Claim ID:** `GLC4:proposition:p:loc unital fund`
- **Location:** `gaits4.tex` lines 5843-5848
- **Context:** Proof of \propref{p:Ran emb abs rel}
- **Dependencies (outgoing):** 0 — _(none found by label-scan)_
- **Used by (incoming):** 2 — [`GLC4:corollary:c:fact hom rel`](./GLC4.md#glc4-corollary-c-fact-hom-rel-5d74a5a3), [`GLC4:remark:auto0076@L5873`](./GLC4.md#glc4-remark-auto0076-l5873-f2a84da9)

- **Unresolved `\*ref{…}` targets (not claims):** 1

```tex
\label{p:loc unital fund} Let $\CY$ be a D-prestack with an affine diagonal, satisfying the finiteness assumptions of \secref{sss:good D stacks} above. Then the counit of the adjunction $$\Loc_\CY\circ \Loc^R_\CY \to \on{Id},$$ is an isomorphism.
```

---

<a id="glc4-corollary-c-loc-unital-bis-f5615e0f"></a>
### Corollary `c:loc unital bis`
- **Claim ID:** `GLC4:corollary:c:loc unital bis`
- **Location:** `gaits4.tex` lines 5852-5856
- **Context:** Proof of \propref{p:Ran emb abs rel}
- **Dependencies (outgoing):** 1 — [`GLC4:proposition:p:Gamma ff`](./GLC4.md#glc4-proposition-p-gamma-ff-64870d2e)
- **Used by (incoming):** 0 — _(none)_

```tex
\label{c:loc unital bis} Under the above assumptions on $\CY$, the functor $$\Loc^R_\CY:\QCoh(\on{Sect}(X,\CY))\to \QCoh(\CY)_\Ran$$ is fully faithful.
```

---

<a id="glc4-remark-auto0076-l5873-f2a84da9"></a>
### Remark `auto0076@L5873`
- **Claim ID:** `GLC4:remark:auto0076@L5873`
- **Location:** `gaits4.tex` lines 5873-5876
- **Context:** Proof of \propref{p:Ran emb abs rel}
- **Dependencies (outgoing):** 5 — [`GLC4:proposition:p:Ran emb abs rel`](./GLC4.md#glc4-proposition-p-ran-emb-abs-rel-9400f7ef), [`GLC4:proposition:p:Ran emb unital local`](./GLC4.md#glc4-proposition-p-ran-emb-unital-local-fe0fb232), [`GLC4:proposition:p:fact hom`](./GLC4.md#glc4-proposition-p-fact-hom-e741c7f6), [`GLC4:proposition:p:loc unital`](./GLC4.md#glc4-proposition-p-loc-unital-c7c052e4), [`GLC4:proposition:p:loc unital fund`](./GLC4.md#glc4-proposition-p-loc-unital-fund-659c1067)
- **Used by (incoming):** 0 — _(none)_

- **Unresolved `\*ref{…}` targets (not claims):** 10

```tex
As far as the actual proof of \propref{p:loc unital} is concerned, we will first establish \propref{p:loc unital fund}, and then deduce the general case stated in \propref{p:loc unital}.
```

---

<a id="glc4-proposition-p-fact-hom-rel-e6786271"></a>
### Proposition `p:fact hom rel`
- **Claim ID:** `GLC4:proposition:p:fact hom rel`
- **Location:** `gaits4.tex` lines 6182-6186
- **Context:** Proof of \propref{p:Ran emb abs rel}
- **Dependencies (outgoing):** 0 — _(none found by label-scan)_
- **Used by (incoming):** 0 — _(none)_

- **Unresolved `\*ref{…}` targets (not claims):** 1

```tex
\label{p:fact hom rel} The natural transformation \eqref{e:chir hom nat transf rel} is an isomorphism, when evaluated on objects lying in the essential image of the forgetful functor $$\sft^!:\QCoh(\CZ_1)_\Ranu\to \QCoh(\CZ_1)_\Ran.$$
```

---

<a id="glc4-corollary-c-fact-hom-rel-5d74a5a3"></a>
### Corollary `c:fact hom rel`
- **Claim ID:** `GLC4:corollary:c:fact hom rel`
- **Location:** `gaits4.tex` lines 6188-6191
- **Context:** Proof of \propref{p:Ran emb abs rel}
- **Dependencies (outgoing):** 1 — [`GLC4:proposition:p:loc unital fund`](./GLC4.md#glc4-proposition-p-loc-unital-fund-659c1067)
- **Used by (incoming):** 0 — _(none)_

- **Unresolved `\*ref{…}` targets (not claims):** 2

```tex
\label{c:fact hom rel} The natural transformation \eqref{e:chir hom nat transf rel} is an isomorphism, when evaluated on the object $$(p_{\CZ_{1,\Ran}})^*(\omega_\Ran)\in \QCoh(\CZ_1)_\Ran.$$
```

---

