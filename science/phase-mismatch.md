# Phase mismatch and reference disturbance

The receiver is calibrated for a common phase. This section quantifies its response when the reference still has orientation $`\phi`$ but all $`k`$ signal copies acquire a common relative phase offset $`\delta`$. In the two-copy case we also give the response to unequal offsets.

## Impossibility of unambiguous readout over an interval

Fix the reference orientation and a phase offset interval with nonempty interior. The $`k`$-copy signals with sign $`s\in\{+1,-1\}`$ have the Dicke-basis expansion

```math
|\psi_{s,\delta}\rangle
=\sum_{j=0}^{k} \sqrt{B_j}\,s^j e^{\mathrm{i}j(\phi+\delta)}|D_j^{(k)}\rangle,
\qquad B_j=2^{-k}\binom{k}{j}.
```

Choose any $`k+1`$ offsets in the interval whose complex exponentials are distinct. The matrix of their coefficient vectors is a Vandermonde matrix times an invertible diagonal matrix. For either sign the vectors span the full symmetric $`k`$-qubit subspace. Tensoring each vector with the same reference preserves this equality of spans. A positive conclusive effect for either label must annihilate every vector from the other sign to have zero wrong-label probability throughout the interval. It therefore annihilates the entire shared span. Both conclusive probabilities vanish. This argument applies even if the reference may be discarded or the measurement may break charge covariance.

A single known offset can be corrected by a charge-diagonal phase shift on each signal. An unknown fixed offset is the mismatch considered below.

## Exact response of the calibrated receiver

Write the reference weights as $`w_i=|c_i|^2`$ and extend them by zero outside the ladder. For each total charge $`q`$, the even and odd signal-charge weights are

```math
e_q=\sum_{j\ \mathrm{even}} B_j w_{q-j},
\qquad
o_q=\sum_{j\ \mathrm{odd}} B_j w_{q-j}.
```

Define their normalized phase responses on active sectors by

```math
A_q(\delta)=\frac{\sum_{j\ \mathrm{even}} B_j w_{q-j}e^{\mathrm{i}j\delta}}{e_q},
\qquad
C_q(\delta)=\frac{\sum_{j\ \mathrm{odd}} B_j w_{q-j}e^{\mathrm{i}j\delta}}{o_q}.
```

Feasibility of the calibrated instrument ensures that $`e_q,o_q>0`$ when a conclusive row has nonzero weight in sector $`q`$. If the true sign is $`s`$ and the reported sign is $`t`$, put $`g_q^{st}=(A_q+st\,C_q)/2`$. A conclusive charge shift $`\ell`$ produces the unnormalized reference vector

```math
|\xi_{t,\ell}\rangle
=\sqrt{p_\ell}\,e^{\mathrm{i}\ell\phi}\sum_i c_i e^{\mathrm{i}i\phi}g_{i+\ell}^{st}|i\rangle.
```

The corresponding sign probability and squared fidelity of the reference to its original pure state, conditional on that sign, are

```math
\begin{aligned}
P_t&=\sum_\ell p_\ell\sum_i w_i |g_{i+\ell}^{st}|^2,\\
F_t&=\frac{\sum_\ell p_\ell\left|\sum_i w_i g_{i+\ell}^{st}\right|^2}{P_t}.
\end{aligned}
```

Here $`F_t`$ is defined when $`P_t>0`$. The abort probability is $`1-P_{+1}-P_{-1}`$. For the conditional trace distance $`D_t=\tfrac12\|\rho_{R\mid t}-|R_\phi\rangle\langle R_\phi|\|_1`$, one has $`D_t\le\sqrt{1-F_t}`$, with equality when only one shift is used.

These formulas follow by taking inner products of the mismatched input with the calibrated even and odd vectors in each sector. They keep the charge sectors coherent until the reference output is formed. They also give the general bound $`P_{-s}\le pk^2\delta^2/4`$, where $`p=\sum_\ell p_\ell`$. For any even charge $`j`$ and odd charge $`j'`$, $`\left|e^{\mathrm{i}j\delta}-e^{\mathrm{i}j'\delta}\right|\le |j-j'||\delta|`$. Taking the product average over the two normalized parity distributions yields $`|A_q-C_q|\le k|\delta|`$. Also $`|g_q^{+1}-1|\le k|\delta|`$. If $`k|\delta|<1`$, then $`P_s\ge p(1-k|\delta|)^2`$ and $`D_s\le k|\delta|/(1-k|\delta|)`$. To see the second bound, write $`1-F_s`$ as the sum of the within-shift variances of $`g_{i+\ell}^{+1}`$ with respect to $`w_i`$, multiplied by $`p_\ell/P_s`$. Each variance is at most $`\sum_i w_i|g_{i+\ell}^{+1}-1|^2`$.

## Two copies and the optimal reference

Set $`L=N+2`$ with $`N\ge1`$, $`\theta=\pi/L`$ and

```math
w_i=\frac{\sin[(i+1)\theta]}{\sum_{j=1}^{L-1}\sin(j\theta)},
\qquad
p=\cos\theta.
```

The receiver uses the single shift $`\ell=1`$. Define

```math
d_i=\frac{w_{i-1}-w_{i+1}}{w_{i-1}+w_{i+1}},
\qquad
M=\sum_i w_i d_i^2.
```

The weights are reflection-symmetric and $`d_{N-i}=-d_i`$, so $`\sum_i w_i d_i=0`$. The even and odd responses in sector $`i+1`$ are

```math
A_{i+1}=e^{\mathrm{i}\delta}(\cos\delta+\mathrm{i}d_i\sin\delta), \qquad C_{i+1}=e^{\mathrm{i}\delta}.
```

Consequently,

