# How the copy count changes the failure rate

A receiver with $`k`$ identical signals makes a zero-error phase-label measurement using a pure reference on charges $`0,\ldots,N`$. It returns the same phase-oriented reference on either conclusive outcome. Under the [common phase and resource assumptions](model.md), let $`\delta_k^{\mathrm{ret}}(N)`$ denote the smallest worst-case failure probability, optimized over the receiver and reference. Let $`\delta_k^{\mathrm{free}}(N)`$ denote the analogous optimum when the reference can be discarded.

For each fixed integer $`k\ge 2`$, as $`N\to\infty`$,

```math
\delta_k^{\mathrm{ret}}(N)=\Theta_k\!\left(N^{-2\lfloor k/2\rfloor}\right),
\qquad
\delta_k^{\mathrm{free}}(N)=\Theta_k\!\left(N^{-k}\right).
```

The exponents for two, three, and four copies under exact return are respectively two, two, and four. An odd extra copy can still affect the finite-size probability. The theorem fixes the copy count before growing the ladder and allows the reference profile to depend on both.

## Charge distributions

Write $`w_i=|c_i|^2`$ for the reference charge distribution, extended by zero outside $`0,\ldots,N`$. Set $`B_j=2^{-k}\binom{k}{j}`$ on $`0,\ldots,k`$. The even and odd parts of this binomial law are $`B_{\mathrm e}`$ and $`B_{\mathrm o}`$. For total charge $`q`$, define

```math
e_q=(B_{\mathrm e}*w)_q,\qquad
o_q=(B_{\mathrm o}*w)_q,\qquad
(\Delta w)_q=w_q-w_{q-1}.
```

The [receiver construction](receiver.md) shows that exact return for a fixed $`w`$ is possible with success $`p`$ if and only if there are nonnegative masses $`p_\ell`$ on $`\ell=1,\ldots,k-1`$ with sum $`p`$ and

```math
(P*w)_q\le 2\min(e_q,o_q)\qquad\text{for every }q.
```

Here $`P`$ is the sequence of masses $`p_\ell`$ and has zeros at both endpoints $`0,k`$. The bound uses the same success probability for each sign, which can be arranged by sign symmetrization.

## Baseline without the reference return

When the reference can be discarded, the receiver may measure the total charge and run unambiguous sign discrimination within each sector. The unnormalized signal alternatives in sector $`q`$ have common squared norm $`e_q+o_q`$ and overlap $`e_q-o_q`$. The optimal conclusive mass in that sector is $`2\min(e_q,o_q)`$. Thus the optimal failure probability for a fixed profile is

```math
\sum_q |e_q-o_q|=2^{-k}\sum_q |(\Delta^k w)_q|.
```

For $`\theta=1/(N+1)`$, the Fourier transform $`\widehat w(\theta)=\sum_i w_i e^{\mathrm i i\theta}`$ satisfies $`|\widehat w(\theta)|\ge\cos(1/2)`$. After rotation by the midpoint phase, each unit vector in the weighted sum has real part at least $`\cos(1/2)`$. The Fourier transform of the backward difference multiplies by $`1-e^{\mathrm i\theta}`$, so

```math
2^{-k}\sum_q |(\Delta^k w)_q|
\ge 2^{-k}|1-e^{\mathrm i\theta}|^k|\widehat w(\theta)|
\ge \cos(1/2)\,\sin^k\!\left(\frac{1}{2(N+1)}\right).
```

This lower bound holds uniformly over the reference profile. It also bounds the failure probability with exact return.

For the upper bound, set $`h=\pi/(N+2)`$ and use the normalized samples of the function $`f_k(x)=\sin^k x`$ on $`[0,\pi]`$, extended by zero elsewhere:

```math
v_i=f_k((i+1)h),\qquad w_i=\frac{v_i}{\sum_j v_j}.
```

