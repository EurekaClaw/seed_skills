---
name: fundamental-inequalities
description: A comprehensive reference of fundamental mathematical inequalities based on László Kozma's cheat sheet. Contains algebraic, elementary function, means, convexity, matrices, and combinatorial inequalities (excludes probability and concentration inequalities).
---

# Fundamental Inequalities Cheat Sheet

This skill provides a curated collection of fundamental inequalities commonly used in mathematical proofs, algorithmic analysis, and bound derivations. It is based on [László Kozma's Useful Inequalities cheat sheet](https://www.lkozma.net/inequalities_cheat_sheet/ineq.pdf). 

*Note: Concentration and probability tail inequalities (such as Markov, Chebyshev, Chernoff, Hoeffding, Azuma, McDiarmid, etc.) are explicitly excluded as they belong to the [`concentration_inequalities` skill.](https://github.com/EurekaClaw/seed_skills/blob/main/concentration_inequalities/SKILL.md)*

## 1. Classical Inequalities

- **Cauchy-Schwarz**: 
  $$ \left( \sum_{i=1}^n x_i y_i \right)^2 \leq \left( \sum_{i=1}^n x_i^2 \right) \left( \sum_{i=1}^n y_i^2 \right) $$

- **Minkowski**: 
  $$ \left( \sum_{i=1}^n |x_i + y_i|^p \right)^{1/p} \leq \left( \sum_{i=1}^n |x_i|^p \right)^{1/p} + \left( \sum_{i=1}^n |y_i|^p \right)^{1/p} \quad \text{for } p \geq 1 $$

- **Hölder**: 
  $$ \sum_{i=1}^n |x_i y_i| \leq \left( \sum_{i=1}^n |x_i|^p \right)^{1/p} \left( \sum_{i=1}^n |y_i|^q \right)^{1/q} \quad \text{for } p, q > 1, \; \frac{1}{p} + \frac{1}{q} = 1 $$

## 2. Algebraic and Elementary Functions

### Bernoulli
- $ (1 + x)^r \geq 1 + rx $ for $ x \geq -1, r \in \mathbb{R} \setminus (0, 1) $. Reverse holds for $ r \in[0, 1] $.
- $ (1 + x)^r \leq \frac{1}{1 - rx} $ for $ x \in[-1, 1/r) $, $ r \geq 0 $.
- $ (1 + x)^r \leq 1 + \frac{x}{x+1}r $ for $ x \geq 0 $, $ r \in [-1, 0] $.
- $ (1 + x)^r \leq 1 + (2r - 1)x $ for $ x \in[0, 1], r \in \mathbb{R} \setminus (0, 1) $.
- $ (1 + nx)^{n+1} \geq (1 + (n+1)x)^n $ for $ x \geq 0, n \in \mathbb{N} $.
- $ (a + b)^n \leq a^n + nb(a + b)^{n-1} $ for $ a, b \geq 0, n \in \mathbb{N} $.

### Exponential
- $ e^x \geq \left(1 + \frac{x}{n}\right)^n \geq 1 + x $ and $ \left(1 + \frac{x}{n}\right)^n \geq e^x \left(1 - \frac{x^2}{n}\right) $ for $ n \geq 1, |x| \leq n $.
- $ \frac{x^n}{n!} + 1 \leq e^x \leq \left(1 + \frac{x}{n}\right)^{n+x/2} $ for $ x, n > 0 $.
- $ x^y + y^x > 1 $; $ x^y > \frac{x}{x+y} $; $ e^x > \left(1 + \frac{x}{y}\right)^y > e^{\frac{xy}{x+y}} $; $ x^y \geq e^{x-y}x^x $ for $ x, y > 0 $.
- $ x e^x \geq x + x^2 + \frac{x^3}{2} $; $ e^x \leq x + e^{x^2} $; $ e^x + e^{-x} \leq 2e^{x^2/2} $ for $ x \in \mathbb{R} $.

### Logarithm
- $ \frac{x}{1+x} \leq \ln(1 + x) \leq \frac{x(6+x)}{6+4x} \leq x $ for $ x > -1 $.
- $ \frac{1}{n+1} < \ln(n+1) - \ln(n) < \frac{1}{n} \leq \sum_{i=1}^n \frac{1}{i} \leq \ln(n) + 1 $ for $ n \geq 1 $.
- $ |\ln x| \leq \frac{1}{2} \left| x - \frac{1}{x} \right| $; $ \ln(x+y) \leq \ln(x) + \frac{y}{x} $; $ \ln x \leq y(x^{1/y} - 1) $ for $ x, y > 0 $.
- $ \ln(1 + x) \geq x - \frac{x^2}{2} $ for $ x \geq 0 $; $ \ln(1 + x) \geq x - x^2 $ for $ x \geq -0.68 $.

### Square Root
- $ 2\sqrt{x+1} - 2\sqrt{x} < \frac{1}{\sqrt{x}} < \sqrt{x+1} - \sqrt{x-1} < 2\sqrt{x} - 2\sqrt{x-1} $ for $ x \geq 1 $.
- $ x \leq \frac{x+1}{2} - \frac{(x-1)^2}{2} \leq \sqrt{x} \leq \frac{x+1}{2} - \frac{(x-1)^2}{8} $ for $ x \in[0, 1] $.

## 3. Combinatorial and Information Theoretic

### Binomial and Stirling
- $ \max\left\{ \left(\frac{n}{k}\right)^k, \frac{(n-k+1)^k}{k!} \right\} \leq \binom{n}{k} \leq \frac{n^k}{k!} \leq \left(\frac{en}{k}\right)^k $.
- $ \binom{n}{k} \leq \frac{n^n}{k^k (n-k)^{n-k}} $.
- **Stirling**: $ e\left(\frac{n}{e}\right)^n \leq \sqrt{2\pi n} \left(\frac{n}{e}\right)^n e^{\frac{1}{12n+1}} \leq n! \leq \sqrt{2\pi n} \left(\frac{n}{e}\right)^n e^{\frac{1}{12n}} \leq en\left(\frac{n}{e}\right)^n $.

### Binary Entropy
Let $ H(x) = -x \lg x - (1-x) \lg (1-x) $:
- $ H(x) \leq \min \left\{ x \lg \frac{4}{x}, (1-x) \lg \frac{4}{1-x}, (4x(1-x))^{\frac{1}{\ln 4}}, \lg x \cdot \lg (1-x) \right\} $.
- $ H(x) \geq \max \{ 4x(1-x), \ln 2 \cdot \lg x \cdot \lg (1-x) \} $ for $ x \in (0, 1) $.

## 4. Means and Convexity

### Means
- $ \min x_i \leq \frac{n}{\sum x_i^{-1}} \leq \left( \prod x_i \right)^{1/n} \leq \frac{1}{n} \sum x_i \leq \sqrt{\frac{1}{n} \sum x_i^2} \leq \max x_i $.

### Power Means
- $ M_p \leq M_q $ for $ p \leq q $, where $ M_p = \left( \sum w_i |x_i|^p \right)^{1/p} $ with $ w_i \geq 0, \sum w_i = 1 $.

### Jensen
- $ \phi\left( \sum p_i x_i \right) \leq \sum p_i \phi(x_i) $ where $ p_i \geq 0, \sum p_i = 1 $, and $ \phi $ is convex. Alternatively: $ \phi(\mathbb{E}[X]) \leq \mathbb{E}[\phi(X)] $. (Reverse for concave $ \phi $).

### Rearrangement & Weierstrass
- **Rearrangement**: $ \sum_{i=1}^n a_i b_i \geq \sum_{i=1}^n a_i b_{\pi(i)} \geq \sum_{i=1}^n a_i b_{n-i+1} $ for $ a_1 \leq \dots \leq a_n $, $ b_1 \leq \dots \leq b_n $.
- **Weierstrass**: $ 1 - \sum w_i x_i \leq \prod (1 - x_i)^{w_i} $ and $ 1 + \sum w_i x_i \leq \prod (1 + x_i)^{w_i} \leq \prod (1 - x_i)^{-w_i} $ for $ x_i \in [0, 1], w_i \geq 1 $.

## 5. Sums, Integrals, and Matrices

### Cauchy, Hermite-Hadamard, Kantorovich
- **Cauchy**: $ f'(a) \leq \frac{f(b) - f(a)}{b - a} \leq f'(b) $ where $ a < b $ and $ f $ is convex.
- **Hermite**: $ \phi\left(\frac{a+b}{2}\right) \leq \frac{1}{b-a} \int_a^b \phi(x) dx \leq \frac{\phi(a)+\phi(b)}{2} $ for $ \phi $ convex.
- **Kantorovich**: $ \left(\sum x_i^2\right)\left(\sum y_i^2\right) \leq \left(\frac{A}{G}\right)^2 \left(\sum x_i y_i\right)^2 $ where $ 0 < m \leq \frac{x_i}{y_i} \leq M < \infty $, $ A = \frac{m+M}{2} $, $ G = \sqrt{mM} $.

### Information Divergence
- **Gibbs**: $ \sum a_i \log \frac{a_i}{b_i} \geq a \log \frac{a}{b} $ for $ a_i, b_i \geq 0, a = \sum a_i, b = \sum b_i $.
- **Pinsker**: $ \sum a_i \lg \frac{a_i}{b_i} \geq \frac{1}{2} \left( \sum |a_i - b_i| \right)^2 $ for $ a_i, b_i \geq 0, \sum a_i = \sum b_i = 1 $.

### Matrices
- **Hadamard**: $ (\det A)^2 \leq \prod_{i=1}^n \sum_{j=1}^n A_{ij}^2 $ where $ A $ is an $ n \times n $ matrix.
- **Schur**: $ \sum_{i=1}^n \lambda_i^2 \leq \sum_{i=1}^n \sum_{j=1}^n A_{ij}^2 $ and $ \sum_{i=1}^k d_i \leq \sum_{i=1}^k \lambda_i $ for $ 1 \leq k \leq n $. ($ A $ is symmetric for the second inequality, with $ \lambda_i $ eigenvalues and $ d_i $ diagonal elements).

## 6. Miscellaneous

- **Samuelson**: $ \mu - \sigma\sqrt{n-1} \leq x_i \leq \mu + \sigma\sqrt{n-1} $ for $ i = 1, \dots, n $, where $ \mu = \frac{1}{n} \sum x_i $ and $ \sigma^2 = \frac{1}{n} \sum (x_i - \mu)^2 $.
- **Sum & Product**: $ \left| \prod_{i=1}^n a_i - \prod_{i=1}^n b_i \right| \leq \sum_{i=1}^n |a_i - b_i| $ for $ |a_i|, |b_i| \leq 1 $.
- **Karamata**: $ \sum_{i=1}^n \phi(a_i) \geq \sum_{i=1}^n \phi(b_i) $ for majorization $ \{a_i\} \succeq \{b_i\} $ and convex $ \phi $.
- **Hilbert**: $ \sum_{m=1}^\infty \sum_{n=1}^\infty \frac{a_m b_n}{m+n} \leq \pi \left( \sum_{m=1}^\infty a_m^2 \right)^{1/2} \left( \sum_{n=1}^\infty b_n^2 \right)^{1/2} $.
- **Hardy**: $ \sum_{n=1}^\infty \left( \frac{a_1 + \dots + a_n}{n} \right)^p \leq \left( \frac{p}{p-1} \right)^p \sum_{n=1}^\infty a_n^p $ for $ a_n \geq 0, p > 1 $.
- **FKG**: $ 2^n \cdot |A \cap B| \geq |A| \cdot |B| $ for monotone set systems $ A, B $ over $ \{1, \dots, n\} $.