```math
\begin{aligned}
P_s &=\frac p4\left[(1+\cos\delta)^2+M\sin^2\delta\right],\\
P_{-s}&=\frac p4\left[(1-\cos\delta)^2+M\sin^2\delta\right],\\
P_{?}&=1-p+\frac p2(1-M)\sin^2\delta,\\
D_{\pm s}
&=\frac{\sqrt{M}\,|\sin\delta|}
{\sqrt{(\cos\delta\pm1)^2+M\sin^2\delta}},
\end{aligned}
```

where each conditional distance is defined on a label of positive probability. The disturbance formula comes from projecting the pure returned vector onto $`|R_\phi\rangle`$. The part proportional to $`d_i`$ is orthogonal to $`|R_\phi\rangle`$ because $`\sum_i w_i d_i=0`$.

If the offsets of the two signals are $`\delta_1,\delta_2`$, set $`\bar\delta=(\delta_1+\delta_2)/2`$ and $`\Delta=(\delta_1-\delta_2)/2`$. The even response is $`e^{\mathrm{i}\bar\delta}(\cos\bar\delta+\mathrm{i}d_i\sin\bar\delta)`$ and the odd response is $`e^{\mathrm{i}\bar\delta}\cos\Delta`$. Thus

```math
\begin{aligned}
P_{\pm s}&=\frac p4\left[(\cos\bar\delta\pm\cos\Delta)^2+M\sin^2\bar\delta\right],\\
P_{?}&=1-\frac p2\left[\cos^2\bar\delta+\cos^2\Delta+M\sin^2\bar\delta\right],\\
D_{\pm s}&=\frac{\sqrt{M}\,|\sin\bar\delta|}
{\sqrt{(\cos\bar\delta\pm\cos\Delta)^2+M\sin^2\bar\delta}}.
\end{aligned}
```

Only the symmetric part of the charge-one signal sector enters the conclusive rows. The antisymmetric component from unequal offsets goes to the abort branch.

## Size and alignment scales

The sine profile gives an exact finite sum for the disturbance coefficient. The identity $`d_i=-\tan\theta\cot[(i+1)\theta]`$ implies

```math
M=\tan^2\theta
\left[\frac{\sum_{j=1}^{L-1}\csc(j\theta)}{\cot(\theta/2)}-1\right]
=\frac{\pi^2}{L^2}\left(\log L+O(1)\right).
```

For the asymptotic estimate, subtract $`1/x+1/(\pi-x)`$ from $`\csc x`$. The residual is bounded on $`(0,\pi)`$, so the discrete sum is $`(2L/\pi)\log L+O(L)`$. At $`N=1`$, $`M=1`$ and the common offset changes the sign distribution while the abort probability stays constant.

For small common offset, the wrong-label probability is $`O(\delta^4+M\delta^2)`$ and the disturbance on the correct-label branch is $`O(\sqrt M\,|\delta|)`$. The ideal abort probability is $`1-p\sim \pi^2/(2L^2)`$ and mismatch adds $`p(1-M)\sin^2\delta/2`$. In particular, a sufficiently small offset of order $`L^{-1}`$ preserves the $`L^{-2}`$ abort scaling, while the wrong-label probability and correct-label disturbance are respectively $`O((\log L)/L^4)`$ and $`O(\sqrt{\log L}/L^2)`$. These are guarantees for the calibrated receiver on an individual batch. The formulas track the reference on both conclusive branches, including wrong-label branches.

## A profile with reduced disturbance

The two-copy receiver can trade ideal success for reduced sensitivity to phase mismatch. Use the symmetric weights

```math
w_i=\frac{\sin^2[(i+1)\theta]}{\sum_{j=1}^{L-1}\sin^2(j\theta)}.
```

For a fixed reference, the greatest allowed two-copy success is the minimum of $`1`$ and the neighboring-weight ratios $`(w_{i-1}+w_{i+1})/(2w_i)`$. For these weights the ratio at $`j=i+1`$ is

```math
\cos^2\theta+\sin^2\theta\cot^2(j\theta).
```

Its minimum is $`\cos^2\theta`$ for even $`L`$ and $`\cos^2\theta+\sin^2\theta\tan^2(\theta/2)`$ for odd $`L`$. In either case the ideal abort probability is $`\theta^2+O(\theta^4)`$, compared with $`\theta^2/2+O(\theta^4)`$ for the success-optimal reference.

The two-copy response formulas still apply because the charge-one odd response is unchanged and the weights are symmetric. For the squared-sine weights,

```math
d_i=\frac{-2\tan\theta\cot[(i+1)\theta]}
{1+\tan^2\theta\cot^2[(i+1)\theta]}.
```

The denominator gives the uniform bound

```math
M\le4\tan^2\theta\,\frac{\sum_{j=1}^{L-1}\cos^2(j\theta)}
{\sum_{j=1}^{L-1}\sin^2(j\theta)}
=4\tan^2\theta(1-2/L).
```

In fact $`M\sim4\theta^2`$. On each fixed interior subinterval of $`(0,\pi)`$ the denominator of $`d_i`$ tends uniformly to one. After multiplication by $`\sin^2(j\theta)`$ the associated normalized summand is bounded by $`\cos^2(j\theta)`$, so the contribution of arbitrarily small end intervals can be bounded uniformly before taking the Riemann limit.

At a common offset $`\delta=O(L^{-1})`$, this reference gives an abort probability of order $`L^{-2}`$, a wrong-label probability $`O(L^{-4})`$, and correct-label trace distance $`O(L^{-2})`$. It thus removes the logarithmic factors of the success-optimal profile in this calibrated receiver. Optimizing the profile and receiver jointly for a prescribed combination of errors, aborts, and returned-state disturbance is a separate optimization.
