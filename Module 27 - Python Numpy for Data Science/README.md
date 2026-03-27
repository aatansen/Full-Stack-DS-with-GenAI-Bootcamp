# **Context**

- [**Context**](#context)
- [**Day 32 - Numpy for Data Science**](#day-32---numpy-for-data-science)
  - [**NumPy Setup**](#numpy-setup)
  - [**Creating NumPy Arrays**](#creating-numpy-arrays)
  - [**Array Attributes**](#array-attributes)
  - [**Common Array Creation Methods**](#common-array-creation-methods)
  - [**Random Numbers**](#random-numbers)
  - [**Array Indexing**](#array-indexing)
  - [**Array Slicing**](#array-slicing)
  - [**Boolean Indexing**](#boolean-indexing)
  - [**Array Operations (Vectorization)**](#array-operations-vectorization)
  - [**Mathematical Functions**](#mathematical-functions)
  - [**Reshaping Arrays**](#reshaping-arrays)
  - [**Broadcasting**](#broadcasting)
  - [**Copy vs View**](#copy-vs-view)
  - [**Sorting \& Searching**](#sorting--searching)
  - [**Stacking \& Splitting**](#stacking--splitting)
  - [**Linear Algebra Using Numpy**](#linear-algebra-using-numpy)
  - [**File I/O with NumPy**](#file-io-with-numpy)
  - [**NumPy vs Python Lists**](#numpy-vs-python-lists)
  - [**When to Use NumPy**](#when-to-use-numpy)

# [**Day 32 - Numpy for Data Science**](./Day%2032%20-%20Numpy%20for%20Data%20Science/)

## **NumPy Setup**

- [Numpy docs](https://numpy.org/doc/stable/user/absolute_beginners.html)
- Install [numpy](https://pypi.org/project/numpy/), [ipykernel](https://pypi.org/project/ipykernel/)
- Import NumPy

  ```py
  import numpy as np
  ```

- Check version

  ```py
  np.__version__
  ```

[⬆️ Go to Context](#context)

## **Creating NumPy Arrays**

- From Python list

  ```py
  arr = np.array([1, 2, 3, 4])
  ```

- 2D array (matrix)

  ```py
  arr2d = np.array([
      [1, 2, 3],
      [4, 5, 6]
  ])
  ```

- Check array type

  ```py
  type(arr)
  ```

[⬆️ Go to Context](#context)

## **Array Attributes**

- Shape (rows, columns)

  ```py
  arr2d.shape
  ```

- Number of dimensions

  ```py
  arr2d.ndim
  ```

- Total elements

  ```py
  arr2d.size
  ```

- Data type

  ```py
  arr2d.dtype
  ```

[⬆️ Go to Context](#context)

## **Common Array Creation Methods**

- Zeros

  ```py
  np.zeros((3, 4))
  ```

- Ones

  ```py
  np.ones((2, 2))
  ```

- Identity matrix

  ```py
  np.eye(3)
  ```

- Range (like Python range)

  ```py
  np.arange(0, 10, 2)
  ```

- Evenly spaced numbers

  ```py
  np.linspace(0, 1, 5)
  ```

[⬆️ Go to Context](#context)

## **Random Numbers**

- Random floats (0 to 1)

  ```py
  np.random.rand(3, 2)
  ```

- Random integers

  ```py
  np.random.randint(1, 10, size=(2, 3))
  ```

- Normal distribution

  ```py
  np.random.randn(3, 3)
  ```

- Set random seed (important for ML)

  ```py
  np.random.seed(42)
  ```

[⬆️ Go to Context](#context)

## **Array Indexing**

- 1D indexing

  ```py
  arr = np.array([10, 20, 30, 40])
  arr[0]
  arr[-1]
  ```

- 2D indexing

  ```py
  arr2d[0, 1]   # row 0, col 1
  ```

- Row slicing

  ```py
  arr2d[1]
  ```

- Column slicing

  ```py
  arr2d[:, 1]
  ```

[⬆️ Go to Context](#context)

## **Array Slicing**

- Basic slicing

  ```py
  arr[1:4]
  ```

- 2D slicing

  ```py
  arr2d[:2, :2]
  ```

- Step slicing

  ```py
  arr[::2]
  ```

[⬆️ Go to Context](#context)

## **Boolean Indexing**

- Condition-based selection

  ```py
  arr = np.array([5, 10, 15, 20])
  arr[arr > 10]
  ```

- Modify values using condition

  ```py
  arr[arr < 10] = 0
  ```

[⬆️ Go to Context](#context)

## **Array Operations (Vectorization)**

- Element-wise operations

  ```py
  arr + 10
  arr * 2
  arr ** 2
  ```

- Array-to-array operations

  ```py
  a = np.array([1, 2, 3])
  b = np.array([4, 5, 6])

  a + b
  a * b
  ```

- Why NumPy is fast

  - No Python loops
  - Uses C under the hood

[⬆️ Go to Context](#context)

## **Mathematical Functions**

- Basic math

  ```py
  np.sum(arr)
  np.mean(arr)
  np.min(arr)
  np.max(arr)
  np.std(arr)
  ```

- Axis-wise operations

  ```py
  np.sum(arr2d, axis=0)  # column-wise
  np.sum(arr2d, axis=1)  # row-wise
  ```

[⬆️ Go to Context](#context)

## **Reshaping Arrays**

- Change shape

  ```py
  arr = np.arange(12)
  arr.reshape(3, 4)
  ```

- Flatten array

  ```py
  arr.flatten()
  ```

- Automatic dimension inference

  ```py
  arr.reshape(2, -1)
  ```

[⬆️ Go to Context](#context)

## **Broadcasting**

- Add scalar to matrix

  ```py
  arr2d + 10
  ```

- Broadcasting rules (simple idea)

  - Smaller array stretches to match shape
  - Dimensions must be compatible

- Example

  ```py
  mat = np.array([[1, 2, 3]])
  mat + np.array([10, 20, 30])
  ```

[⬆️ Go to Context](#context)

## **Copy vs View**

- View (shares memory)

  ```py
  a = np.array([1, 2, 3])
  b = a[:]
  b[0] = 99
  ```

- Copy (independent)

  ```py
  c = a.copy()
  c[0] = 100
  ```

[⬆️ Go to Context](#context)

## **Sorting & Searching**

- Sort array

  ```py
  np.sort(arr)
  ```

- Argsort (indices)

  ```py
  np.argsort(arr)
  ```

- Where condition

  ```py
  np.where(arr > 10)
  ```

[⬆️ Go to Context](#context)

## **Stacking & Splitting**

- Vertical stack

  ```py
  np.vstack([a, b])
  ```

- Horizontal stack

  ```py
  np.hstack([a, b])
  ```

- Split array

  ```py
  np.split(arr, 3)
  ```

[⬆️ Go to Context](#context)

## **Linear Algebra Using Numpy**

- Matrix multiplication

  ```py
  A = np.array([[1, 2], [3, 4]])
  B = np.array([[5, 6], [7, 8]])

  A @ B
  ```

- Transpose

  ```py
  A.T
  ```

- Determinant

  ```py
  np.linalg.det(A)
  ```

- Inverse

  ```py
  np.linalg.inv(A)
  ```

[⬆️ Go to Context](#context)

## **File I/O with NumPy**

- Save array

  ```py
  np.save("data.npy", arr)
  ```

- Load array

  ```py
  np.load("data.npy")
  ```

- Load CSV

  ```py
  np.loadtxt("data.csv", delimiter=",")
  ```

[⬆️ Go to Context](#context)

## **NumPy vs Python Lists**

- Faster numerical computation
- Less memory usage
- Vectorized operations
- Foundation of Pandas, SciPy, Scikit-learn, TensorFlow

[⬆️ Go to Context](#context)

## **When to Use NumPy**

- Numerical computation
- Matrix & vector math
- Data preprocessing
- Machine learning foundations
- Scientific computing

[⬆️ Go to Context](#context)
