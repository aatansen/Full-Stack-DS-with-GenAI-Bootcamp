# **Context**

- [**Context**](#context)
- [**Day 47 - Feature Engineering**](#day-47---feature-engineering)
  - [**What is GIGO?**](#what-is-gigo)
  - [**Machine Learning Workflow Pipeline**](#machine-learning-workflow-pipeline)
  - [**Feature Engineering**](#feature-engineering)
    - [1. Feature Transformation](#1-feature-transformation)
      - [Missing Value Handling (Imputation)](#missing-value-handling-imputation)
      - [Handling Categorical Features (Encoding)](#handling-categorical-features-encoding)
      - [Outlier Detection \& Handling](#outlier-detection--handling)
      - [Feature Scaling](#feature-scaling)
      - [Mathematical Transforms (Fixing Skewness)](#mathematical-transforms-fixing-skewness)
    - [2. Feature Construction](#2-feature-construction)
      - [Numerical Operations](#numerical-operations)
      - [Date / Time Engineering](#date--time-engineering)
      - [Binning (Discretization)](#binning-discretization)
      - [Polynomial \& Interaction Features](#polynomial--interaction-features)
    - [3. Feature Selection](#3-feature-selection)
      - [Filter Methods (Statistical — Model-Independent)](#filter-methods-statistical--model-independent)
      - [Wrapper Methods (Model-Driven — Iterative)](#wrapper-methods-model-driven--iterative)
      - [Embedded Methods (Selection During Training)](#embedded-methods-selection-during-training)
    - [4. Feature Extraction](#4-feature-extraction)
      - [PCA (Principal Component Analysis)](#pca-principal-component-analysis)
      - [LDA (Linear Discriminant Analysis)](#lda-linear-discriminant-analysis)
      - [t-SNE \& UMAP (Visualization)](#t-sne--umap-visualization)
      - [Truncated SVD (Sparse Data)](#truncated-svd-sparse-data)
      - [Word Embeddings (NLP)](#word-embeddings-nlp)
    - [5. Feature Engineering Pipeline](#5-feature-engineering-pipeline)
      - [When To Use Which Technique](#when-to-use-which-technique)
- [**Day 48 - MinMaxScaling, Handling Categorical Data, Label Encoding**](#day-48---minmaxscaling-handling-categorical-data-label-encoding)
  - [**MinMaxScaling**](#minmaxscaling)
  - [**Handling Categorical Data**](#handling-categorical-data)
    - [Ordinal Encoding](#ordinal-encoding)
    - [One-Hot Encoding (Nominal)](#one-hot-encoding-nominal)
    - [Label Encoding (Mostly for Target Variable)](#label-encoding-mostly-for-target-variable)
    - [Label Encoding vs Ordinal Encoding](#label-encoding-vs-ordinal-encoding)
      - [Label Encoding(No order)](#label-encodingno-order)
      - [Ordinal Encoding(ordered)](#ordinal-encodingordered)
    - [Dummy Variable Trap](#dummy-variable-trap)
    - [Target Encoding](#target-encoding)
    - [Frequency Encoding](#frequency-encoding)
  - [**Pipeline-Ready Preprocessing Setup**](#pipeline-ready-preprocessing-setup)
- [**Day 49 - Train Test Split, Use Of Column Transformer In Sklearn**](#day-49---train-test-split-use-of-column-transformer-in-sklearn)
  - [**Train Test Split**](#train-test-split)
    - [Test Split Using Scikit-learn](#test-split-using-scikit-learn)
    - [Train Test Split Explanation](#train-test-split-explanation)
    - [Train Model After Split](#train-model-after-split)
    - [When NOT to Shuffle](#when-not-to-shuffle)
  - [**Column Transformer in Scikit-learn**](#column-transformer-in-scikit-learn)
    - [Why ColumnTransformer is Needed](#why-columntransformer-is-needed)
    - [Column Transformer](#column-transformer)
    - [After ColumnTransformer](#after-columntransformer)
    - [ColumnTransformer + Model](#columntransformer--model)
- [**Day 50 - EDA Project - Visa Data**](#day-50---eda-project---visa-data)
  - [**Visa Data EDA**](#visa-data-eda)
- [**Day 51 - Machine Learning Pipelines**](#day-51---machine-learning-pipelines)
  - [**Titanic training without pipeline**](#titanic-training-without-pipeline)
  - [**Predict without pipeline**](#predict-without-pipeline)
  - [**Titanic Training Using Pipeline**](#titanic-training-using-pipeline)
  - [**Predict Using Pipeline**](#predict-using-pipeline)
    - [What Happens Internally?](#what-happens-internally)
  - [**Manual vs Pipeline Prediction**](#manual-vs-pipeline-prediction)
- [**Day 52 - Data Transformation Techniques**](#day-52---data-transformation-techniques)
  - [**Function Transformer**](#function-transformer)
    - [Log Transformation](#log-transformation)
    - [Reciprocal Transformation](#reciprocal-transformation)
    - [Square Transformation](#square-transformation)
    - [Square Root Transformation](#square-root-transformation)
  - [**Function Transformer Comparison**](#function-transformer-comparison)
  - [**Power Transformer**](#power-transformer)
    - [Box-Cox Transformation](#box-cox-transformation)
    - [Yeo Johnson Transformation](#yeo-johnson-transformation)
  - [**Power Transformer Comparison**](#power-transformer-comparison)
- [**Day 53 - Outlier Detection and Removal**](#day-53---outlier-detection-and-removal)
  - [**Outlier Detection**](#outlier-detection)
  - [**Outlier Removal**](#outlier-removal)
    - [Trimming](#trimming)
    - [Capping](#capping)

# [**Day 47 - Feature Engineering**](./Day%2047%20-%20Feature%20Engineering/)

## **What is GIGO?**

- **GIGO (Garbage In, Garbage Out)**
  - If your input data is poor → your output will be poor
  - No matter how advanced your algorithm is

- Poor ML model + Good quality data → Often Good (or Decent)
  - Linear Regression
  - Logistic Regression
  - Decision Tree

  Can perform surprisingly well **if the data is clean, relevant, and well-structured**.

  Cause:
  - Clear signal
  - Low noise
  - Proper features
  - Fewer inconsistencies

- Powerful ML model + Bad quality data → Bad
  - XGBoost
  - Random Forest
  - Neural Networks
  - Deep Learning

  But if your data has:
  - Missing values
  - Wrong labels
  - Noise
  - Data leakage
  - Bias
  - Outliers not handled

  Then the model will just learn garbage patterns.

  > A deep neural network is just a very powerful pattern memorizer. If the pattern is wrong, it memorizes wrong.

ML models learn patterns from:

- Distribution
- Feature relationships
- Target consistency

If those are corrupted:

- The model optimizes the wrong objective
- Overfits noise
- Produces unstable predictions

- What Actually Matters More?

In production ML:

- 70–80% effort → Data cleaning & feature engineering
- 10–20% → Model selection
- 5–10% → Hyperparameter tuning

> Data quality > Model complexity

[⬆️ Go to Context](#context)

## **Machine Learning Workflow Pipeline**

- Simple pipeline

  ```mermaid
  flowchart LR
      A[📥 Data Loading]:::load -->
      B[🔎 Exploratory Data Analysis]:::eda -->
      C[🛠 Feature Engineering]:::fe -->
      D[🤖 Model Training]:::train -->
      E[📊 Evaluation]:::eval -->
      F[🚀 Deployment]:::deploy

      classDef load fill:#4FC3F7,color:#000,stroke:#0288D1,stroke-width:2px;
      classDef eda fill:#81C784,color:#000,stroke:#2E7D32,stroke-width:2px;
      classDef fe fill:#FFD54F,color:#000,stroke:#F57F17,stroke-width:2px;
      classDef train fill:#BA68C8,color:#000,stroke:#6A1B9A,stroke-width:2px;
      classDef eval fill:#FF8A65,color:#000,stroke:#BF360C,stroke-width:2px;
      classDef deploy fill:#A1887F,color:#000,stroke:#4E342E,stroke-width:2px;
  ```

- Production pipeline

  ```mermaid
  flowchart LR
      A[📥 Data Collection]:::data -->
      B[🔎 EDA]:::eda -->
      C[🛠 Feature Engineering]:::fe -->
      D[🤖 Model Training]:::train -->
      E[📊 Evaluation]:::eval -->
      F{Good Enough?}:::decision

      F -- ❌ No --> B
      F -- ✅ Yes --> G[🚀 Deploy]:::deploy
      G --> H[📡 Monitor Performance]:::monitor
      H --> I{Drift Detected?}:::decision
      I -- ⚠️ Yes --> A
      I -- ✅ No --> H

      classDef data fill:#4FC3F7,stroke:#0288D1,stroke-width:2px,color:#000;
      classDef eda fill:#81C784,stroke:#2E7D32,stroke-width:2px,color:#000;
      classDef fe fill:#FFD54F,stroke:#F57F17,stroke-width:2px,color:#000;
      classDef train fill:#BA68C8,stroke:#6A1B9A,stroke-width:2px,color:#000;
      classDef eval fill:#FF8A65,stroke:#BF360C,stroke-width:2px,color:#000;
      classDef deploy fill:#A1887F,stroke:#4E342E,stroke-width:2px,color:#000;
      classDef monitor fill:#90A4AE,stroke:#37474F,stroke-width:2px,color:#000;
      classDef decision fill:#EF5350,stroke:#B71C1C,stroke-width:2px,color:#fff;
  ```

## **Feature Engineering**

- Feature engineering is the process of using domain knowledge to extract features from raw data. These features can be used to improve the performance of machine learning algorithms.

[⬆️ Go to Context](#context)

### 1. Feature Transformation

- Changing the scale, distribution, or representation of existing features without creating new ones. Makes data more suitable for modeling and helps algorithms converge faster or perform better.
- *Clean data and reshape its distribution so algorithms can learn from it effectively.*

---

#### Missing Value Handling (Imputation)

Replacing missing data with meaningful values, e.g., mean, median, mode, or predictions.

- **Mean Imputation** — Replace missing values with the column mean. Best for normally distributed data.
- **Median Imputation** — More robust than mean; use when outliers are present.
- **Mode Imputation** — Used for categorical columns.
- **KNN Imputer** — Fills missing values using the K nearest neighbors. Slower but more accurate.
- **Iterative Imputer (MICE)** — Models each feature as a function of others iteratively.

  ```py
  import pandas as pd
  import numpy as np
  from sklearn.impute import SimpleImputer, KNNImputer

  df = pd.DataFrame({'age': [25, np.nan, 35, np.nan, 45], 'income': [50000, 60000, np.nan, 80000, 90000]})

  # Mean / Median / Mode
  imputer = SimpleImputer(strategy='mean')  # or 'median', 'most_frequent'
  df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

  # KNN Imputer
  knn_imputer = KNNImputer(n_neighbors=2)
  df_knn = pd.DataFrame(knn_imputer.fit_transform(df), columns=df.columns)
  ```

---

[⬆️ Go to Context](#context)

#### Handling Categorical Features (Encoding)

Converting categories to numbers, e.g., one-hot encoding, label encoding, or target encoding.

- **One-Hot Encoding (Nominal)** — Creates binary columns for each category. Use when there is no natural order (e.g., Color: Red, Blue, Green).
- **Label Encoding (Ordinal)** — Maps categories to integers. Use when order matters (e.g., Low=0, Medium=1, High=2).
- **Target Encoding** — Replaces category with the mean of the target variable. Useful for high-cardinality features.
- **Binary Encoding** — Converts categories to binary representation. Efficient for high-cardinality.
- **Frequency Encoding** — Replaces category with its frequency in the dataset.

  ```py
  import pandas as pd
  from sklearn.preprocessing import LabelEncoder, OrdinalEncoder
  from sklearn.preprocessing import OneHotEncoder

  df = pd.DataFrame({'color': ['Red', 'Blue', 'Green', 'Blue'], 'size': ['Low', 'Medium', 'High', 'Low']})

  # One-Hot Encoding (Nominal)
  df_ohe = pd.get_dummies(df, columns=['color'])

  # Label / Ordinal Encoding (Ordinal)
  le = OrdinalEncoder(categories=[['Low', 'Medium', 'High']])
  df['size_encoded'] = le.fit_transform(df[['size']])

  # Target Encoding (manual)
  target = [1, 0, 1, 0]
  df['color_target_enc'] = df['color'].map(df.groupby('color').apply(lambda x: pd.Series(target).iloc[x.index].mean()))
  ```

---

[⬆️ Go to Context](#context)

#### Outlier Detection & Handling

Identifying extreme values and treating them (removing, capping, or transforming) to avoid skewed models.

- **Z-Score** — Flags values more than N standard deviations from the mean. Assumes normal distribution.
- **IQR (Interquartile Range)** — Flags values below Q1−1.5×IQR or above Q3+1.5×IQR. More robust.
- **Isolation Forest** — Tree-based anomaly detection. Works well in high dimensions.
- **Capping (Winsorization)** — Clips extreme values to a defined percentile instead of removing them.

  ```py
  import numpy as np
  import pandas as pd
  from scipy import stats

  df = pd.DataFrame({'salary': [30000, 35000, 40000, 42000, 500000]})

  # Z-Score method
  z_scores = np.abs(stats.zscore(df['salary']))
  df_clean = df[z_scores < 3]

  # IQR method
  Q1 = df['salary'].quantile(0.25)
  Q3 = df['salary'].quantile(0.75)
  IQR = Q3 - Q1
  df_iqr = df[(df['salary'] >= Q1 - 1.5 * IQR) & (df['salary'] <= Q3 + 1.5 * IQR)]

  # Capping / Winsorization
  lower = df['salary'].quantile(0.05)
  upper = df['salary'].quantile(0.95)
  df['salary_capped'] = df['salary'].clip(lower, upper)
  ```

---

[⬆️ Go to Context](#context)

#### Feature Scaling

Standardizing or normalizing numeric features so all features contribute equally (e.g., Min-Max Scaling, Standardization).

- **Standardization (Z-score)** — Centers data to mean=0, std=1. Best for algorithms that assume normality (e.g., SVM, PCA, Logistic Regression).
- **Min-Max Normalization** — Scales data to [0, 1]. Best for neural networks and distance-based models.
- **Robust Scaler** — Uses median and IQR instead of mean and std. Best when outliers are present.
- **MaxAbs Scaler** — Scales to [-1, 1]. Useful for sparse data.

  ```py
  from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler

  X = [[10], [20], [30], [1000]]  # 1000 is an outlier

  # Standardization
  std = StandardScaler().fit_transform(X)

  # Normalization
  minmax = MinMaxScaler().fit_transform(X)

  # Robust (handles outliers better)
  robust = RobustScaler().fit_transform(X)
  ```

  > A detail Standardization -> [Feature_Scaling_Standardization.ipynb](./Day%2047%20-%20Feature%20Engineering/Feature_Scaling_Standardization.ipynb)

---

[⬆️ Go to Context](#context)

#### Mathematical Transforms (Fixing Skewness)

Applying log, square root, or Box-Cox transformations to reduce skewness and improve model performance.

- **Log Transform** — Compresses large values; great for right-skewed data (e.g., income, prices). Requires all values > 0.
- **Square Root Transform** — Milder version of log. Works on zero values.
- **Box-Cox Transform** — Finds the optimal power transformation automatically. Requires all values > 0.
- **Yeo-Johnson** — Like Box-Cox but also handles zero and negative values.

  ```py
  import numpy as np
  import pandas as pd
  from scipy.stats import boxcox, yeojohnson
  from sklearn.preprocessing import PowerTransformer

  data = pd.Series([1, 2, 5, 10, 100, 1000, 10000])

  log_transformed    = np.log1p(data)           # log(x+1) handles zeros
  sqrt_transformed   = np.sqrt(data)

  boxcox_data, _     = boxcox(data + 1)         # scipy boxcox
  yj_data, _         = yeojohnson(data)         # handles negatives

  # Sklearn auto-select
  pt = PowerTransformer(method='yeo-johnson')
  pt_data = pt.fit_transform(data.values.reshape(-1, 1))
  ```

---

[⬆️ Go to Context](#context)

### 2. Feature Construction

- Creating new features from existing data to capture additional information or patterns. Enhance model performance by providing more meaningful inputs.
- *Manually engineer new features that encode domain knowledge and improve model signal.*

---

#### Numerical Operations

Creating new features by combining existing ones, e.g., `Total_Sales = Price × Quantity`.

- **Ratios** — Capture relationships between two features (e.g., Debt-to-Income, Price-per-sqft).
- **Aggregates** — Sum, mean, min, max across related features (e.g., Total_Spent).
- **Differences** — Useful in time-series (e.g., Revenue_Change = Revenue_Now - Revenue_Last).

  ```py
  df = pd.DataFrame({'debt': [5000, 10000, 15000], 'income': [50000, 60000, 70000],
                    'spent_food': [200, 300, 250], 'spent_rent': [1000, 1200, 900]})

  df['debt_to_income']  = df['debt'] / df['income']
  df['total_spent']     = df['spent_food'] + df['spent_rent']
  df['income_per_debt'] = df['income'] / (df['debt'] + 1)  # +1 to avoid division by zero
  ```

---

[⬆️ Go to Context](#context)

#### Date / Time Engineering

Extracting useful info from dates/times, e.g., day of week, month, quarter, time difference, season.

- **Cyclical Encoding** — Encodes hour, month, day as sin/cos to preserve circular nature.
- **Time Since** — Days since last purchase, account creation, etc.
- **Is_Holiday / Is_Weekend** — Binary flags for special periods.
- **Part of Day** — Morning, Afternoon, Evening, Night.

  ```py
  import pandas as pd
  import numpy as np

  df = pd.DataFrame({'timestamp': pd.to_datetime(['2024-01-15 09:30:00', '2024-07-04 18:45:00', '2024-12-25 00:15:00'])})

  df['hour']       = df['timestamp'].dt.hour
  df['day_of_week']= df['timestamp'].dt.dayofweek    # 0=Monday
  df['month']      = df['timestamp'].dt.month
  df['is_weekend'] = df['day_of_week'].isin([5, 6]).astype(int)

  # Cyclical encoding for hour (preserves 23→0 continuity)
  df['hour_sin']   = np.sin(2 * np.pi * df['hour'] / 24)
  df['hour_cos']   = np.cos(2 * np.pi * df['hour'] / 24)

  # Days since a reference date
  df['days_since_epoch'] = (df['timestamp'] - pd.Timestamp('2020-01-01')).dt.days
  ```

---

[⬆️ Go to Context](#context)

#### Binning (Discretization)

Converting continuous variables into discrete bins, e.g., age → age groups.

- **Equal-Width Bins** — Splits range into N equal intervals. Sensitive to outliers.
- **Equal-Frequency Bins (Quantile)** — Each bin has the same number of samples.
- **Custom Bins** — Domain-driven thresholds (e.g., age groups: Child, Adult, Senior).

  ```py
  import pandas as pd

  df = pd.DataFrame({'age': [5, 15, 25, 35, 45, 60, 75, 85]})

  # Equal-width bins
  df['age_bin_width']    = pd.cut(df['age'], bins=4)

  # Equal-frequency bins
  df['age_bin_quantile'] = pd.qcut(df['age'], q=4, labels=['Q1', 'Q2', 'Q3', 'Q4'])

  # Custom bins
  bins   = [0, 12, 17, 35, 60, 100]
  labels = ['Child', 'Teen', 'Young Adult', 'Middle-Aged', 'Senior']
  df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels)
  ```

---

[⬆️ Go to Context](#context)

#### Polynomial & Interaction Features

Creating combinations of features to capture nonlinear relationships, e.g., `x1 * x2`, `x1^2`.

- **Polynomial Features** — Creates x², x³, and cross-products (x₁·x₂) to capture non-linear patterns.
- **Manual Interactions** — Multiply or combine specific features based on domain knowledge.

  ```py
  from sklearn.preprocessing import PolynomialFeatures
  import pandas as pd

  df = pd.DataFrame({'x1': [1, 2, 3], 'x2': [4, 5, 6]})

  poly = PolynomialFeatures(degree=2, include_bias=False)
  poly_features = poly.fit_transform(df)

  # Feature names: ['x1', 'x2', 'x1^2', 'x1 x2', 'x2^2']
  poly_df = pd.DataFrame(poly_features, columns=poly.get_feature_names_out(['x1', 'x2']))
  ```

---

[⬆️ Go to Context](#context)

### 3. Feature Selection

- Choosing the most relevant features and removing redundant or noisy ones. Reduce model complexity, avoid overfitting, and improve interpretability.
- *Remove noise and redundancy to prevent overfitting and reduce training time.*

---

#### Filter Methods (Statistical — Model-Independent)

Selecting features using statistics like correlation, chi-square, mutual information, without involving a model.

- **Pearson Correlation** — Measures linear relationship between numerical features. Remove features with |corr| > 0.9 (multicollinearity).
- **Spearman Correlation** — Non-parametric version; works for monotonic relationships.
- **Chi-Square Test** — Tests dependence between categorical features and a categorical target.
- **ANOVA F-Test** — Tests if means of a numerical feature differ across target classes.
- **Mutual Information** — Measures how much a feature reduces uncertainty about the target.
- **Variance Threshold** — Removes features with near-zero variance (they carry no signal).

  ```py
  from sklearn.feature_selection import chi2, f_classif, mutual_info_classif, VarianceThreshold
  from sklearn.datasets import load_iris
  import pandas as pd
  import seaborn as sns
  import matplotlib.pyplot as plt

  X, y = load_iris(return_X_y=True)
  feature_names = load_iris().feature_names

  # Variance Threshold
  vt = VarianceThreshold(threshold=0.1)
  X_var = vt.fit_transform(X)

  # ANOVA F-Test
  f_scores, p_values = f_classif(X, y)
  print(pd.Series(f_scores, index=feature_names).sort_values(ascending=False))

  # Mutual Information
  mi_scores = mutual_info_classif(X, y)
  print(pd.Series(mi_scores, index=feature_names).sort_values(ascending=False))

  # Correlation Heatmap
  df = pd.DataFrame(X, columns=feature_names)
  sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
  plt.show()
  ```

---

[⬆️ Go to Context](#context)

#### Wrapper Methods (Model-Driven — Iterative)

Using a predictive model to evaluate combinations of features and select the best subset, e.g., recursive feature elimination (RFE).

- **Forward Selection** — Start with no features; add the one that improves score most, repeat.
- **Backward Elimination** — Start with all features; remove the weakest one, repeat.
- **Recursive Feature Elimination (RFE)** — Fits model repeatedly, pruning the least important feature each time.
- **Sequential Feature Selector (SFS)** — Sklearn implementation of forward/backward selection.

  ```py
  from sklearn.feature_selection import RFE, SequentialFeatureSelector
  from sklearn.linear_model import LogisticRegression
  from sklearn.datasets import load_iris

  X, y = load_iris(return_X_y=True)
  model = LogisticRegression(max_iter=1000)

  # RFE — keep top 2 features
  rfe = RFE(estimator=model, n_features_to_select=2)
  rfe.fit(X, y)
  print("Selected:", rfe.support_)
  print("Ranking:", rfe.ranking_)

  # Sequential Forward Selection
  sfs = SequentialFeatureSelector(model, n_features_to_select=2, direction='forward')
  sfs.fit(X, y)
  print("SFS Selected:", sfs.get_support())
  ```

---

[⬆️ Go to Context](#context)

#### Embedded Methods (Selection During Training)

Feature selection happens during model training, e.g., Lasso, Ridge, or tree-based feature importance.

- **Lasso (L1) Regularization** — Shrinks some coefficients to exactly zero, effectively removing those features.
- **Ridge (L2) Regularization** — Shrinks all coefficients but rarely zeros them out (not ideal for selection).
- **Elastic Net** — Combines L1 and L2; good balance for correlated features.
- **Tree-Based Feature Importance** — Random Forest and XGBoost rank features by how much they reduce impurity.
- **Permutation Importance** — Measures performance drop when a feature is randomly shuffled.

  ```py
  from sklearn.linear_model import LassoCV
  from sklearn.ensemble import RandomForestClassifier
  from sklearn.inspection import permutation_importance
  from sklearn.datasets import load_iris
  import pandas as pd

  X, y = load_iris(return_X_y=True)
  feature_names = load_iris().feature_names

  # Lasso (L1) — zero coefficients = removed features
  lasso = LassoCV(cv=5).fit(X, y)
  print(pd.Series(lasso.coef_, index=feature_names))

  # Random Forest Importance
  rf = RandomForestClassifier(n_estimators=100, random_state=42)
  rf.fit(X, y)
  importances = pd.Series(rf.feature_importances_, index=feature_names).sort_values(ascending=False)
  print(importances)

  # Permutation Importance
  result = permutation_importance(rf, X, y, n_repeats=10, random_state=42)
  perm = pd.Series(result.importances_mean, index=feature_names).sort_values(ascending=False)
  print(perm)
  ```

---

[⬆️ Go to Context](#context)

### 4. Feature Extraction

- Transforming the original features into a new set of features that better capture the underlying structure of the data. Unlike feature construction, it often reduces dimensionality. Reduce complexity, remove redundancy, and capture the most important information in fewer features.
- *Reduce dimensionality by projecting original features into a new, compact representation.*

---

#### PCA (Principal Component Analysis)

Reduces dimensionality by projecting data into components capturing the most variance.

- Transforms correlated features into uncorrelated **principal components**.
- Each component captures the maximum remaining variance.
- Does not use class labels — purely unsupervised.
- Best used when features are highly correlated and dimensionality is high.

  ```py
  from sklearn.decomposition import PCA
  from sklearn.preprocessing import StandardScaler
  from sklearn.datasets import load_iris
  import pandas as pd

  X, y = load_iris(return_X_y=True)
  X_scaled = StandardScaler().fit_transform(X)

  pca = PCA(n_components=2)
  X_pca = pca.fit_transform(X_scaled)

  print("Explained Variance Ratio:", pca.explained_variance_ratio_)
  print("Total Variance Retained:", pca.explained_variance_ratio_.sum())
  ```

---

[⬆️ Go to Context](#context)

#### LDA (Linear Discriminant Analysis)

Creates features that maximize separation between classes.

- Finds axes that **maximize class separability**.
- Supervised — uses class labels.
- Max components = (n_classes − 1).
- Better than PCA for classification tasks.

  ```py
  from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
  from sklearn.datasets import load_iris

  X, y = load_iris(return_X_y=True)

  lda = LinearDiscriminantAnalysis(n_components=2)
  X_lda = lda.fit_transform(X, y)

  print("Explained Variance Ratio:", lda.explained_variance_ratio_)
  ```

---

[⬆️ Go to Context](#context)

#### t-SNE & UMAP (Visualization)

Non-linear techniques for visualizing high-dimensional data in 2D/3D.

- **t-SNE** — Reveals local cluster structure in 2D/3D. Slow on large datasets. Not used for training — only visualization.
- **UMAP** — Faster than t-SNE, better preserves global structure. Can be used for dimensionality reduction before training.

  ```py
  from sklearn.manifold import TSNE
  import umap  # pip install umap-learn
  from sklearn.datasets import load_digits
  import matplotlib.pyplot as plt

  X, y = load_digits(return_X_y=True)

  # t-SNE
  X_tsne = TSNE(n_components=2, random_state=42, perplexity=30).fit_transform(X)

  # UMAP
  reducer = umap.UMAP(n_components=2, random_state=42)
  X_umap = reducer.fit_transform(X)

  fig, axes = plt.subplots(1, 2, figsize=(14, 5))
  axes[0].scatter(X_tsne[:, 0], X_tsne[:, 1], c=y, cmap='tab10', s=5)
  axes[0].set_title('t-SNE')
  axes[1].scatter(X_umap[:, 0], X_umap[:, 1], c=y, cmap='tab10', s=5)
  axes[1].set_title('UMAP')
  plt.show()
  ```

---

[⬆️ Go to Context](#context)

#### Truncated SVD (Sparse Data)

Dimensionality reduction for sparse matrices, e.g., TF-IDF matrices in text.

- Like PCA but works directly on **sparse matrices** (e.g., TF-IDF vectors).
- Standard in NLP pipelines (also called LSA — Latent Semantic Analysis).

  ```py
  from sklearn.decomposition import TruncatedSVD
  from sklearn.feature_extraction.text import TfidfVectorizer

  corpus = ["machine learning is great", "deep learning is powerful", "NLP is a branch of AI"]

  tfidf = TfidfVectorizer()
  X_sparse = tfidf.fit_transform(corpus)

  svd = TruncatedSVD(n_components=2)
  X_reduced = svd.fit_transform(X_sparse)
  print("Reduced shape:", X_reduced.shape)
  ```

---

[⬆️ Go to Context](#context)

#### Word Embeddings (NLP)

Represent words as vectors capturing semantic meaning, e.g., Word2Vec, GloVe, BERT embeddings.

- **Word2Vec** — Learns dense word vectors from co-occurrence patterns. Captures semantic similarity.
- **GloVe** — Global log-bilinear model; pre-trained on massive corpora.
- **FastText** — Handles out-of-vocabulary words by using character n-grams.
- **BERT / Sentence Transformers** — Contextual embeddings; the same word gets different vectors in different sentences.

  ```py
  # Word2Vec with Gensim
  from gensim.models import Word2Vec

  corpus = [["machine", "learning", "is", "great"], ["deep", "learning", "is", "powerful"]]
  model = Word2Vec(sentences=corpus, vector_size=100, window=5, min_count=1, workers=4)
  print(model.wv['learning'])  # 100-dim vector

  # Sentence Transformers (BERT-based)
  from sentence_transformers import SentenceTransformer  # pip install sentence-transformers

  smodel = SentenceTransformer('all-MiniLM-L6-v2')
  embeddings = smodel.encode(["Machine learning is fascinating", "Deep learning is powerful"])
  print(embeddings.shape)  # (2, 384)
  ```

---

[⬆️ Go to Context](#context)

### 5. Feature Engineering Pipeline

- *Combine all steps into a reproducible, production-ready sklearn pipeline.*

  ```py
  from sklearn.pipeline import Pipeline
  from sklearn.compose import ColumnTransformer
  from sklearn.preprocessing import StandardScaler, OneHotEncoder
  from sklearn.impute import SimpleImputer
  from sklearn.decomposition import PCA
  from sklearn.ensemble import RandomForestClassifier
  import pandas as pd
  import numpy as np

  # Sample data
  X = pd.DataFrame({
      'age':    [25, np.nan, 35, 45],
      'income': [50000, 60000, np.nan, 80000],
      'city':   ['NYC', 'LA', 'NYC', 'Chicago']
  })
  y = [0, 1, 0, 1]

  num_features = ['age', 'income']
  cat_features = ['city']

  num_pipeline = Pipeline([
      ('imputer', SimpleImputer(strategy='median')),
      ('scaler',  StandardScaler()),
  ])

  cat_pipeline = Pipeline([
      ('imputer', SimpleImputer(strategy='most_frequent')),
      ('encoder', OneHotEncoder(handle_unknown='ignore')),
  ])

  preprocessor = ColumnTransformer([
      ('num', num_pipeline, num_features),
      ('cat', cat_pipeline, cat_features),
  ])

  full_pipeline = Pipeline([
      ('preprocessor', preprocessor),
      ('pca',          PCA(n_components=3)),
      ('classifier',   RandomForestClassifier(n_estimators=100, random_state=42)),
  ])

  full_pipeline.fit(X, y)
  print("Pipeline trained successfully.")
  ```

---

[⬆️ Go to Context](#context)

#### When To Use Which Technique

| Goal                     | Technique                  | When to Use                       |
| ------------------------ | -------------------------- | --------------------------------- |
| Fill missing values      | Mean/Median/KNN Imputer    | Always — models cannot handle NaN |
| Encode categories        | One-Hot / Ordinal          | Nominal → OHE; Ordinal → Label    |
| Remove outlier effect    | IQR Capping, Robust Scaler | Skewed distributions              |
| Normalize range          | Min-Max Scaler             | Neural networks, KNN              |
| Fix skewed data          | Log / Box-Cox              | Right-skewed features like income |
| Reduce multicollinearity | PCA, Drop correlated       | Correlation > 0.9                 |
| Select top features      | RFE, Lasso, RF Importance  | High-dimensional data             |
| Visualize clusters       | t-SNE, UMAP                | Exploratory analysis              |
| NLP features             | TF-IDF + SVD, BERT         | Text classification, similarity   |

[⬆️ Go to Context](#context)

# [**Day 48 - MinMaxScaling, Handling Categorical Data, Label Encoding**](./Day%2048%20-%20MinMaxScaling,%20Handling%20Categorical%20Data,%20Label%20Encoding/)

## **MinMaxScaling**

- Scales numerical features into a fixed range (usually **0 → 1**)
- Preserves original data distribution
- Sensitive to outliers
- Commonly used in Neural Networks and distance-based algorithms

```math
X_{\text{scaled}} = \frac{X - X_{\min}}{X_{\max} - X_{\min}}
```

- **When to Use**
  - Feature values have different ranges
  - Algorithms depend on distance
  - Deep Learning models

  ```py
  from sklearn.preprocessing import MinMaxScaler
  import pandas as pd

  data = pd.DataFrame({
      "age": [18, 25, 40, 60]
  })

  scaler = MinMaxScaler()
  data_scaled = scaler.fit_transform(data)

  print(data_scaled)
  ```

[⬆️ Go to Context](#context)

## **Handling Categorical Data**

- Machine learning models work with numbers, not text
- Categorical values must be converted into numerical form
- Encoding method depends on category type

- **Types**
  - **Ordinal Encoding** → ordered categories
  - **One-Hot Encoding** → unordered (nominal) categories
  - **Label Encoding** → mainly for target labels

[⬆️ Go to Context](#context)

### Ordinal Encoding

- Converts categories into integers based on **defined order**
- Used when categories have **natural ranking**
- Model understands relative importance

- **Example Categories**
  - Low < Medium < High
  - Beginner < Intermediate < Expert

  ```py
  from sklearn.preprocessing import OrdinalEncoder
  import pandas as pd

  data = pd.DataFrame({
      "size": ["Small", "Medium", "Large"]
  })

  encoder = OrdinalEncoder(
      categories=[["Small", "Medium", "Large"]]
  )

  encoded = encoder.fit_transform(data)

  print(encoded)
  ```

> [!NOTE]
>
> - Only use when order exists
> - Wrong usage introduces false relationships

[⬆️ Go to Context](#context)

### One-Hot Encoding (Nominal)

- Creates binary columns for each category
- No ranking relationship introduced
- Safest encoding for unordered categories

- **Example Categories**
  - Red, Blue, Green
  - Dhaka, Chittagong, Sylhet

  ```py
  from sklearn.preprocessing import OneHotEncoder
  import pandas as pd

  data = pd.DataFrame({
      "color": ["Red", "Blue", "Green"]
  })

  encoder = OneHotEncoder(sparse_output=False)
  encoded = encoder.fit_transform(data)

  print(encoded)
  ```

- **Using pandas shortcut**

  ```py
  pd.get_dummies(data["color"])
  ```

> [!NOTE]
>
> - Creates many columns for large categories
> - May increase dimensionality

[⬆️ Go to Context](#context)

### Label Encoding (Mostly for Target Variable)

- Assigns integer labels automatically
- Does **not** represent true ordering
- Commonly used for encoding **target (y)**

  ```py
  from sklearn.preprocessing import LabelEncoder

  labels = ["Cat", "Dog", "Bird"]

  encoder = LabelEncoder()
  encoded = encoder.fit_transform(labels)

  print(encoded)
  ```

> [!NOTE]
>
> - Not recommended for input features
> - Model may assume incorrect ranking

- Data Type And Encoding

  | Data Type           | Encoding         |
  | ------------------- | ---------------- |
  | Ordinal categorical | Ordinal Encoding |
  | Nominal categorical | One-Hot Encoding |
  | Target labels       | Label Encoding   |

[⬆️ Go to Context](#context)

### Label Encoding vs Ordinal Encoding

- Both convert categories into numbers
- Often confused in interviews
- Key difference → **meaning of numbers**

[⬆️ Go to Context](#context)

#### Label Encoding(No order)

- Assigns arbitrary integer values
- No order awareness
- Mainly used for **target (y) labels**

  ```py
  from sklearn.preprocessing import LabelEncoder

  data = ["Cat", "Dog", "Bird"]

  encoder = LabelEncoder()
  encoded = encoder.fit_transform(data)

  print(encoded)
  ```

  ```sh
  Bird=0, Cat=1, Dog=2
  ```

- Numbers are random
- Model may wrongly assume ranking

[⬆️ Go to Context](#context)

#### Ordinal Encoding(ordered)

- Used when categories have logical order
- Order is explicitly defined

  ```py
  from sklearn.preprocessing import OrdinalEncoder

  data = [["Low"], ["Medium"], ["High"]]

  encoder = OrdinalEncoder(
      categories=[["Low", "Medium", "High"]]
  )

  print(encoder.fit_transform(data))
  ```

- Label Encoding ≠ Ordinal Encoding
- Label Encoding → arbitrary mapping
- Ordinal Encoding → meaningful ranking

- **Rule**
  - Target column → Label Encoding
  - Ordered feature → Ordinal Encoding
  - Unordered feature → One-Hot Encoding

[⬆️ Go to Context](#context)

### Dummy Variable Trap

- Happens during One-Hot Encoding
- One column becomes predictable from others
- Causes **multicollinearity**

  ```sh
  Male → [1,0]
  Female → [0,1]
  ```

  > If Male is known → Female automatically known.

- Problem
  - Linear Regression models become unstable
  - Coefficients become unreliable

- Solution
  - Drop one encoded column

- **Using pandas**

  ```py
  pd.get_dummies(data["gender"], drop_first=True)
  ```

- **Using sklearn**

  ```py
  from sklearn.preprocessing import OneHotEncoder

  encoder = OneHotEncoder(drop="first")
  ```

[⬆️ Go to Context](#context)

### Target Encoding

- Replace category using target mean
- Useful for high-cardinality features
- Common in competitions (Kaggle)

  ```sh
  Category → Mean(target)
  ```

  ```py
  import pandas as pd

  data = pd.DataFrame({
      "city": ["A", "A", "B", "B"],
      "price": [100, 120, 200, 220]
  })

  target_mean = data.groupby("city")["price"].mean()

  data["city_encoded"] = data["city"].map(target_mean)

  print(data)
  ```

[⬆️ Go to Context](#context)

### Frequency Encoding

- Replace category with occurrence frequency
- Keeps dataset compact
- Good for large categorical sets

  ```py
  freq = data["city"].value_counts(normalize=True)

  data["city_freq"] = data["city"].map(freq)
  ```

[⬆️ Go to Context](#context)

## **Pipeline-Ready Preprocessing Setup**

- Automates preprocessing
- Prevents data leakage
- Production-ready workflow

- Step 1 — Separate Columns

  ```py
  num_features = ["age", "salary"]
  cat_features = ["city", "gender"]
  ```

- Step 2 — Create Transformers

  ```py
  from sklearn.preprocessing import StandardScaler, OneHotEncoder
  from sklearn.compose import ColumnTransformer

  preprocessor = ColumnTransformer(
      transformers=[
          ("num", StandardScaler(), num_features),
          ("cat", OneHotEncoder(drop="first"), cat_features)
      ]
  )
  ```

- Step 3 — Full ML Pipeline

  ```py
  from sklearn.pipeline import Pipeline
  from sklearn.linear_model import LogisticRegression

  pipeline = Pipeline([
      ("preprocessing", preprocessor),
      ("model", LogisticRegression())
  ])

  pipeline.fit(X_train, y_train)
  ```

[⬆️ Go to Context](#context)

# [**Day 49 - Train Test Split, Use Of Column Transformer In Sklearn**](./Day%2049%20-%20Train%20Test%20Split,%20Use%20Of%20Column%20Transformer%20In%20Sklearn/)

## **Train Test Split**

- Train Test Split is used to evaluate how well a machine learning model performs on **unseen data**
- Dataset is divided into two parts:
  - **Training set** → used to train the model
  - **Testing set** → used to evaluate performance
- Prevents **overfitting** (model memorizing data instead of learning)

- Common split ratios:
  - 80% Training — 20% Testing
  - 70% Training — 30% Testing
  - 90% Training — 10% Testing (large datasets)

[⬆️ Go to Context](#context)

### Test Split Using Scikit-learn

- Import required function:

  ```py
  from sklearn.model_selection import train_test_split
  ```

- Example

  ```py
  import pandas as pd

  data = {
      "hours": [1,2,3,4,5,6,7,8],
      "score": [10,20,30,40,50,60,70,80]
  }

  df = pd.DataFrame(data)

  X = df[["hours"]]   # Features
  y = df["score"]     # Target
  ```

- Perform Train Test Split

  ```py
  from sklearn.model_selection import train_test_split

  X_train, X_test, y_train, y_test = train_test_split(
      X,
      y,
      test_size=0.2,
      random_state=42
  )
  ```

[⬆️ Go to Context](#context)

### Train Test Split Explanation

- Parameter Explanation

  - `test_size=0.2`

    - 20% data used for testing

  - `random_state=42`

    - Ensures same split every run
    - Important for reproducibility

- Check Split Size

  ```py
  print(X_train.shape)
  print(X_test.shape)
  ```

  ```sh
  (6, 1)
  (2, 1)
  ```

- Visual Understanding

  ```sh
  Full Dataset
  │
  ├── Training Data (80%)
  │       Model Learning
  │
  └── Testing Data (20%)
          Model Evaluation
  ```

[⬆️ Go to Context](#context)

### Train Model After Split

```py
from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

[⬆️ Go to Context](#context)

### When NOT to Shuffle

- Time-based datasets:
  - Stock prices
  - Weather data
  - Sales forecasting

  ```py
  train_test_split(X, y, shuffle=False)
  ```

[⬆️ Go to Context](#context)

## **Column Transformer in Scikit-learn**

- `ColumnTransformer` allows applying **different preprocessing steps** to different columns
- Useful when dataset contains:
  - Numerical features
  - Categorical features
  - Mixed data types
- Keeps preprocessing clean and automated

[⬆️ Go to Context](#context)

### Why ColumnTransformer is Needed

Real datasets usually contain:

- Numerical data → needs scaling
- Categorical data → needs encoding

Without ColumnTransformer:

- Manual preprocessing becomes messy
- Hard to maintain pipelines
- Risk of preprocessing mistakes

ColumnTransformer solves this by handling everything **in one step**

- Example dataset:

  | Age | Salary | City       |
  | --- | ------ | ---------- |
  | 25  | 30000  | Dhaka      |
  | 30  | 50000  | Chittagong |
  | 35  | 70000  | Dhaka      |

Required preprocessing:

- Age, Salary → Scaling
- City → One-Hot Encoding

[⬆️ Go to Context](#context)

### Column Transformer

  ```py
  from sklearn.compose import ColumnTransformer
  from sklearn.preprocessing import StandardScaler, OneHotEncoder
  ```

  ```py
  import pandas as pd

  data = {
      "age": [25, 30, 35],
      "salary": [30000, 50000, 70000],
      "city": ["Dhaka", "Chittagong", "Dhaka"]
  }

  df = pd.DataFrame(data)

  X = df
  ```

- Define Column Groups

  ```py
  num_cols = ["age", "salary"]
  cat_cols = ["city"]
  ```

- Create ColumnTransformer

  ```py
  preprocessor = ColumnTransformer(
      transformers=[
          ("num", StandardScaler(), num_cols),
          ("cat", OneHotEncoder(), cat_cols)
      ]
  )
  ```

- Each tuple contains:
  - Name → `"num"` or `"cat"`
  - Transformer → preprocessing method
  - Columns → target columns

- Structure:

  ```sh
  (name, transformer, columns)
  ```

- Apply Transformation

  ```py
  X_transformed = preprocessor.fit_transform(X)
  ```

  ```py
  print(X_transformed)
  ```

- Result:
  - Numerical columns scaled
  - Categorical column converted into encoded vectors
  - Combined into one final feature matrix

[⬆️ Go to Context](#context)

### After ColumnTransformer

- Convert Output to DataFrame

  ```py
  import pandas as pd

  pd.DataFrame(
      X_transformed,
      columns=preprocessor.get_feature_names_out()
  )
  ```

- Using with Train Test Split

  ```py
  from sklearn.model_selection import train_test_split

  X_train, X_test = train_test_split(X, test_size=0.2, random_state=42)

  X_train = preprocessor.fit_transform(X_train)
  X_test = preprocessor.transform(X_test)
  ```

  - `fit_transform()` → training data
  - `transform()` → test data

[⬆️ Go to Context](#context)

### ColumnTransformer + Model

  ```py
  from sklearn.pipeline import Pipeline
  from sklearn.linear_model import LinearRegression

  pipeline = Pipeline([
      ("preprocessing", preprocessor),
      ("model", LinearRegression())
  ])

  pipeline.fit(X_train, y_train)
  ```

[⬆️ Go to Context](#context)

# [**Day 50 - EDA Project - Visa Data**](./Day%2050%20-%20EDA%20Project%20-%20Visa%20Data/)

## **Visa Data EDA**

- Dataset: [EasyVisa_Dataset](https://www.kaggle.com/datasets/moro23/easyvisa-dataset)
- Full EDA on Visa Data: [EDA_Visa_data.ipynb](./Day%2050%20-%20EDA%20Project%20-%20Visa%20Data/EDA_Visa_data.ipynb)

---

- For FE:
  - Missing value - No
  - Categorical handler - Yes
  - Outlier - Yes
  - Imbalance - Yes
  - Duplicate - No
  - Drop any column - Yes
  - Scaling - Yes
  - Transformation - Yes

[⬆️ Go to Context](#context)

# [**Day 51 - Machine Learning Pipelines**](./Day%2051%20-%20Machine%20Learning%20Pipelines/)

## **Titanic training without pipeline**

- **Step 0 – Import Libraries**
  - `numpy` → numerical operations
  - `pandas` → data handling
  - `sklearn` → preprocessing, model, evaluation
  - `pickle` → save trained objects

    ```py
    import numpy as np
    import pandas as pd

    from sklearn.model_selection import train_test_split
    from sklearn.impute import SimpleImputer
    from sklearn.preprocessing import OneHotEncoder
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.metrics import accuracy_score

    import pickle
    ```

[⬆️ Go to Context](#context)

- **Step 1 – Load Dataset**

  - Read CSV file
  - Quick inspection using `.head()`

    ```py
    df = pd.read_csv('train.csv')
    df.head()
    ```

[⬆️ Go to Context](#context)

- **Step 2 – Drop Unnecessary Columns**

  These columns are not useful for prediction:

  - PassengerId → unique ID
  - Name → too many unique values
  - Ticket → high cardinality
  - Cabin → too many missing values

    ```py
    df.drop(columns=['PassengerId','Name','Ticket','Cabin'], inplace=True)
    df.head()
    ```

[⬆️ Go to Context](#context)

- **Step 3 – Train Test Split**

  - Separate features (X) and target (y)
  - 80% training, 20% testing
  - `random_state=42` for reproducibility

    ```py
    X_train, X_test, y_train, y_test = train_test_split(
        df.drop(columns=['Survived']),
        df['Survived'],
        test_size=0.2,
        random_state=42
    )
    ```

[⬆️ Go to Context](#context)

- **Step 4 – Check Missing Values**

  ```py
  df.isnull().sum()
  ```

  - Important columns with missing values:
    - Age
    - Embarked

[⬆️ Go to Context](#context)

- **Step 5 – Imputation (Handling Missing Values)**
  - Strategy
    - Age → Mean (default)
    - Embarked → Most frequent value

  - Create Imputers

    ```py
    si_age = SimpleImputer()
    si_embarked = SimpleImputer(strategy='most_frequent')
    ```

  - Fit on Training Data (Very Important Rule)
    - Always fit on training data
    - Only transform test data

      ```py
      X_train_age = si_age.fit_transform(X_train[['Age']])
      X_test_age = si_age.transform(X_test[['Age']])

      X_train_embarked = si_embarked.fit_transform(X_train[['Embarked']])
      X_test_embarked = si_embarked.transform(X_test[['Embarked']])
      ```

[⬆️ Go to Context](#context)

- **Step 6 – One Hot Encoding**

  Categorical columns:

  - Sex
  - Embarked

- Create Encoders

  ```py
  ohe_sex = OneHotEncoder(sparse=False, handle_unknown='ignore')
  ohe_embarked = OneHotEncoder(sparse=False, handle_unknown='ignore')
  ```

- Fit & Transform

  ```py
  X_train_sex = ohe_sex.fit_transform(X_train[['Sex']])
  X_test_sex = ohe_sex.transform(X_test[['Sex']])

  X_train_embarked = ohe_embarked.fit_transform(X_train_embarked)
  X_test_embarked = ohe_embarked.transform(X_test_embarked)
  ```

  - `handle_unknown='ignore'` prevents error if unseen category appears
  - `sparse=False` gives normal numpy array

[⬆️ Go to Context](#context)

- **Step 7 – Remove Original Columns**

  Drop already processed columns:

  - Sex
  - Age
  - Embarked

    ```py
    X_train_rem = X_train.drop(columns=['Sex','Age','Embarked'])
    X_test_rem = X_test.drop(columns=['Sex','Age','Embarked'])
    ```

[⬆️ Go to Context](#context)

- **Step 8 – Concatenate All Features**

  Combine:

  - Remaining numeric columns
  - Imputed Age
  - Encoded Sex
  - Encoded Embarked

    ```py
    X_train_transformed = np.concatenate(
        (X_train_rem, X_train_age, X_train_sex, X_train_embarked),
        axis=1
    )

    X_test_transformed = np.concatenate(
        (X_test_rem, X_test_age, X_test_sex, X_test_embarked),
        axis=1
    )
    ```

- Check shape:

  ```py
  X_train_transformed.shape
  X_test_transformed.shape
  ```

[⬆️ Go to Context](#context)

- **Step 9 – Train Model**

  Using Decision Tree Classifier:

    ```py
    clf = DecisionTreeClassifier()
    clf.fit(X_train_transformed, y_train)
    ```

[⬆️ Go to Context](#context)

- **Step 10 – Prediction**

  ```py
  y_pred = clf.predict(X_test_transformed)
  ```

- **Step 11 – Evaluation**

  Accuracy Score:

  ```py
  accuracy_score(y_test, y_pred)
  ```

  - Measures percentage of correct predictions
  - Range → 0 to 1

[⬆️ Go to Context](#context)

- **Step 12 – Save Model & Encoders**

  Very important for deployment.

    ```py
    pickle.dump(ohe_sex, open('models/ohe_sex.pkl','wb'))
    pickle.dump(ohe_embarked, open('models/ohe_embarked.pkl','wb'))
    pickle.dump(clf, open('models/clf.pkl','wb'))
    ```

  Also save `si_age`,`si_embarked` for imputers:

    ```py
    pickle.dump(si_age, open('models/si_age.pkl','wb'))
    pickle.dump(si_embarked, open('models/si_embarked.pkl','wb'))
    ```

[⬆️ Go to Context](#context)

## **Predict without pipeline**

- **Step 1 – Import Libraries**

  ```py
  import pickle
  import numpy as np
  ```

- **Step 2 – Load Saved Objects**
  - OneHotEncoder for Sex
  - OneHotEncoder for Embarked
  - Trained Decision Tree model

    ```py
    ohe_sex = pickle.load(open('models/ohe_sex.pkl','rb'))
    ohe_embarked = pickle.load(open('models/ohe_embarked.pkl','rb'))
    clf = pickle.load(open('models/clf.pkl','rb'))
    ```

- Load imputers:

  ```py
  si_age = pickle.load(open('models/si_age.pkl','rb'))
  si_embarked = pickle.load(open('models/si_embarked.pkl','rb'))
  ```

[⬆️ Go to Context](#context)

- **Step 3 – Create User Input**

  Feature order must match training:

  - Pclass
  - Sex
  - Age
  - SibSp
  - Parch
  - Fare
  - Embarked

    ```py
    # Pclass / Sex / Age / SibSp / Parch / Fare / Embarked
    test_input = np.array(
        [2, 'male', 31.0, 0, 0, 10.5, 'S'],
        dtype=object
    ).reshape(1,7)

    test_input
    ```

[⬆️ Go to Context](#context)

- **Step 4 – Apply Same Preprocessing**

  - Extract and Encode Sex

    ```py
    test_input_sex = ohe_sex.transform(
        test_input[:,1].reshape(1,1)
    )
    ```

  - Extract and Encode Embarked

    ```py
    test_input_embarked = ohe_embarked.transform(
        test_input[:,-1].reshape(1,1)
    )
    ```

  - Extract Age

    If no missing value:

    ```py
    test_input_age = test_input[:,2].reshape(1,1)
    ```

    If missing value handling needed:

      ```py
      test_input_age = si_age.transform(
          test_input[:,2].reshape(1,1)
      )
      ```

  - Extract Remaining Numeric Columns

    Keep:

    - Pclass
    - SibSp
    - Parch
    - Fare

    ```py
    test_input_numeric = test_input[:,[0,3,4,5]]
    ```

[⬆️ Go to Context](#context)

- **Step 5 – Concatenate Features**

  Order must match training order:

  - Remaining numeric
  - Age
  - Encoded Sex
  - Encoded Embarked

    ```py
    test_input_transformed = np.concatenate(
        (
            test_input_numeric,
            test_input_age,
            test_input_sex,
            test_input_embarked
        ),
        axis=1
    )

    test_input_transformed.shape
    ```

[⬆️ Go to Context](#context)

- **Step 6 – Make Prediction**

  ```py
  clf.predict(test_input_transformed)
  ```

  Output:

  - `0` → Did Not Survive
  - `1` → Survived

[⬆️ Go to Context](#context)

## **Titanic Training Using Pipeline**

- **Step 0 – Import Libraries**

  ```py
  import numpy as np
  import pandas as pd

  from sklearn.model_selection import train_test_split
  from sklearn.compose import ColumnTransformer
  from sklearn.impute import SimpleImputer
  from sklearn.preprocessing import OneHotEncoder
  from sklearn.preprocessing import MinMaxScaler
  from sklearn.pipeline import Pipeline, make_pipeline
  from sklearn.feature_selection import SelectKBest, chi2
  from sklearn.tree import DecisionTreeClassifier
  from sklearn.metrics import accuracy_score
  from sklearn.model_selection import cross_val_score

  import pickle
  ```

[⬆️ Go to Context](#context)

- **Step 1 – Load Dataset**

  ```py
  df = pd.read_csv('train.csv')
  df.head()
  ```

- **Step 2 – Drop Unnecessary Columns**

  Removed columns:

  - PassengerId → unique identifier
  - Name → high cardinality
  - Ticket → high cardinality
  - Cabin → too many missing values

    ```py
    df.drop(columns=['PassengerId','Name','Ticket','Cabin'], inplace=True)
    ```

[⬆️ Go to Context](#context)

- **Step 3 – Train Test Split**

  ```py
  X_train, X_test, y_train, y_test = train_test_split(
      df.drop(columns=['Survived']),
      df['Survived'],
      test_size=0.2,
      random_state=42
  )
  ```

  - 80% training
  - 20% testing
  - `random_state=42` ensures reproducibility

> [!NOTE]
> Understanding Each Transformer
>
> - Pipeline steps will execute sequentially:
> - Imputation → Encoding → Scaling → Feature Selection → Model

[⬆️ Go to Context](#context)

- **Step 4 – Imputation (trf1)**

  Handle missing values:

  - Age → Mean
  - Embarked → Most frequent

    ```py
    trf1 = ColumnTransformer([
        ('impute_age', SimpleImputer(), [2]),
        ('impute_embarked', SimpleImputer(strategy='most_frequent'), [6])
    ], remainder='passthrough')
    ```

    - Column indices used instead of names
    - `remainder='passthrough'` keeps other columns

[⬆️ Go to Context](#context)

- **Step 5 – One Hot Encoding (trf2)**

  Encode:

  - Sex
  - Embarked

    ```py
    trf2 = ColumnTransformer([
        ('ohe_sex_embarked',
        OneHotEncoder(sparse=False, handle_unknown='ignore'),
        [1,6])
    ], remainder='passthrough')
    ```

    - `handle_unknown='ignore'` prevents errors
    - Output becomes numpy array

[⬆️ Go to Context](#context)

- **Step 6 – Scaling (trf3)**

  Scale features between 0 and 1:

    ```py
    trf3 = ColumnTransformer([
        ('scale', MinMaxScaler(), slice(0,10))
    ])
    ```

  - Why scaling?
    - Required for chi-square feature selection
    - Makes features comparable

[⬆️ Go to Context](#context)

- **Step 7 – Feature Selection (trf4)**

  Select top 8 features using Chi-square test:

  ```py
  trf4 = SelectKBest(score_func=chi2, k=8)
  ```

  - `chi2` works only with non-negative values
  - That is why scaling was done before

[⬆️ Go to Context](#context)

- **Step 8 – Model (trf5)**

  ```py
  trf5 = DecisionTreeClassifier()
  ```

- **Step 9 – Create Full Pipeline**

  ```py
  pipe = Pipeline([
      ('trf1', trf1),
      ('trf2', trf2),
      ('trf3', trf3),
      ('trf4', trf4),
      ('trf5', trf5)
  ])
  ```

Execution order:

1. Missing value handling
2. Encoding
3. Scaling
4. Feature selection
5. Model training

- **Pipeline vs make_pipeline**

- `Pipeline()` → must name each step
- `make_pipeline()` → names auto-generated

Same idea applies to:

- `ColumnTransformer()`
- `make_column_transformer()`

Alternate syntax:

  ```py
  pipe = make_pipeline(trf1, trf2, trf3, trf4, trf5)
  ```

[⬆️ Go to Context](#context)

- **Step 10 – Train the Pipeline**

  ```py
  pipe.fit(X_train, y_train)
  ```

Important:

- All preprocessing + training happens internally
- No manual transformations required

- **Explore Pipeline**

  ```py
  pipe.named_steps
  ```

- Optional visualization:

  ```py
  from sklearn import set_config
  set_config(display='diagram')
  pipe
  ```

[⬆️ Go to Context](#context)

- **Step 11 – Prediction**

  ```py
  y_pred = pipe.predict(X_test)
  y_pred
  ```

No manual preprocessing required.

- **Step 12 – Evaluation**

  ```py
  accuracy_score(y_test, y_pred)
  ```

- **Step 13 – Cross Validation**

  ```py
  cross_val_score(pipe, X_train, y_train, cv=5, scoring='accuracy').mean()
  ```

- Why this is powerful?

  - Each fold automatically applies full preprocessing
  - No data leakage
  - Cleaner evaluation

- **Step 14 – Export Full Pipeline**

  ```py
  pickle.dump(pipe, open('pipe.pkl','wb'))
  ```

- Now only need:

  ```py
  pipe = pickle.load(open('pipe.pkl','rb'))
  pipe.predict(new_data)
  ```

> [!NOTE]
>
> - No separate encoders. No manual preprocessing.

[⬆️ Go to Context](#context)

## **Predict Using Pipeline**

- **Step 1 – Import Libraries**

  ```py
  import pickle
  import pandas as pd
  ```

- **Step 2 – Load Saved Pipeline**

  ```py
  pipe = pickle.load(open('pipe.pkl','rb'))
  ```

  What this pipeline already contains:

  - Imputation
  - One Hot Encoding
  - Scaling
  - Feature Selection
  - Decision Tree Model

  Everything is bundled together.

[⬆️ Go to Context](#context)

- **Step 3 – Create User Input**

  Important rules:

  - Must be a pandas DataFrame
  - Column names must match training data
  - Column order should remain same

  ```py
  test_input2 = pd.DataFrame(
      [[2, 'male', 31.0, 0, 0, 10.5, 'S']],
      columns=['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
  )

  test_input2
  ```

[⬆️ Go to Context](#context)

- **Step 4 – Make Prediction**

  ```py
  pipe.predict(test_input2)
  ```

  Output:

  - `0` → Did Not Survive
  - `1` → Survived

[⬆️ Go to Context](#context)

### What Happens Internally?

When we call:

  ```py
  pipe.predict(test_input2)
  ```

- Pipeline automatically performs:
  - Missing value handling
  - Encoding categorical features
  - Scaling numeric values
  - Selecting best features
  - Passing processed data into Decision Tree

- Why This Is Powerful
  - No manual feature extraction
  - No need to load encoders separately
  - No risk of feature order mismatch
  - Cleaner and safer deployment
  - Production ready

- Common Mistakes to Avoid
  - Passing numpy array instead of DataFrame (if using column names internally)
  - Missing required columns
  - Changing column order
  - Wrong data types

[⬆️ Go to Context](#context)

## **Manual vs Pipeline Prediction**

- Without Pipeline:
  - Manually impute
  - Manually encode
  - Manually concatenate
  - High risk of mistakes

- With Pipeline:
  - One line → `pipe.predict()`
  - Clean
  - Reliable
  - Scalable

[⬆️ Go to Context](#context)

# [**Day 52 - Data Transformation Techniques**](./Day%2052%20-%20Data%20Transformation%20Techniques/)

## **Function Transformer**

- A **Function Transformer** applies a mathematical function to a feature.
- Used in preprocessing to **change the distribution of data**.
- Often used when data is **skewed, has large ranges, or violates model assumptions**.
- In libraries like **scikit-learn**, it is implemented using `FunctionTransformer`.

  ```py
  from sklearn.preprocessing import FunctionTransformer
  import numpy as np

  transformer = FunctionTransformer(np.log)

  data = np.array([[1],[2],[10],[100]])
  transformed = transformer.transform(data)

  print(transformed)
  ```

There are:

- Log Transformation
- Reciprocal Transformation
- Square Transformation
- Square Root Transformation

[⬆️ Go to Context](#context)

### Log Transformation

- Applies the **logarithm** to values.
- Reduces **right-skewed distributions**.
- Compresses large values more than small values.
- Formula
  - `y = log(x)`

- When to Use
  - Data is **highly right skewed**
  - Feature values grow **exponentially**
  - There are **large outliers**

- Where Used
  - Financial data
  - Population growth
  - Income distribution
  - Web traffic counts

  ```py
  import numpy as np
  from sklearn.preprocessing import FunctionTransformer

  log_transformer = FunctionTransformer(np.log1p)  # log(1+x) safer for zero values

  X = np.array([[0],[1],[10],[100]])

  X_log = log_transformer.transform(X)

  print(X_log)
  ```

[⬆️ Go to Context](#context)

### Reciprocal Transformation

- Uses the **inverse of the variable**.
- Strongly reduces the effect of **very large values**.
- Formula
  - `y = 1 / x`

- When to Use
  - Data has **extreme right skew**
  - Relationship between variables is **inverse**

- Where Used
  - Physics formulas
  - Rate calculations
  - Time vs speed relationships

  ```py
  import numpy as np
  from sklearn.preprocessing import FunctionTransformer

  reciprocal_transformer = FunctionTransformer(lambda x: 1/x)

  X = np.array([[1],[2],[4],[8]])

  X_recip = reciprocal_transformer.transform(X)

  print(X_recip)
  ```

> [!NOTE]
>
> - Cannot contain **zero values**.

[⬆️ Go to Context](#context)

### Square Transformation

- Squares each value.
- Expands large values more than small ones.
- Formula
  - `y = x²`

- When to Use
  - Relationship is **quadratic**
  - Need to emphasize **large differences**

- Where Used
  - Polynomial regression
  - Variance calculations
  - Feature engineering

  ```py
  import numpy as np
  from sklearn.preprocessing import FunctionTransformer

  square_transformer = FunctionTransformer(lambda x: x**2)

  X = np.array([[1],[2],[3],[4]])

  X_square = square_transformer.transform(X)

  print(X_square)
  ```

[⬆️ Go to Context](#context)

### Square Root Transformation

- Takes the **square root** of values.
- Moderately reduces **right skew**.
- Formula
  - `y = √x`

- When to Use
  - Data is **moderately skewed**
  - Counts or frequency data

- Where Used
  - Biological counts
  - Event frequencies
  - Population data

  ```py
  import numpy as np
  from sklearn.preprocessing import FunctionTransformer

  sqrt_transformer = FunctionTransformer(np.sqrt)

  X = np.array([[1],[4],[9],[16]])

  X_sqrt = sqrt_transformer.transform(X)

  print(X_sqrt)
  ```

[⬆️ Go to Context](#context)

## **Function Transformer Comparison**

| Transformation | Strength              | Handles Zero  | Typical Use              |
| -------------- | --------------------- | ------------- | ------------------------ |
| Log            | Strong skew reduction | Yes (`log1p`) | Finance, growth data     |
| Reciprocal     | Very strong           | No            | Rates, inverse relations |
| Square         | Expands values        | Yes           | Polynomial models        |
| Square Root    | Mild skew reduction   | Yes           | Count data               |

[⬆️ Go to Context](#context)

## **Power Transformer**

- A **Power Transformer** applies a **power-based mathematical transformation** to make data more **Gaussian (normal distribution)**.
- Helps reduce **skewness** and stabilize **variance**.
- Commonly used before models that assume normality (e.g., linear models).

- In **scikit-learn**, this is implemented using `PowerTransformer`.

  ```py
  from sklearn.preprocessing import PowerTransformer
  import numpy as np

  X = np.array([[1],[2],[3],[4],[5]])

  pt = PowerTransformer()

  X_transformed = pt.fit_transform(X)

  print(X_transformed)
  ```

- Box-Cox Transformation
- Yeo Johnson Transformation

[⬆️ Go to Context](#context)

### Box-Cox Transformation

- A **power transformation** designed to make data **more normally distributed**.
- Uses a parameter **λ (lambda)** to determine the transformation strength.
- Formula
  - If λ ≠ 0 → `y = (x^λ − 1) / λ`
  - If λ = 0 → `y = log(x)`

- When to Use
  - Data is **positively skewed**
  - Values are **strictly positive**
  - Need to approximate **normal distribution**

- Where Used
  - Econometrics
  - Biological measurements
  - Financial modeling

> [!NOTE]
>
> - **Cannot handle zero or negative values**

  ```py
  from sklearn.preprocessing import PowerTransformer
  import numpy as np

  X = np.array([[1],[2],[3],[4],[5]])

  boxcox = PowerTransformer(method='box-cox')

  X_boxcox = boxcox.fit_transform(X)

  print(X_boxcox)
  ```

[⬆️ Go to Context](#context)

### Yeo Johnson Transformation

- Extension of **Box-Cox** that works with **negative values and zero**.
- Automatically finds the **best λ parameter**.
- Key Advantage
  - Works with **positive, zero, and negative values**.

- When to Use
  - Data contains **zero or negative numbers**
  - Want **automatic skewness correction**
  - Similar goal as Box-Cox but more flexible

- Where Used
  - General machine learning preprocessing
  - Real-world datasets containing **mixed values**

  ```py
  from sklearn.preprocessing import PowerTransformer
  import numpy as np

  X = np.array([[-5],[-1],[0],[2],[10]])

  yeo = PowerTransformer(method='yeo-johnson')

  X_yeo = yeo.fit_transform(X)

  print(X_yeo)
  ```

[⬆️ Go to Context](#context)

## **Power Transformer Comparison**

  | Transformation | Handles Zero | Handles Negative | Typical Use                   |
  | -------------- | ------------ | ---------------- | ----------------------------- |
  | Box-Cox        | No           | No               | Strictly positive skewed data |
  | Yeo-Johnson    | Yes          | Yes              | Real-world mixed data         |

- Use **Box-Cox** when you are **sure all values are positive**.
- Use **Yeo-Johnson** when dataset may contain **zero or negative values**.

- Inside a pipeline:

  ```py
  from sklearn.preprocessing import PowerTransformer
  from sklearn.pipeline import Pipeline

  pipe = Pipeline([
      ('power', PowerTransformer(method='yeo-johnson'))
  ])
  ```

[⬆️ Go to Context](#context)

# [**Day 53 - Outlier Detection and Removal**](./Day%2053%20-%20Outlier%20Detection%20and%20Removal/)

- [placement dataset](https://www.kaggle.com/datasets/biplavkant/placement)

## **Outlier Detection**

- Detects data points that are significantly different from the rest.
- Helps improve model accuracy by identifying anomalies.
- **Z-Score Method**

  - Measures how many standard deviations a point is from the mean.
  - Typically, |z| > 3 is considered an outlier.

- **IQR (Interquartile Range) Method**

  - Calculates Q1 (25th percentile) and Q3 (75th percentile).
  - Outliers: values < Q1 − 1.5×IQR or > Q3 + 1.5×IQR.

- **Boxplot Visualization**

  - Uses quartiles to visually detect outliers as points outside whiskers.

- **Scatter Plot / Pair Plot**

  - Helps detect outliers in multidimensional data visually.

- **Percentile / Quantile Method**

  - Defines thresholds based on specific percentiles (e.g., top 1% or bottom 1%).

- **DBSCAN (Density-Based Clustering)**

  - Points far from dense clusters are flagged as outliers in multidimensional data.

- **Isolation Forest**

  - Tree-based model isolates anomalies automatically in large datasets.

  ```py
  import pandas as pd
  import numpy as np
  from scipy.stats import zscore

  data = pd.DataFrame({'Age': [12, 15, 14, 130, 16, 17, 15]})

  # Z-Score Detection
  data['z_score'] = zscore(data['Age'])
  z_outliers = data[np.abs(data['z_score']) > 3]

  # IQR Detection
  Q1 = data['Age'].quantile(0.25)
  Q3 = data['Age'].quantile(0.75)
  IQR = Q3 - Q1
  iqr_outliers = data[(data['Age'] < Q1 - 1.5*IQR) | (data['Age'] > Q3 + 1.5*IQR)]

  print("Z-Score Outliers:\n", z_outliers)
  print("IQR Outliers:\n", iqr_outliers)
  ```

[⬆️ Go to Context](#context)

## **Outlier Removal**

- Removes or reduces the effect of extreme values.
- Two common methods: **Trimming** and **Capping**.

[⬆️ Go to Context](#context)

### Trimming

- Completely removes the outlier rows from the dataset.
- Simple but reduces dataset size.

  ```py
  # Removing outliers beyond 3 standard deviations
  data_trimmed = data[np.abs(data['z_score']) <= 3]
  print(data_trimmed)
  ```

[⬆️ Go to Context](#context)

### Capping

- Replaces outliers with the nearest non-outlier value.
- Preserves dataset size while reducing extreme impact.

  ```py
  # Using IQR method for capping
  Q1 = data['Age'].quantile(0.25)
  Q3 = data['Age'].quantile(0.75)
  IQR = Q3 - Q1

  lower_bound = Q1 - 1.5 * IQR
  upper_bound = Q3 + 1.5 * IQR

  data_capped = data.copy()
  data_capped['Age'] = np.where(data['Age'] > upper_bound, upper_bound,
                                np.where(data['Age'] < lower_bound, lower_bound, data['Age']))
  print(data_capped)
  ```

[⬆️ Go to Context](#context)