The zero extension has continuous derivatives through order $`k-1`$. Its derivative of order $`k-1`$ is absolutely continuous with bounded derivative almost everywhere. The fundamental theorem of calculus, applied once per difference, gives

```math
(\Delta^k v)_q
=\int_{[0,h]^k} f_k^{(k)}\!\left((q+1)h-t_1-\cdots-t_k\right)\,dt_1\cdots dt_k.
```

Hence $`|(\Delta^k v)_q|\le C_k h^k`$ for every $`q`$. There are at most $`N+k+1`$ nonzero terms, and the reference normalizer is of order $`N+1`$ because the profile is bounded below on a fixed central interval. The normalized failure is therefore $`O_k(N^{-k})`$.

## A receiver for an even number of signals

Take even $`k`$ and use the same sine-power profile. Set $`p_\ell=2p B_\ell`$ at odd $`\ell`$ and set the other masses to zero. All odd binomial shifts lie strictly inside $`1,\ldots,k-1`$, and their unscaled binomial weight is $`1/2`$. The shift masses sum to $`p`$, and the LP constraints are equivalent to

```math
p\le 1,\qquad p\le\frac{e_q}{o_q}\quad\text{whenever }o_q>0.
```

To bound the ratios, use the unnormalized convolutions $`\bar e_q=(B_{\mathrm e}*v)_q`$ and $`\bar o_q=(B_{\mathrm o}*v)_q`$. Their difference is $`2^{-k}(\Delta^k v)_q`$. For even $`k`$, the derivative $`f_k^{(k)}`$ tends to $`k!`$ from inside the interval at both ends. It vanishes outside, so any region where it is negative is confined to some fixed interval $`[a,\pi-a]`$ with $`a>0`$ depending on $`k`$.

If $`\bar e_q-\bar o_q<0`$, the integration interval in the finite-difference formula must intersect $`[a,\pi-a]`$. When $`kh<a/2`$, all samples used by the convolution then lie in $`[a/2,\pi-a/2]`$. In particular, the odd convolution is bounded below by a positive constant that depends only on $`k`$. The finite-difference bound gives $`\bar e_q/\bar o_q\ge 1-C'_kh^k`$ in these sectors. In all other sectors with $`\bar o_q>0`$, the ratio is at least one. This proves that the exact-return construction achieves failure $`O_k(N^{-k})`$. The Fourier lower bound gives the matching order.

## The penalty for an odd number of signals

For odd $`k\ge3`$, ignoring one signal achieves the even-copy order $`O_k(N^{-(k-1)})`$. Discarding the extra input qubit is covariant and has no effect on the other independent signals. To prove the converse, consider any feasible shift law $`P`$ and put

```math
r_q=((B-P)*w)_q.
```

The LP constraint implies $`r_q\ge0`$ since $`2\min(e_q,o_q)\le e_q+o_q`$. Its total mass is $`1-p`$. Although $`B-P`$ can contain negative coefficients, this convolved sequence is a nonnegative measure and serves as the failure distribution over total input charge.

Let $`m=k-1`$ and $`g(j)=\prod_{\ell=1}^{m}(j-\ell)`$. This polynomial vanishes on the allowed shift window and satisfies $`g(0)=g(k)=m!`$ because $`m`$ is even. For a random variable $`I`$ with law $`w`$, there is a unique degree $`m`$ polynomial $`F`$ satisfying

```math
\mathbb E[F(I+j)]=g(j)
```

as a polynomial identity in $`j`$. The linear map on coefficients is triangular with diagonal entries one. Writing $`F(x)=\sum_{a=0}^m b_a x^a`$, the leading coefficient is one and the coefficient of $`j^s`$ in the expectation is

```math
b_s+\sum_{a=s+1}^m \binom{a}{s}b_a\,\mathbb E[I^{a-s}].
```

Since $`0\le I\le N`$, descending induction gives $`|b_a|\le C_k(N+1)^{m-a}`$, with a constant independent of the profile. Thus $`\max_{0\le q\le N+k}|F(q)|\le C'_k(N+1)^m`$. The expectation identity now yields

