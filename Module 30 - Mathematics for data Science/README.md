# **Context**

- [**Context**](#context)
- [**Day 42 - Mathematics For Data Science 01**](#day-42---mathematics-for-data-science-01)
  - [**Linear Algebra**](#linear-algebra)
    - [Vectors](#vectors)
    - [Scalars](#scalars)
    - [Matrices](#matrices)
    - [Core Matrix Properties and Decompositions](#core-matrix-properties-and-decompositions)
  - [**Statistics \& Probability**](#statistics--probability)
- [**Day 43 - Mathematics For Data Science 02**](#day-43---mathematics-for-data-science-02)
  - [**Calculus**](#calculus)
    - [Differential Calculus](#differential-calculus)
    - [Integral Calculus](#integral-calculus)
  - [**Optimization**](#optimization)

# **Day 42 - Mathematics For Data Science 01**

## **Linear Algebra**

- **Linear Algebra** is a branch of mathematics that studies **vectors, matrices, and linear equations**, and how they transform and relate to each other.In simple terms, linear algebra is the mathematics of working with structured numbers arranged in rows and columns to model relationships between variables.
- It is the most important math topic in Data Science. Used in `ML models`, `neural networks`, `embeddings`, `PCA`, `SVD`, etc.

- It provides the mathematical framework for representing and solving systems like:

```math
Ax = b
```

- Here
  - $A$ is a matrix
  - $x$ is a vector of variables
  - $b$ is a result vector

[⬆️ Go to Context](#context)

### Vectors

- **Vector Basics**: An ordered array of numbers representing magnitude and direction in n-dimensional space
  - **Formula**: **v** = [v₁, v₂, v₃, ..., vₙ]
  - **Where used**: Feature representation, word embeddings, coordinate systems

    ```py
    import numpy as np
    vector_a = np.array([1, 2, 3])
    vector_b = np.array([4, 5, 6])
    ```

- **Dot Product (Vector)**: Scalar result from multiplying corresponding elements and summing them
  - **Formula**: **a** · **b** = a₁b₁ + a₂b₂ + ... + aₙbₙ = Σ(aᵢbᵢ)
  - **Where used**: Similarity measures, neural network computations, cosine similarity

    ```py
    dot_product = np.dot(vector_a, vector_b)  # Result: 32
    # Or: vector_a @ vector_b
    ```

- **Cross Product (Vector)**: Vector perpendicular to two input vectors (only in 3D)
  - **Formula**: **a** × **b** = [a₂b₃ - a₃b₂, a₃b₁ - a₁b₃, a₁b₂ - a₂b₁]
  - **Where used**: Computer graphics, robotics, physics simulations

    ```py
    cross_product = np.cross(vector_a, vector_b)  # Result: [-3, 6, -3]
    ```

- **Vector Magnitude (Norm)**: Length of a vector
  - **Formula**: ||**v**|| = √(v₁² + v₂² + ... + vₙ²)
  - **Where used**: Distance calculations, normalization, regularization

    ```py
    magnitude = np.linalg.norm(vector_a)  # L2 norm
    ```

- **Unit Vector (Normalization)**: Vector with magnitude 1
  - **Formula**: **û** = **v** / ||**v**||
  - **Where used**: Feature scaling, gradient descent optimization

    ```py
    unit_vector = vector_a / np.linalg.norm(vector_a)
    ```

- **Cosine Similarity**: Measure of similarity between two vectors
  - **Formula**: cos(θ) = (**a** · **b**) / (||**a**|| × ||**b**||)
  - **Where used**: Text similarity, recommendation systems, clustering

    ```py
    from sklearn.metrics.pairwise import cosine_similarity
    similarity = cosine_similarity([vector_a], [vector_b])
    ```

[⬆️ Go to Context](#context)

### Scalars

- **Scalar Basics**: A single numerical value
  - **Formula**: k ∈ ℝ (a real number)
  - **Where used**: Learning rates, weights, biases, temperature in softmax

    ```py
    scalar = 5
    scaled_vector = scalar * vector_a  # [5, 10, 15]
    ```

- **Scalar Multiplication (Vector)**: Multiplying each element of a vector by a scalar
  - **Formula**: k**v** = [kv₁, kv₂, ..., kvₙ]
  - **Where used**: Feature scaling, adjusting learning rates

    ```py
    result = 3 * vector_a  # [3, 6, 9]
    ```

- **Scalar Multiplication (Matrix)**: Multiplying each element of a matrix by a scalar
  - **Formula**: kA = [ka₁₁, ka₁₂, ...; ka₂₁, ka₂₂, ...]
  - **Where used**: Weight initialization, gradient scaling

    ```py
    matrix = np.array([[1, 2], [3, 4]])
    scaled_matrix = 2 * matrix  # [[2, 4], [6, 8]]
    ```

[⬆️ Go to Context](#context)

### Matrices

- **Matrix Basics**: 2D array of numbers arranged in rows and columns
  - **Formula**: A = [a₁₁, a₁₂, ..., a₁ₙ; a₂₁, a₂₂, ..., a₂ₙ; ...; aₘ₁, aₘ₂, ..., aₘₙ]
  - **Where used**: Data representation, transformations, neural network layers

    ```py
    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    ```

- **Matrix Order (Shape)**: Dimensions of a matrix (rows × columns)
  - **Formula**: A ∈ ℝᵐˣⁿ (m rows, n columns)
  - **Where used**: Ensuring compatible matrix operations, defining model architecture

    ```py
    shape = matrix.shape  # (2, 3) - 2 rows, 3 columns
    ```

- **Null (Zero) Matrix**: Matrix with all elements as zero
  - **Formula**: O = [0, 0, ..., 0; 0, 0, ..., 0; ...]
  - **Where used**: Initialization, padding, placeholder matrices

    ```py
    null_matrix = np.zeros((3, 3))
    ```

- **Identity Matrix**: Square matrix with 1s on diagonal, 0s elsewhere
  - **Formula**: I = [1, 0, ..., 0; 0, 1, ..., 0; ...; 0, 0, ..., 1]
  - **Where used**: Matrix inverse verification, neutral element in multiplication

    ```py
    identity = np.eye(3)  # 3x3 identity matrix
    ```

- **Square Matrix**: Matrix with equal rows and columns
  - **Formula**: A ∈ ℝⁿˣⁿ
  - **Where used**: Covariance matrices, correlation matrices, transformation matrices

    ```py
    square_matrix = np.array([[1, 2], [3, 4]])
    ```

- **Column Matrix**: Matrix with single column
  - **Formula**: **c** = [c₁; c₂; ...; cₘ] ∈ ℝᵐˣ¹
  - **Where used**: Feature vectors, target variables in regression

    ```py
    column_matrix = np.array([[1], [2], [3]])  # Shape: (3, 1)
    ```

- **Row Matrix**: Matrix with single row
  - **Formula**: **r** = [r₁, r₂, ..., rₙ] ∈ ℝ¹ˣⁿ
  - **Where used**: Single data sample, probability distributions

    ```py
    row_matrix = np.array([[1, 2, 3]])  # Shape: (1, 3)
    ```

- **Transpose Matrix**: Flipping rows and columns
  - **Formula**: (Aᵀ)ᵢⱼ = Aⱼᵢ
  - **Where used**: Changing data orientation, matrix calculations, neural networks

    ```py
    transposed = matrix.T  # or np.transpose(matrix)
    ```

- **Adjoint (Adjugate) Matrix**: Transpose of cofactor matrix
  - **Formula**: adj(A) = Cᵀ (where C is cofactor matrix)
  - **Where used**: Computing matrix inverse, theoretical linear algebra

    ```py
    # For 2x2 matrix
    A = np.array([[1, 2], [3, 4]])
    det = np.linalg.det(A)
    adj = det * np.linalg.inv(A)  # Adjoint = det(A) * A^(-1)
    ```

- **Inverse Matrix**: Matrix that when multiplied gives identity matrix
  - **Formula**: A⁻¹A = AA⁻¹ = I, where A⁻¹ = adj(A) / det(A)
  - **Where used**: Solving linear equations, linear regression (normal equation)

    ```py
    A = np.array([[4, 7], [2, 6]])
    A_inv = np.linalg.inv(A)
    # Verify: A @ A_inv ≈ Identity
    ```

- **Matrix Addition**: Adding corresponding elements of matrices
  - **Formula**: (A + B)ᵢⱼ = Aᵢⱼ + Bᵢⱼ
  - **Where used**: Gradient accumulation, bias addition in neural networks

    ```py
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    result = A + B  # [[6, 8], [10, 12]]
    ```

- **Matrix Multiplication**: Dot product of rows and columns
  - **Formula**: (AB)ᵢⱼ = Σₖ(Aᵢₖ × Bₖⱼ)
  - **Where used**: Neural network forward propagation, transformations, PCA

    ```py
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    result = A @ B  # or np.dot(A, B)
    ```

- **Matrix Rank**: Maximum number of linearly independent rows/columns
  - **Formula**: rank(A) = number of linearly independent rows (or columns)
  - **Where used**: Determining data dimensionality, checking multicollinearity

    ```py
    A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    rank = np.linalg.matrix_rank(A)  # Result: 2 (not full rank)
    ```

[⬆️ Go to Context](#context)

### Core Matrix Properties and Decompositions

- **Eigenvalues and Eigenvectors**: Special scalars and vectors where Av = λv
  - **Formula**: A**v** = λ**v**, where det(A - λI) = 0
  - **Where used**: PCA, dimensionality reduction, stability analysis, PageRank

    ```py
    A = np.array([[4, 2], [1, 3]])
    eigenvalues, eigenvectors = np.linalg.eig(A)
    ```

- **Determinant**: Scalar value describing matrix properties
  - **Formula**: det(A) = Σ(±a₁ᵢ₁a₂ᵢ₂...aₙᵢₙ) (for 2×2: ad - bc)
  - **Where used**: Checking invertibility, volume scaling, feature importance

    ```py
    det = np.linalg.det(A)
    ```

- **Singular Value Decomposition (SVD)**: Factorization into three matrices
  - **Formula**: A = UΣVᵀ (U: left singular vectors, Σ: singular values, V: right singular vectors)
  - **Where used**: Dimensionality reduction, recommendation systems, image compression

    ```py
    U, S, Vt = np.linalg.svd(matrix)
    ```

- **Trace**: Sum of diagonal elements
  - **Formula**: tr(A) = Σᵢ aᵢᵢ
  - **Where used**: Matrix derivatives, regularization, PCA

    ```py
    trace = np.trace(A)
    ```

[⬆️ Go to Context](#context)

## **Statistics & Probability**

- **Mean (Average)**: Central tendency measure
  - **Formula**: μ = (Σxᵢ) / n
  - **Where used**: Data summarization, feature normalization

    ```py
    data = np.array([1, 2, 3, 4, 5])
    mean = np.mean(data)
    ```

- **Median**: Middle value in sorted data
  - **Formula**: Middle value when n is odd; average of two middle values when n is even
  - **Where used**: Robust central tendency (less affected by outliers)

    ```py
    median = np.median(data)
    ```

- **Mode**: Most frequently occurring value
  - **Formula**: Value with highest frequency
  - **Where used**: Categorical data analysis, imputation

    ```py
    from scipy import stats
    mode = stats.mode(data)
    ```

- **Variance**: Average squared deviation from mean
  - **Formula**: σ² = Σ(xᵢ - μ)² / n (population), s² = Σ(xᵢ - x̄)² / (n-1) (sample)
  - **Where used**: Measuring data spread, feature scaling, model evaluation

    ```py
    variance = np.var(data)  # Population variance
    variance_sample = np.var(data, ddof=1)  # Sample variance
    ```

- **Standard Deviation**: Square root of variance
  - **Formula**: σ = √(σ²), s = √(s²)
  - **Where used**: Feature scaling, confidence intervals, anomaly detection

    ```py
    std_dev = np.std(data)
    ```

- **Covariance**: Measure of joint variability between two variables
  - **Formula**: cov(X,Y) = Σ(xᵢ - x̄)(yᵢ - ȳ) / (n-1)
  - **Where used**: Feature relationship analysis, PCA

    ```py
    data1 = np.array([1, 2, 3, 4, 5])
    data2 = np.array([2, 4, 5, 4, 5])
    cov_matrix = np.cov(data1, data2)
    ```

- **Correlation (Pearson)**: Normalized covariance
  - **Formula**: ρ(X,Y) = cov(X,Y) / (σₓ × σᵧ), range: [-1, 1]
  - **Where used**: Feature selection, multicollinearity detection

    ```py
    correlation = np.corrcoef(data1, data2)
    ```

- **Normal (Gaussian) Distribution**: Bell-shaped probability distribution
  - **Formula**: f(x) = (1/(σ√(2π))) × e^(-(x-μ)²/(2σ²))
  - **Where used**: Statistical inference, data generation, assumptions in models

    ```py
    from scipy import stats
    normal_dist = stats.norm(loc=0, scale=1)
    sample = normal_dist.rvs(size=1000)
    ```

- **Binomial Distribution**: Discrete probability of k successes in n trials
  - **Formula**: P(X=k) = C(n,k) × p^k × (1-p)^(n-k), where C(n,k) = n!/(k!(n-k)!)
  - **Where used**: A/B testing, binary classification evaluation

    ```py
    binomial_dist = stats.binom(n=10, p=0.5)
    prob = binomial_dist.pmf(k=5)
    ```

- **Poisson Distribution**: Discrete probability of k events in fixed interval
  - **Formula**: P(X=k) = (λ^k × e^(-λ)) / k!, where λ is the average rate
  - **Where used**: Counting events, rare event modeling

    ```py
    poisson_dist = stats.poisson(mu=3)
    prob = poisson_dist.pmf(k=2)
    ```

- **Bayes' Theorem**: Update probability based on new evidence
  - **Formula**: P(A|B) = [P(B|A) × P(A)] / P(B)
  - **Where used**: Naive Bayes classifier, probabilistic inference

    ```py
    # P(Disease|Positive) = P(Positive|Disease) * P(Disease) / P(Positive)
    posterior = (0.95 * 0.01) / 0.05  # = 0.19
    ```

- **Conditional Probability**: Probability of A given B has occurred
  - **Formula**: P(A|B) = P(A ∩ B) / P(B)
  - **Where used**: Decision trees, probabilistic graphical models

    ```py
    p_a_and_b = 0.3
    p_b = 0.5
    p_a_given_b = p_a_and_b / p_b
    ```

- **Expected Value (Mean of distribution)**: Long-run average
  - **Formula**: E[X] = Σ(xᵢ × P(xᵢ)) (discrete), ∫(x × f(x))dx (continuous)
  - **Where used**: Decision theory, risk assessment

    ```py
    values = np.array([1, 2, 3, 4, 5])
    probabilities = np.array([0.1, 0.2, 0.3, 0.2, 0.2])
    expected_value = np.sum(values * probabilities)
    ```

[⬆️ Go to Context](#context)

# **Day 43 - Mathematics For Data Science 02**

## **Calculus**

### Differential Calculus

- **Derivative**: Instantaneous rate of change
  - **Formula**: f'(x) = lim(h→0) [f(x+h) - f(x)] / h
  - **Where used**: Gradient descent, backpropagation, optimization

    ```py
    # Numerical derivative
    def derivative(f, x, h=1e-5):
        return (f(x + h) - f(x - h)) / (2 * h)

    f = lambda x: x**2
    df = derivative(f, 3)  # ≈ 6
    ```

- **Common Derivatives**: Frequently used derivative rules
  - **Formulas**:
    - d/dx(x^n) = nx^(n-1) (Power Rule)
    - d/dx(e^x) = e^x
    - d/dx(ln(x)) = 1/x
    - d/dx(sin(x)) = cos(x)
    - d/dx(cos(x)) = -sin(x)
    - d/dx(tan(x)) = sec²(x)
    - d/dx(c) = 0 (constant)
  - **Where used**: Building blocks for complex derivatives

    ```py
    import sympy as sp
    x = sp.Symbol('x')
    f = x**3 + sp.exp(x) + sp.sin(x)
    df = sp.diff(f, x)  # 3*x**2 + exp(x) + cos(x)
    ```

- **Chain Rule**: Derivative of composite functions
  - **Formula**: d/dx[f(g(x))] = f'(g(x)) × g'(x)
  - **Where used**: Backpropagation in neural networks, nested function derivatives

    ```py
    # If y = (2x + 1)^3, then dy/dx = 3(2x+1)^2 × 2 = 6(2x+1)^2
    x = sp.Symbol('x')
    y = (2*x + 1)**3
    dy_dx = sp.diff(y, x)  # 6*(2*x + 1)**2
    ```

- **Product Rule**: Derivative of product of functions
  - **Formula**: d/dx[f(x)g(x)] = f'(x)g(x) + f(x)g'(x)
  - **Where used**: Complex derivative calculations, physics equations

    ```py
    # d/dx[x^2 * sin(x)] = 2x*sin(x) + x^2*cos(x)
    x = sp.Symbol('x')
    f = x**2 * sp.sin(x)
    df = sp.diff(f, x)
    ```

- **Quotient Rule**: Derivative of quotient of functions
  - **Formula**: d/dx[f(x)/g(x)] = [f'(x)g(x) - f(x)g'(x)] / [g(x)]²
  - **Where used**: Complex derivative calculations, rate problems

    ```py
    # d/dx[x^2 / (x+1)]
    x = sp.Symbol('x')
    f = x**2 / (x + 1)
    df = sp.diff(f, x)
    ```

- **Partial Derivative**: Derivative with respect to one variable
  - **Formula**: ∂f/∂x = lim(h→0) [f(x+h, y) - f(x, y)] / h
  - **Where used**: Multivariable optimization, neural network gradients

    ```py
    import torch
    x = torch.tensor([2.0, 3.0], requires_grad=True)
    y = x[0]**2 + x[1]**3
    y.backward()
    print(x.grad)  # [4.0, 27.0] - partial derivatives
    ```

- **Gradient**: Vector of all partial derivatives
  - **Formula**: ∇f = [∂f/∂x₁, ∂f/∂x₂, ..., ∂f/∂xₙ]
  - **Where used**: Optimization algorithms, direction of steepest ascent

    ```py
    def f(x):
        return x[0]**2 + 2*x[1]**2

    # Gradient: [2x, 4y]
    x = np.array([1.0, 2.0])
    gradient = np.array([2*x[0], 4*x[1]])  # [2.0, 8.0]
    ```

- **Directional Derivative**: Rate of change in a specific direction
  - **Formula**: D_u f = ∇f · u (where u is unit vector)
  - **Where used**: Finding rate of change in any direction, optimization

    ```py
    gradient = np.array([2.0, 8.0])
    direction = np.array([1, 1]) / np.sqrt(2)  # Unit vector
    directional_deriv = np.dot(gradient, direction)
    ```

- **Higher-Order Derivatives**: Second, third, etc. derivatives
  - **Formula**: f''(x), f'''(x), ..., f^(n)(x)
  - **Where used**: Convexity analysis, Newton's method, Taylor series

    ```py
    x = sp.Symbol('x')
    f = x**4 + 2*x**2
    f_prime = sp.diff(f, x)      # First derivative
    f_double_prime = sp.diff(f, x, 2)  # Second derivative
    ```

- **Hessian Matrix**: Matrix of second-order partial derivatives
  - **Formula**: H = [[∂²f/∂x₁², ∂²f/∂x₁∂x₂], [∂²f/∂x₂∂x₁, ∂²f/∂x₂²]]
  - **Where used**: Newton's method, convexity testing, optimization

    ```py
    from scipy.optimize import rosen, rosen_hess
    x = np.array([1.0, 1.0])
    hessian = rosen_hess(x)
    ```

- **Jacobian Matrix**: Matrix of first-order partial derivatives
  - **Formula**: J = [[∂f₁/∂x₁, ∂f₁/∂x₂], [∂f₂/∂x₁, ∂f₂/∂x₂]]
  - **Where used**: Neural networks, coordinate transformations, optimization

    ```py
    import torch
    x = torch.tensor([[1.0, 2.0]], requires_grad=True)
    y = torch.stack([x[0,0]**2, x[0,1]**3])
    jacobian = torch.autograd.functional.jacobian(lambda x: y, x)
    ```

[⬆️ Go to Context](#context)

### Integral Calculus

- **Indefinite Integral (Antiderivative)**: Reverse of differentiation
  - **Formula**: ∫f(x)dx = F(x) + C, where F'(x) = f(x)
  - **Where used**: Probability calculations, area under curve (AUC)

    ```py
    import sympy as sp
    x = sp.Symbol('x')
    f = x**2
    integral = sp.integrate(f, x)  # x**3/3 + C
    ```

- **Common Integrals**: Frequently used integration formulas
  - **Formulas**:
    - ∫x^n dx = x^(n+1)/(n+1) + C (n ≠ -1)
    - ∫1/x dx = ln|x| + C
    - ∫e^x dx = e^x + C
    - ∫sin(x) dx = -cos(x) + C
    - ∫cos(x) dx = sin(x) + C
  - **Where used**: Probability density functions, cumulative distributions

    ```py
    x = sp.Symbol('x')
    integrals = {
        'power': sp.integrate(x**3, x),      # x**4/4
        'exponential': sp.integrate(sp.exp(x), x),  # exp(x)
        'sine': sp.integrate(sp.sin(x), x)   # -cos(x)
    }
    ```

- **Definite Integral**: Area under curve between bounds
  - **Formula**: ∫ₐᵇ f(x)dx = F(b) - F(a)
  - **Where used**: Expected value calculations, probability distributions

    ```py
    from scipy import integrate
    # Integrate x^2 from 0 to 1
    result, error = integrate.quad(lambda x: x**2, 0, 1)  # = 1/3
    ```

- **Fundamental Theorem of Calculus**: Links differentiation and integration
  - **Formula**:
    - Part 1: d/dx[∫ₐˣ f(t)dt] = f(x)
    - Part 2: ∫ₐᵇ f(x)dx = F(b) - F(a), where F'(x) = f(x)
  - **Where used**: Theoretical foundation for calculus operations

    ```py
    # Area under normal distribution curve
    from scipy.stats import norm
    area = norm.cdf(1) - norm.cdf(-1)  # ~68% within 1 std dev
    ```

- **Riemann Sum**: Approximation of definite integral
  - **Formula**: ∫ₐᵇ f(x)dx ≈ Σᵢ f(xᵢ)Δx, where Δx = (b-a)/n
  - **Where used**: Numerical integration, understanding integration concept

    ```py
    def riemann_sum(f, a, b, n=1000):
        dx = (b - a) / n
        x = np.linspace(a, b, n)
        return np.sum(f(x) * dx)

    result = riemann_sum(lambda x: x**2, 0, 1)  # ≈ 0.333
    ```

- **Integration by Parts**: Product integral rule
  - **Formula**: ∫u dv = uv - ∫v du
  - **Where used**: Complex integration problems, probability calculations

    ```py
    # ∫x*e^x dx
    x = sp.Symbol('x')
    f = x * sp.exp(x)
    integral = sp.integrate(f, x)  # x*exp(x) - exp(x)
    ```

- **Integration by Substitution**: Chain rule in reverse
  - **Formula**: ∫f(g(x))g'(x)dx = ∫f(u)du, where u = g(x)
  - **Where used**: Simplifying complex integrals, probability transformations

    ```py
    # ∫2x*cos(x^2) dx, let u = x^2
    x = sp.Symbol('x')
    f = 2*x * sp.cos(x**2)
    integral = sp.integrate(f, x)  # sin(x**2)
    ```

- **Double Integral**: Integration over 2D region
  - **Formula**: ∬ᴿ f(x,y) dA = ∫ₐᵇ ∫_c^d f(x,y) dy dx
  - **Where used**: Joint probability distributions, volume calculations

    ```py
    from scipy import integrate
    # ∫∫ xy dxdy over [0,1]×[0,1]
    def f(y, x):
        return x * y
    result = integrate.dblquad(f, 0, 1, 0, 1)  # = 0.25
    ```

- **Numerical Integration**: Approximating integrals computationally
  - **Methods**: Trapezoidal rule, Simpson's rule, Monte Carlo
  - **Where used**: When analytical solutions don't exist

    ```py
    from scipy.integrate import trapz, simps
    x = np.linspace(0, 1, 100)
    y = x**2
    area_trapz = trapz(y, x)  # Trapezoidal rule
    area_simps = simps(y, x)  # Simpson's rule
    ```

[⬆️ Go to Context](#context)

## **Optimization**

- **Gradient Descent**: Iterative optimization to find minimum
  - **Formula**: θₜ₊₁ = θₜ - α∇J(θₜ), where α is learning rate
  - **Where used**: Training machine learning models

    ```py
    learning_rate = 0.01
    theta = np.random.randn(2)
    for epoch in range(100):
        gradient = compute_gradient(loss, theta)
        theta = theta - learning_rate * gradient
    ```

- **Stochastic Gradient Descent (SGD)**: Gradient descent with single samples
  - **Formula**: θₜ₊₁ = θₜ - α∇J(θₜ; xᵢ, yᵢ)
  - **Where used**: Large-scale machine learning, deep learning

    ```py
    for epoch in range(epochs):
        for x_i, y_i in zip(X, y):
            gradient = compute_gradient(loss, theta, x_i, y_i)
            theta = theta - learning_rate * gradient
    ```

- **Mini-Batch Gradient Descent**: Gradient descent with batches
  - **Formula**: θₜ₊₁ = θₜ - α∇J(θₜ; X_batch, y_batch)
  - **Where used**: Deep learning (balances speed and accuracy)

    ```py
    batch_size = 32
    for epoch in range(epochs):
        for i in range(0, len(X), batch_size):
            X_batch = X[i:i+batch_size]
            y_batch = y[i:i+batch_size]
            gradient = compute_gradient(loss, theta, X_batch, y_batch)
            theta = theta - learning_rate * gradient
    ```

- **Learning Rate**: Step size in gradient descent
  - **Formula**: α (typically between 0.001 and 0.1)
  - **Where used**: Controlling convergence speed and stability

    ```py
    # Adaptive learning rate (decay)
    initial_lr = 0.1
    decay_rate = 0.95
    lr = initial_lr * (decay_rate ** epoch)
    ```

- **Momentum**: Accelerated gradient descent using past gradients
  - **Formula**: vₜ = βvₜ₋₁ + ∇J(θₜ), θₜ₊₁ = θₜ - αvₜ
  - **Where used**: Faster convergence, escaping local minima

    ```py
    velocity = np.zeros_like(theta)
    beta = 0.9
    for epoch in range(epochs):
        gradient = compute_gradient(loss, theta)
        velocity = beta * velocity + gradient
        theta = theta - learning_rate * velocity
    ```

- **Adam Optimizer**: Adaptive learning rates with momentum
  - **Formula**: mₜ = β₁mₜ₋₁ + (1-β₁)∇J, vₜ = β₂vₜ₋₁ + (1-β₂)(∇J)²
  - **Where used**: Most popular optimizer for deep learning

    ```py
    from torch.optim import Adam
    optimizer = Adam(model.parameters(), lr=0.001, betas=(0.9, 0.999))
    ```

- **Convex Function**: Function with single global minimum
  - **Formula**: f(λx + (1-λ)y) ≤ λf(x) + (1-λ)f(y) for λ ∈ [0,1]
  - **Where used**: Guaranteeing optimization convergence

    ```py
    # Example: f(x) = x^2 is convex
    # Loss functions in linear regression, logistic regression are convex
    ```

- **Loss Function (Cost Function)**: Measure of model error
  - **Formulas**:
    - MSE: L = (1/n)Σ(yᵢ - ŷᵢ)²
    - Cross-Entropy: L = -(1/n)Σ[yᵢlog(ŷᵢ) + (1-yᵢ)log(1-ŷᵢ)]
  - **Where used**: Model training objective

    ```py
    # Mean Squared Error
    mse = np.mean((y_true - y_pred)**2)

    # Binary Cross-Entropy
    bce = -np.mean(y_true*np.log(y_pred) + (1-y_true)*np.log(1-y_pred))
    ```

[⬆️ Go to Context](#context)