```math
\sum_q r_q F(q)
=\sum_j(B_j-P_j)g(j)
=2^{1-k}(k-1)!.
```

Nonnegativity of $`r`$ bounds the left side by $`(1-p)C'_k(N+1)^m`$. This gives $`1-p=\Omega_k(N^{-(k-1)})`$ and completes the parity law.

The obstruction comes from the two endpoint charges that cannot appear in a conclusive shift. At odd copy count, the polynomial that kills all interior shifts gives both endpoints the same sign. A finite amount of failure is needed to carry that endpoint contribution.

## Three copies halve the leading failure constant

The third copy improves the leading constant even though the exponent stays the same. Set $`h=\pi/(N+2)`$. The optimum satisfies

```math
\lim_{N\to\infty}\frac{\delta_3^{\mathrm{ret}}(N)}{h^2}=\frac14.
```

For comparison, the [two-copy cosine formula](receiver.md) gives a limit of $`1/2`$ in the same units. To bound three-copy success, use the even-sector constraint at $`q=i+1`$ and the odd-sector constraint at $`q=i+2`$. They read

```math
\begin{aligned}
4p_1w_i+(4p_2-3)w_{i-1}&\le w_{i+1},\\
4p_2w_i+(4p_1-3)w_{i+1}&\le w_{i-1}.
\end{aligned}
```

Adding and dividing by four gives $`p w_i\le(1-p_1)w_{i+1}+(1-p_2)w_{i-1}`$. The two off-diagonal coefficients are positive because the Fourier bound gives $`p<1`$ for finite $`N`$. Diagonal similarity transforms this tridiagonal matrix to the path adjacency multiplied by $`\sqrt{(1-p_1)(1-p_2)}`$. Multiplying the componentwise inequality by its positive top left eigenvector gives

```math
p\le 2\sqrt{(1-p_1)(1-p_2)}\cos h
\le (2-p)\cos h.
```

It follows that $`\delta_3^{\mathrm{ret}}(N)\ge(1-\cos h)/(1+\cos h)`$.

For achievability, choose $`p_1=p_2=(1-\delta)/2`$ and take a reference profile proportional to $`v_i=\sin^\alpha((i+1)h)`$ with fixed $`1<\alpha<2`$. With zero extension of the samples, the two sector inequalities above are satisfied throughout the ladder when

```math
\delta\ge
\max_{0\le i\le N}
\frac{(2v_i-v_{i-1}-v_{i+1})_+}
     {2\bigl(v_i+\min(v_{i-1},v_{i+1})\bigr)}.
```

The remaining exterior inequalities follow from $`4p_1,4p_2\le 2`$. For $`f(x)=\sin^\alpha x`$ on the open interval, direct differentiation gives $`f''/f=-\alpha+\alpha(\alpha-1)\cot^2 x\ge-\alpha`$. The zero extension has an absolutely continuous first derivative. The centered second difference is the integral of $`f''`$ against a triangular kernel supported within distance $`h`$ of the sample point and of total mass $`h^2`$. Since $`f''`$ is nonnegative near the endpoints and outside, any strictly positive numerator must be centered in a fixed compact subinterval of $`(0,\pi)`$ for sufficiently small $`h`$. There $`v_i`$ is bounded below and the negative second difference is at most $`\alpha h^2(v_i+O_\alpha(h))`$. The denominator is $`4v_i+O_\alpha(h)`$. The displayed maximum is therefore at most $`(\alpha/4+O_\alpha(h))h^2`$. Taking the limit superior at fixed $`\alpha`$ and then letting $`\alpha\downarrow1`$ proves the claimed constant.

The [phase-mismatch analysis](phase-mismatch.md) studies how the common-phase promise affects the receiver in a different regime. The [verification guide](../verification/README.md) describes the finite checks of the receiver and example profiles.
