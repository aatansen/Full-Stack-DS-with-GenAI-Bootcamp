# **Context**

- [**Context**](#context)
- [**Day 44 - Exploratory Data Analysis EDA**](#day-44---exploratory-data-analysis-eda)
  - [**Types of EDA**](#types-of-eda)
    - [Univariate Analysis](#univariate-analysis)
    - [Bivariate Analysis](#bivariate-analysis)
    - [Multivariate Analysis](#multivariate-analysis)
  - [**Titanic Dataset EDA**](#titanic-dataset-eda)
    - [Univariate Analysis(Titanic)](#univariate-analysistitanic)
    - [Bivariate Analysis(Titanic)](#bivariate-analysistitanic)
    - [Multivariate Analysis(Titanic)](#multivariate-analysistitanic)
  - [**Advanced EDA Techniques**](#advanced-eda-techniques)
    - [Data Quality Assessment](#data-quality-assessment)
    - [Outlier Analysis](#outlier-analysis)
    - [Distribution Analysis](#distribution-analysis)
    - [Feature Engineering for EDA](#feature-engineering-for-eda)
    - [Time-Based Analysis (if applicable)](#time-based-analysis-if-applicable)
    - [Segmentation Analysis](#segmentation-analysis)
    - [Comprehensive EDA Report](#comprehensive-eda-report)
- [**Day 45 - Bivariate and Multivariate Analysis in EDA**](#day-45---bivariate-and-multivariate-analysis-in-eda)
  - [**Bivariate and Multivariate Analysis**](#bivariate-and-multivariate-analysis)
  - [**Automatic Analysis**](#automatic-analysis)
- [**Day 46 - EDA Project - Titanic Data**](#day-46---eda-project---titanic-data)
  - [**Titanic EDA**](#titanic-eda)


# [**Day 44 - Exploratory Data Analysis EDA**](./Day%2044%20-%20Exploratory%20Data%20Analysis%20EDA/)

## **Types of EDA**

- Univariate Analysis
- Bivariate Analysis
- Multivariate Analysis

### Univariate Analysis

- **Definition**: Analysis of a single variable at a time
  - **Purpose**: Understand distribution, central tendency, and spread of individual variables
  - **Where used**: Initial data exploration, feature understanding, outlier detection

- **Measures of Central Tendency**: Locate the center of data
  - **Formulas**:
    - Mean: μ = (1/n)Σxᵢ
    - Median: Middle value when sorted
    - Mode: Most frequent value
  - **Where used**: Summary statistics, understanding typical values

    ```py
    import pandas as pd
    import numpy as np

    # Central tendency
    mean = df['Age'].mean()
    median = df['Age'].median()
    mode = df['Age'].mode()[0]

    print(f"Mean: {mean}, Median: {median}, Mode: {mode}")
    ```

- **Measures of Dispersion**: Measure variability in data
  - **Formulas**:
    - Variance: σ² = (1/n)Σ(xᵢ - μ)²
    - Standard Deviation: σ = √variance
    - Range: max - min
    - IQR: Q3 - Q1
  - **Where used**: Understanding data spread, identifying outliers

    ```py
    # Dispersion measures
    variance = df['Age'].var()
    std_dev = df['Age'].std()
    data_range = df['Age'].max() - df['Age'].min()
    iqr = df['Age'].quantile(0.75) - df['Age'].quantile(0.25)

    print(f"Std Dev: {std_dev}, IQR: {iqr}")
    ```

- **Skewness**: Measure of asymmetry in distribution
  - **Formula**: Skewness = E[(X-μ)³]/σ³
  - **Interpretation**:
    - Skewness > 0: Right-skewed (tail on right)
    - Skewness < 0: Left-skewed (tail on left)
    - Skewness ≈ 0: Symmetric
  - **Where used**: Understanding distribution shape, feature engineering

    ```py
    from scipy.stats import skew

    skewness = skew(df['Age'].dropna())
    print(f"Skewness: {skewness:.3f}")

    # Interpretation
    if skewness > 1:
        print("Highly right-skewed")
    elif skewness < -1:
        print("Highly left-skewed")
    else:
        print("Approximately symmetric")
    ```

- **Kurtosis**: Measure of tail heaviness
  - **Formula**: Kurtosis = E[(X-μ)⁴]/σ⁴
  - **Interpretation**:
    - Kurtosis > 3: Heavy tails (leptokurtic)
    - Kurtosis < 3: Light tails (platykurtic)
    - Kurtosis ≈ 3: Normal distribution (mesokurtic)
  - **Where used**: Identifying outliers, understanding distribution tails

    ```py
    from scipy.stats import kurtosis

    kurt = kurtosis(df['Age'].dropna(), fisher=False)
    print(f"Kurtosis: {kurt:.3f}")
    ```

- **Histogram**: Visual representation of frequency distribution
  - **Purpose**: Show distribution shape, identify modes, detect outliers
  - **Where used**: Continuous numerical variables

    ```py
    import matplotlib.pyplot as plt

    plt.figure(figsize=(10, 5))
    plt.hist(df['Age'].dropna(), bins=30, edgecolor='black', alpha=0.7)
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.title('Age Distribution')
    plt.axvline(df['Age'].mean(), color='red', linestyle='--', label='Mean')
    plt.axvline(df['Age'].median(), color='green', linestyle='--', label='Median')
    plt.legend()
    plt.show()
    ```

- **Box Plot (Box-and-Whisker Plot)**: Display five-number summary
  - **Components**:
    - Minimum (Q1 - 1.5×IQR)
    - Q1 (25th percentile)
    - Median (Q2, 50th percentile)
    - Q3 (75th percentile)
    - Maximum (Q3 + 1.5×IQR)
  - **Where used**: Identifying outliers, comparing distributions

    ```py
    plt.figure(figsize=(8, 5))
    plt.boxplot(df['Age'].dropna(), vert=True)
    plt.ylabel('Age')
    plt.title('Age Box Plot')
    plt.grid(True, alpha=0.3)
    plt.show()

    # Identify outliers
    Q1 = df['Age'].quantile(0.25)
    Q3 = df['Age'].quantile(0.75)
    IQR = Q3 - Q1
    outliers = df[(df['Age'] < Q1 - 1.5*IQR) | (df['Age'] > Q3 + 1.5*IQR)]
    print(f"Number of outliers: {len(outliers)}")
    ```

- **Density Plot (KDE)**: Smooth estimate of probability density
  - **Formula**: KDE uses kernel function K: f̂(x) = (1/nh)Σ K((x-xᵢ)/h)
  - **Where used**: Visualizing continuous distributions smoothly

    ```py
    plt.figure(figsize=(10, 5))
    df['Age'].dropna().plot(kind='density', linewidth=2)
    plt.xlabel('Age')
    plt.ylabel('Density')
    plt.title('Age Density Plot')
    plt.grid(True, alpha=0.3)
    plt.show()
    ```

- **Q-Q Plot (Quantile-Quantile Plot)**: Test for normality
  - **Purpose**: Compare data distribution to theoretical normal distribution
  - **Where used**: Checking normality assumption for statistical tests

    ```py
    from scipy import stats

    plt.figure(figsize=(8, 5))
    stats.probplot(df['Age'].dropna(), dist="norm", plot=plt)
    plt.title('Q-Q Plot for Age')
    plt.grid(True, alpha=0.3)
    plt.show()
    ```

- **Frequency Table**: Count occurrences of categorical values
  - **Purpose**: Understand distribution of categories
  - **Where used**: Categorical variables

    ```py
    # Absolute frequency
    freq_table = df['Pclass'].value_counts().sort_index()
    print("Frequency Table:")
    print(freq_table)

    # Relative frequency (percentage)
    rel_freq = df['Pclass'].value_counts(normalize=True).sort_index() * 100
    print("\nRelative Frequency:")
    print(rel_freq)
    ```

- **Bar Chart**: Visual representation of categorical data
  - **Purpose**: Compare frequencies across categories
  - **Where used**: Categorical variables with few unique values

    ```py
    plt.figure(figsize=(8, 5))
    df['Pclass'].value_counts().sort_index().plot(kind='bar', color='skyblue', edgecolor='black')
    plt.xlabel('Passenger Class')
    plt.ylabel('Count')
    plt.title('Passenger Class Distribution')
    plt.xticks(rotation=0)
    plt.grid(axis='y', alpha=0.3)
    plt.show()
    ```

- **Pie Chart**: Show proportions of whole
  - **Purpose**: Display percentage breakdown of categories
  - **Where used**: Categorical variables (best with 2-5 categories)

    ```py
    plt.figure(figsize=(8, 8))
    df['Survived'].value_counts().plot(kind='pie', autopct='%1.1f%%',
                                       labels=['Died', 'Survived'],
                                       colors=['#ff9999', '#66b3ff'],
                                       startangle=90)
    plt.ylabel('')
    plt.title('Survival Rate')
    plt.show()
    ```

- **Missing Value Analysis**: Identify and quantify missing data
  - **Purpose**: Understand data completeness, plan imputation strategy
  - **Where used**: Data quality assessment

    ```py
    # Count missing values
    missing_counts = df.isnull().sum()
    missing_percent = (df.isnull().sum() / len(df)) * 100

    missing_df = pd.DataFrame({
        'Missing_Count': missing_counts,
        'Percentage': missing_percent
    })
    print(missing_df[missing_df['Missing_Count'] > 0])

    # Visualize missing values
    import seaborn as sns
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.isnull(), cbar=True, yticklabels=False, cmap='viridis')
    plt.title('Missing Values Heatmap')
    plt.show()
    ```

[⬆️ Go to Context](#context)

### Bivariate Analysis

- **Definition**: Analysis of relationship between two variables
  - **Purpose**: Understand associations, dependencies, and patterns between variables
  - **Where used**: Feature selection, correlation analysis, relationship exploration

- **Pearson Correlation Coefficient**: Linear relationship strength
  - **Formula**: r = Σ[(xᵢ-x̄)(yᵢ-ȳ)] / √[Σ(xᵢ-x̄)²Σ(yᵢ-ȳ)²]
  - **Range**: -1 to +1
    - r = +1: Perfect positive correlation
    - r = -1: Perfect negative correlation
    - r = 0: No linear correlation
  - **Where used**: Numerical vs numerical relationships

    ```py
    # Pearson correlation
    correlation = df['Age'].corr(df['Fare'])
    print(f"Pearson Correlation: {correlation:.3f}")

    # Correlation with p-value
    from scipy.stats import pearsonr
    corr, p_value = pearsonr(df['Age'].dropna(), df['Fare'].dropna())
    print(f"Correlation: {corr:.3f}, P-value: {p_value:.4f}")
    ```

- **Spearman Rank Correlation**: Monotonic relationship strength
  - **Formula**: ρ = 1 - (6Σdᵢ²) / [n(n²-1)], where dᵢ is rank difference
  - **Where used**: Non-linear monotonic relationships, ordinal data

    ```py
    from scipy.stats import spearmanr

    corr, p_value = spearmanr(df['Age'].dropna(), df['Fare'].dropna())
    print(f"Spearman Correlation: {corr:.3f}, P-value: {p_value:.4f}")
    ```

- **Scatter Plot**: Visualize relationship between two numerical variables
  - **Purpose**: Identify patterns, trends, outliers, correlation direction
  - **Where used**: Numerical vs numerical analysis

    ```py
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Age'], df['Fare'], alpha=0.5, edgecolors='black')
    plt.xlabel('Age')
    plt.ylabel('Fare')
    plt.title('Age vs Fare Relationship')

    # Add regression line
    from scipy.stats import linregress
    slope, intercept, r_value, p_value, std_err = linregress(
        df['Age'].dropna(), df['Fare'].dropna()
    )
    line = slope * df['Age'] + intercept
    plt.plot(df['Age'], line, color='red', linewidth=2, label=f'r²={r_value**2:.3f}')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()
    ```

- **Line Plot**: Show trends over continuous variable
  - **Purpose**: Display trends, time series patterns
  - **Where used**: Sequential data, time series

    ```py
    # Group by age and calculate mean fare
    age_fare = df.groupby('Age')['Fare'].mean()

    plt.figure(figsize=(10, 6))
    plt.plot(age_fare.index, age_fare.values, marker='o', linewidth=2)
    plt.xlabel('Age')
    plt.ylabel('Average Fare')
    plt.title('Average Fare by Age')
    plt.grid(True, alpha=0.3)
    plt.show()
    ```

- **Group Statistics**: Compare numerical variable across categories
  - **Metrics**: Mean, median, std, min, max by groups
  - **Where used**: Categorical vs numerical analysis

    ```py
    # Group statistics
    group_stats = df.groupby('Survived')['Age'].agg([
        'count', 'mean', 'median', 'std', 'min', 'max'
    ])
    print(group_stats)

    # Multiple aggregations
    agg_dict = {
        'Age': ['mean', 'median'],
        'Fare': ['mean', 'sum']
    }
    multi_stats = df.groupby('Pclass').agg(agg_dict)
    print(multi_stats)
    ```

- **Grouped Box Plot**: Compare distributions across categories
  - **Purpose**: Visualize distribution differences between groups
  - **Where used**: Categorical vs numerical analysis

    ```py
    plt.figure(figsize=(10, 6))
    df.boxplot(column='Age', by='Survived', grid=False)
    plt.suptitle('')
    plt.xlabel('Survived (0=No, 1=Yes)')
    plt.ylabel('Age')
    plt.title('Age Distribution by Survival Status')
    plt.show()

    # Multiple box plots
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    df.boxplot(column='Age', by='Survived', ax=axes[0], grid=False)
    df.boxplot(column='Fare', by='Pclass', ax=axes[1], grid=False)
    axes[0].set_title('Age by Survival')
    axes[1].set_title('Fare by Class')
    plt.tight_layout()
    plt.show()
    ```

- **Violin Plot**: Combine box plot and density plot
  - **Purpose**: Show distribution shape and summary statistics
  - **Where used**: Detailed distribution comparison across groups

    ```py
    import seaborn as sns

    plt.figure(figsize=(10, 6))
    sns.violinplot(x='Pclass', y='Age', data=df, palette='Set2')
    plt.xlabel('Passenger Class')
    plt.ylabel('Age')
    plt.title('Age Distribution by Class (Violin Plot)')
    plt.show()
    ```

- **Cross Tabulation (Contingency Table)**: Frequency of category combinations
  - **Formula**: Count of each (Category1, Category2) pair
  - **Where used**: Categorical vs categorical analysis

    ```py
    # Absolute frequency
    crosstab = pd.crosstab(df['Sex'], df['Survived'])
    print("Cross Tabulation:")
    print(crosstab)

    # Row percentages
    crosstab_pct = pd.crosstab(df['Sex'], df['Survived'], normalize='index') * 100
    print("\nRow Percentages:")
    print(crosstab_pct)

    # Column percentages
    crosstab_col = pd.crosstab(df['Sex'], df['Survived'], normalize='columns') * 100
    print("\nColumn Percentages:")
    print(crosstab_col)
    ```

- **Chi-Square Test**: Test independence between categorical variables
  - **Formula**: χ² = Σ[(Oᵢⱼ - Eᵢⱼ)² / Eᵢⱼ]
  - **Hypothesis**:
    - H₀: Variables are independent
    - H₁: Variables are dependent
  - **Where used**: Testing categorical relationships

    ```py
    from scipy.stats import chi2_contingency

    crosstab = pd.crosstab(df['Sex'], df['Survived'])
    chi2, p_value, dof, expected = chi2_contingency(crosstab)

    print(f"Chi-square statistic: {chi2:.4f}")
    print(f"P-value: {p_value:.4f}")
    print(f"Degrees of freedom: {dof}")

    if p_value < 0.05:
        print("Variables are significantly related")
    else:
        print("Variables are independent")
    ```

- **Grouped Bar Chart**: Compare categories across groups
  - **Purpose**: Visualize categorical relationships
  - **Where used**: Categorical vs categorical analysis

    ```py
    # Grouped bar chart
    crosstab = pd.crosstab(df['Sex'], df['Survived'])

    plt.figure(figsize=(10, 6))
    crosstab.plot(kind='bar', color=['#ff9999', '#66b3ff'], edgecolor='black')
    plt.xlabel('Sex')
    plt.ylabel('Count')
    plt.title('Survival Count by Gender')
    plt.legend(['Died', 'Survived'])
    plt.xticks(rotation=0)
    plt.grid(axis='y', alpha=0.3)
    plt.show()
    ```

- **Stacked Bar Chart**: Show composition within categories
  - **Purpose**: Display part-to-whole relationships
  - **Where used**: Proportion comparison across categories

    ```py
    crosstab_pct = pd.crosstab(df['Pclass'], df['Survived'], normalize='index') * 100

    plt.figure(figsize=(10, 6))
    crosstab_pct.plot(kind='bar', stacked=True, color=['#ff9999', '#66b3ff'])
    plt.xlabel('Passenger Class')
    plt.ylabel('Percentage')
    plt.title('Survival Rate by Class (Stacked)')
    plt.legend(['Died', 'Survived'])
    plt.xticks(rotation=0)
    plt.grid(axis='y', alpha=0.3)
    plt.show()
    ```

- **T-Test**: Compare means between two groups
  - **Formula**: t = (x̄₁ - x̄₂) / √[(s₁²/n₁) + (s₂²/n₂)]
  - **Where used**: Testing if group means differ significantly

    ```py
    from scipy.stats import ttest_ind

    survived_ages = df[df['Survived'] == 1]['Age'].dropna()
    died_ages = df[df['Survived'] == 0]['Age'].dropna()

    t_stat, p_value = ttest_ind(survived_ages, died_ages)
    print(f"T-statistic: {t_stat:.4f}")
    print(f"P-value: {p_value:.4f}")

    if p_value < 0.05:
        print("Significant difference in means")
    else:
        print("No significant difference")
    ```

- **ANOVA (Analysis of Variance)**: Compare means across multiple groups
  - **Formula**: F = (Between-group variance) / (Within-group variance)
  - **Where used**: Comparing 3+ group means

    ```py
    from scipy.stats import f_oneway

    class1_ages = df[df['Pclass'] == 1]['Age'].dropna()
    class2_ages = df[df['Pclass'] == 2]['Age'].dropna()
    class3_ages = df[df['Pclass'] == 3]['Age'].dropna()

    f_stat, p_value = f_oneway(class1_ages, class2_ages, class3_ages)
    print(f"F-statistic: {f_stat:.4f}")
    print(f"P-value: {p_value:.4f}")
    ```

[⬆️ Go to Context](#context)

### Multivariate Analysis

- **Definition**: Analysis of three or more variables simultaneously
  - **Purpose**: Understand complex interactions, identify patterns across multiple dimensions
  - **Where used**: Advanced feature relationships, comprehensive data understanding

- **Correlation Matrix**: Pairwise correlations between all numerical variables
  - **Formula**: Matrix of Pearson/Spearman correlations
  - **Where used**: Feature selection, multicollinearity detection

    ```py
    # Select numerical columns
    numerical_cols = df.select_dtypes(include=[np.number]).columns
    corr_matrix = df[numerical_cols].corr()

    print("Correlation Matrix:")
    print(corr_matrix)

    # Find highly correlated pairs
    threshold = 0.7
    high_corr = []
    for i in range(len(corr_matrix.columns)):
        for j in range(i+1, len(corr_matrix.columns)):
            if abs(corr_matrix.iloc[i, j]) > threshold:
                high_corr.append((corr_matrix.columns[i],
                                corr_matrix.columns[j],
                                corr_matrix.iloc[i, j]))
    print("\nHighly Correlated Pairs:")
    for pair in high_corr:
        print(f"{pair[0]} <-> {pair[1]}: {pair[2]:.3f}")
    ```

- **Heatmap**: Visual representation of correlation matrix
  - **Purpose**: Quickly identify strong correlations
  - **Where used**: Correlation visualization, pattern detection

    ```py
    import seaborn as sns

    plt.figure(figsize=(12, 10))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0,
                square=True, linewidths=1, cbar_kws={"shrink": 0.8},
                fmt='.2f', vmin=-1, vmax=1)
    plt.title('Correlation Heatmap', fontsize=16)
    plt.tight_layout()
    plt.show()
    ```

- **Pair Plot (Scatter Plot Matrix)**: Grid of scatter plots
  - **Purpose**: Visualize all pairwise relationships
  - **Where used**: Quick exploration of multiple variable relationships

    ```py
    import seaborn as sns

    # Basic pair plot
    sns.pairplot(df[['Age', 'Fare', 'SibSp', 'Parch', 'Survived']])
    plt.suptitle('Pair Plot of Numerical Variables', y=1.02)
    plt.show()

    # With hue
    sns.pairplot(df[['Age', 'Fare', 'Pclass', 'Survived']],
                 hue='Survived', diag_kind='kde',
                 palette={0: 'red', 1: 'green'})
    plt.show()
    ```

- **Pivot Table**: Multi-dimensional aggregation
  - **Purpose**: Summarize data across multiple dimensions
  - **Where used**: Complex aggregations, business intelligence

    ```py
    # Simple pivot table
    pivot = df.pivot_table(values='Survived',
                           index='Pclass',
                           columns='Sex',
                           aggfunc='mean')
    print("Survival Rate by Class and Gender:")
    print(pivot)

    # Multiple aggregations
    pivot_multi = df.pivot_table(values=['Survived', 'Age'],
                                  index='Pclass',
                                  columns='Sex',
                                  aggfunc={'Survived': 'mean', 'Age': ['mean', 'median']})
    print("\nMultiple Aggregations:")
    print(pivot_multi)
    ```

- **Grouped Analysis**: Aggregate by multiple categorical variables
  - **Purpose**: Understand patterns across group combinations
  - **Where used**: Segmentation analysis, pattern discovery

    ```py
    # Group by multiple variables
    grouped = df.groupby(['Pclass', 'Sex', 'Survived']).agg({
        'Age': ['mean', 'count'],
        'Fare': ['mean', 'sum']
    })
    print(grouped)

    # Survival rate by multiple factors
    survival_rate = df.groupby(['Pclass', 'Sex'])['Survived'].agg([
        ('Count', 'count'),
        ('Survived', 'sum'),
        ('Rate', 'mean')
    ])
    print("\nSurvival Rate:")
    print(survival_rate)
    ```

- **FacetGrid**: Multiple plots in grid layout
  - **Purpose**: Visualize data across multiple categorical dimensions
  - **Where used**: Comparing distributions across subgroups

    ```py
    import seaborn as sns

    # Create FacetGrid
    g = sns.FacetGrid(df, col='Pclass', row='Survived',
                      height=3, aspect=1.2)
    g.map(plt.hist, 'Age', bins=20, edgecolor='black', alpha=0.7)
    g.add_legend()
    g.fig.suptitle('Age Distribution by Class and Survival', y=1.02)
    plt.show()

    # With different plot types
    g = sns.FacetGrid(df, col='Pclass', hue='Survived', height=4)
    g.map(plt.scatter, 'Age', 'Fare', alpha=0.5)
    g.add_legend()
    plt.show()
    ```

- **3D Scatter Plot**: Visualize three numerical variables
  - **Purpose**: Show relationships in 3D space
  - **Where used**: Exploring 3-variable relationships

    ```py
    from mpl_toolkits.mplot3d import Axes3D

    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')

    colors = ['red' if s == 0 else 'green' for s in df['Survived']]
    scatter = ax.scatter(df['Age'], df['Fare'], df['Pclass'],
                         c=colors, alpha=0.6, s=50)
    ax.set_xlabel('Age', fontsize=12)
    ax.set_ylabel('Fare', fontsize=12)
    ax.set_zlabel('Pclass', fontsize=12)
    ax.set_title('3D Scatter: Age vs Fare vs Class', fontsize=14)

    # Add legend
    from matplotlib.lines import Line2D
    legend_elements = [Line2D([0], [0], marker='o', color='w',
                             markerfacecolor='r', label='Died'),
                      Line2D([0], [0], marker='o', color='w',
                             markerfacecolor='g', label='Survived')]
    ax.legend(handles=legend_elements)
    plt.show()
    ```

- **Parallel Coordinates Plot**: Visualize multivariate data
  - **Purpose**: Show patterns across multiple numerical variables
  - **Where used**: High-dimensional data visualization

    ```py
    from pandas.plotting import parallel_coordinates

    # Normalize data for better visualization
    df_normalized = df[['Pclass', 'Age', 'Fare', 'Survived']].copy()
    df_normalized['Age'] = (df_normalized['Age'] - df_normalized['Age'].min()) / \
                           (df_normalized['Age'].max() - df_normalized['Age'].min())
    df_normalized['Fare'] = (df_normalized['Fare'] - df_normalized['Fare'].min()) / \
                            (df_normalized['Fare'].max() - df_normalized['Fare'].min())
    df_normalized = df_normalized.dropna()

    plt.figure(figsize=(12, 6))
    parallel_coordinates(df_normalized, 'Survived', color=['red', 'green'])
    plt.title('Parallel Coordinates Plot')
    plt.xlabel('Variables')
    plt.ylabel('Normalized Values')
    plt.legend(['Died', 'Survived'])
    plt.grid(True, alpha=0.3)
    plt.show()
    ```

- **Multivariate Outlier Detection**: Identify outliers in multiple dimensions
  - **Formula**: Mahalanobis Distance: D² = (x-μ)ᵀΣ⁻¹(x-μ)
  - **Where used**: Anomaly detection, data cleaning

    ```py
    from scipy.spatial.distance import mahalanobis
    from scipy import stats

    # Select numerical features
    features = df[['Age', 'Fare', 'SibSp', 'Parch']].dropna()

    # Calculate mean and covariance
    mean = features.mean()
    cov = features.cov()
    cov_inv = np.linalg.inv(cov)

    # Calculate Mahalanobis distance
    distances = []
    for i, row in features.iterrows():
        distance = mahalanobis(row, mean, cov_inv)
        distances.append(distance)

    features['Mahalanobis'] = distances

    # Identify outliers (using chi-square distribution)
    threshold = stats.chi2.ppf(0.95, df=len(features.columns)-1)
    outliers = features[features['Mahalanobis'] > threshold]
    print(f"Number of multivariate outliers: {len(outliers)}")
    ```

- **Principal Component Analysis (PCA)**: Dimensionality reduction
  - **Purpose**: Reduce variables while preserving variance
  - **Where used**: Feature reduction, visualization of high-dimensional data

    ```py
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler

    # Prepare data
    features = df[['Age', 'Fare', 'SibSp', 'Parch']].dropna()
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)

    # Apply PCA
    pca = PCA(n_components=2)
    principal_components = pca.fit_transform(features_scaled)

    # Variance explained
    print(f"Variance explained: {pca.explained_variance_ratio_}")
    print(f"Cumulative variance: {np.cumsum(pca.explained_variance_ratio_)}")

    # Visualize
    plt.figure(figsize=(10, 6))
    plt.scatter(principal_components[:, 0], principal_components[:, 1],
                alpha=0.5)
    plt.xlabel(f'PC1 ({pca.explained_variance_ratio_[0]:.2%} variance)')
    plt.ylabel(f'PC2 ({pca.explained_variance_ratio_[1]:.2%} variance)')
    plt.title('PCA - First Two Principal Components')
    plt.grid(True, alpha=0.3)
    plt.show()
    ```

- **Interaction Effects**: Analyze combined effects of variables
  - **Purpose**: Understand how variable combinations affect outcome
  - **Where used**: Feature engineering, model interpretation

    ```py
    # Create interaction features
    df['Age_Fare_Interaction'] = df['Age'] * df['Fare']
    df['Family_Size'] = df['SibSp'] + df['Parch'] + 1

    # Analyze interaction effect
    interaction_analysis = df.groupby(['Pclass', 'Sex'])['Survived'].mean()
    print("Interaction Effect (Class × Gender on Survival):")
    print(interaction_analysis)

    # Visualize interaction
    pivot = df.pivot_table(values='Survived', index='Pclass',
                           columns='Sex', aggfunc='mean')

    plt.figure(figsize=(10, 6))
    sns.heatmap(pivot, annot=True, cmap='RdYlGn', center=0.5,
                fmt='.3f', linewidths=1, cbar_kws={"label": "Survival Rate"})
    plt.title('Interaction Effect: Class × Gender')
    plt.xlabel('Gender')
    plt.ylabel('Passenger Class')
    plt.show()
    ```

[⬆️ Go to Context](#context)

---

## **Titanic Dataset EDA**

```py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Load dataset
df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
print(f"Dataset Shape: {df.shape}")
print(f"\nFirst 5 rows:\n{df.head()}")
```

### Univariate Analysis(Titanic)

```py
# === NUMERICAL VARIABLES ===
print("\n" + "="*50)
print("UNIVARIATE ANALYSIS - NUMERICAL VARIABLES")
print("="*50)

# Age Analysis
print("\nAge Statistics:")
print(df['Age'].describe())
print(f"Skewness: {df['Age'].skew():.3f}")
print(f"Kurtosis: {df['Age'].kurtosis():.3f}")
print(f"Missing: {df['Age'].isnull().sum()} ({df['Age'].isnull().sum()/len(df)*100:.1f}%)")

# Visualizations
fig, axes = plt.subplots(2, 3, figsize=(15, 10))

# Age
axes[0, 0].hist(df['Age'].dropna(), bins=30, edgecolor='black', alpha=0.7, color='skyblue')
axes[0, 0].axvline(df['Age'].mean(), color='red', linestyle='--', label='Mean')
axes[0, 0].axvline(df['Age'].median(), color='green', linestyle='--', label='Median')
axes[0, 0].set_xlabel('Age')
axes[0, 0].set_ylabel('Frequency')
axes[0, 0].set_title('Age Distribution')
axes[0, 0].legend()
axes[0, 0].grid(alpha=0.3)

axes[0, 1].boxplot(df['Age'].dropna())
axes[0, 1].set_ylabel('Age')
axes[0, 1].set_title('Age Box Plot')
axes[0, 1].grid(alpha=0.3)

df['Age'].dropna().plot(kind='density', ax=axes[0, 2], linewidth=2, color='purple')
axes[0, 2].set_xlabel('Age')
axes[0, 2].set_title('Age Density Plot')
axes[0, 2].grid(alpha=0.3)

# Fare
axes[1, 0].hist(df['Fare'], bins=30, edgecolor='black', alpha=0.7, color='coral')
axes[1, 0].set_xlabel('Fare')
axes[1, 0].set_ylabel('Frequency')
axes[1, 0].set_title('Fare Distribution')
axes[1, 0].grid(alpha=0.3)

axes[1, 1].boxplot(df['Fare'])
axes[1, 1].set_ylabel('Fare')
axes[1, 1].set_title('Fare Box Plot')
axes[1, 1].grid(alpha=0.3)

# Q-Q Plot for Age
stats.probplot(df['Age'].dropna(), dist="norm", plot=axes[1, 2])
axes[1, 2].set_title('Q-Q Plot for Age')
axes[1, 2].grid(alpha=0.3)

plt.tight_layout()
plt.show()

# === CATEGORICAL VARIABLES ===
print("\n" + "="*50)
print("UNIVARIATE ANALYSIS - CATEGORICAL VARIABLES")
print("="*50)

# Survival
print("\nSurvival Distribution:")
print(df['Survived'].value_counts())
print(f"\nSurvival Rate: {df['Survived'].mean()*100:.1f}%")

# Visualizations
fig, axes = plt.subplots(2, 3, figsize=(15, 10))

# Survival
axes[0, 0].bar([0, 1], df['Survived'].value_counts().sort_index(),
               color=['red', 'green'], edgecolor='black')
axes[0, 0].set_xlabel('Survived (0=No, 1=Yes)')
axes[0, 0].set_ylabel('Count')
axes[0, 0].set_title('Survival Distribution')
axes[0, 0].set_xticks([0, 1])
axes[0, 0].grid(axis='y', alpha=0.3)

# Passenger Class
df['Pclass'].value_counts().sort_index().plot(kind='bar', ax=axes[0, 1],
                                               color='skyblue', edgecolor='black')
axes[0, 1].set_xlabel('Passenger Class')
axes[0, 1].set_ylabel('Count')
axes[0, 1].set_title('Class Distribution')
axes[0, 1].set_xticklabels(['1st', '2nd', '3rd'], rotation=0)
axes[0, 1].grid(axis='y', alpha=0.3)

# Gender
df['Sex'].value_counts().plot(kind='pie', ax=axes[0, 2], autopct='%1.1f%%',
                               colors=['lightblue', 'pink'], startangle=90)
axes[0, 2].set_ylabel('')
axes[0, 2].set_title('Gender Distribution')

# Embarked
df['Embarked'].value_counts().plot(kind='bar', ax=axes[1, 0],
                                    color='lightgreen', edgecolor='black')
axes[1, 0].set_xlabel('Port of Embarkation')
axes[1, 0].set_ylabel('Count')
axes[1, 0].set_title('Embarkation Port Distribution')
axes[1, 0].set_xticklabels(['Southampton', 'Cherbourg', 'Queenstown'], rotation=45)
axes[1, 0].grid(axis='y', alpha=0.3)

# SibSp
df['SibSp'].value_counts().sort_index().plot(kind='bar', ax=axes[1, 1],
                                              color='orange', edgecolor='black')
axes[1, 1].set_xlabel('Number of Siblings/Spouses')
axes[1, 1].set_ylabel('Count')
axes[1, 1].set_title('Siblings/Spouses Distribution')
axes[1, 1].set_xticklabels(axes[1, 1].get_xticklabels(), rotation=0)
axes[1, 1].grid(axis='y', alpha=0.3)

# Parch
df['Parch'].value_counts().sort_index().plot(kind='bar', ax=axes[1, 2],
                                              color='purple', edgecolor='black')
axes[1, 2].set_xlabel('Number of Parents/Children')
axes[1, 2].set_ylabel('Count')
axes[1, 2].set_title('Parents/Children Distribution')
axes[1, 2].set_xticklabels(axes[1, 2].get_xticklabels(), rotation=0)
axes[1, 2].grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.show()

# Missing Values
print("\nMissing Values:")
missing = df.isnull().sum()
missing_pct = (missing / len(df)) * 100
missing_df = pd.DataFrame({'Count': missing, 'Percentage': missing_pct})
print(missing_df[missing_df['Count'] > 0])
```

### Bivariate Analysis(Titanic)

```py
print("\n" + "="*50)
print("BIVARIATE ANALYSIS")
print("="*50)

# === NUMERICAL VS NUMERICAL ===
print("\nNumerical vs Numerical:")
age_fare_corr = df['Age'].corr(df['Fare'])
print(f"Age vs Fare Correlation: {age_fare_corr:.3f}")

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Scatter plot
axes[0].scatter(df['Age'], df['Fare'], alpha=0.5, edgecolors='black')
axes[0].set_xlabel('Age')
axes[0].set_ylabel('Fare')
axes[0].set_title(f'Age vs Fare (r={age_fare_corr:.3f})')
axes[0].grid(alpha=0.3)

# Add regression line
from scipy.stats import linregress
valid_data = df[['Age', 'Fare']].dropna()
slope, intercept, r_value, p_value, std_err = linregress(valid_data['Age'], valid_data['Fare'])
line = slope * valid_data['Age'] + intercept
axes[0].plot(valid_data['Age'], line, color='red', linewidth=2,
             label=f'r²={r_value**2:.3f}')
axes[0].legend()

# Age vs SibSp
axes[1].scatter(df['SibSp'], df['Age'], alpha=0.5, edgecolors='black', color='green')
axes[1].set_xlabel('Siblings/Spouses')
axes[1].set_ylabel('Age')
axes[1].set_title('Siblings/Spouses vs Age')
axes[1].grid(alpha=0.3)

plt.tight_layout()
plt.show()

# === CATEGORICAL VS NUMERICAL ===
print("\nCategorical vs Numerical:")
print("\nAge by Survival Status:")
print(df.groupby('Survived')['Age'].describe())

# Statistical test
survived_ages = df[df['Survived'] == 1]['Age'].dropna()
died_ages = df[df['Survived'] == 0]['Age'].dropna()
t_stat, p_value = stats.ttest_ind(survived_ages, died_ages)
print(f"\nT-test: t={t_stat:.4f}, p={p_value:.4f}")

fig, axes = plt.subplots(2, 3, figsize=(15, 10))

# Age by Survival
df.boxplot(column='Age', by='Survived', ax=axes[0, 0], grid=False)
axes[0, 0].set_title('Age by Survival')
axes[0, 0].set_xlabel('Survived (0=No, 1=Yes)')
axes[0, 0].set_ylabel('Age')
plt.sca(axes[0, 0])
plt.xticks([1, 2], ['No', 'Yes'])

# Fare by Class
df.boxplot(column='Fare', by='Pclass', ax=axes[0, 1], grid=False)
axes[0, 1].set_title('Fare by Class')
axes[0, 1].set_xlabel('Passenger Class')
axes[0, 1].set_ylabel('Fare')

# Violin plot: Age by Class
sns.violinplot(x='Pclass', y='Age', data=df, ax=axes[0, 2], palette='Set2')
axes[0, 2].set_title('Age by Class (Violin)')
axes[0, 2].set_xlabel('Passenger Class')

# Fare by Survival
df.boxplot(column='Fare', by='Survived', ax=axes[1, 0], grid=False)
axes[1, 0].set_title('Fare by Survival')
axes[1, 0].set_xlabel('Survived (0=No, 1=Yes)')
axes[1, 0].set_ylabel('Fare')

# Age by Gender
sns.violinplot(x='Sex', y='Age', data=df, ax=axes[1, 1], palette='Set1')
axes[1, 1].set_title('Age by Gender')
axes[1, 1].set_xlabel('Gender')

# Fare by Gender
sns.violinplot(x='Sex', y='Fare', data=df, ax=axes[1, 2], palette='Set1')
axes[1, 2].set_title('Fare by Gender')
axes[1, 2].set_xlabel('Gender')

plt.tight_layout()
plt.show()

# === CATEGORICAL VS CATEGORICAL ===
print("\nCategorical vs Categorical:")
print("\nSurvival by Gender:")
survival_gender = pd.crosstab(df['Sex'], df['Survived'], normalize='index') * 100
print(survival_gender)

# Chi-square test
crosstab = pd.crosstab(df['Sex'], df['Survived'])
chi2, p_value, dof, expected = stats.chi2_contingency(crosstab)
print(f"\nChi-square test: χ²={chi2:.4f}, p={p_value:.4f}")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Survival by Gender - Grouped
crosstab.plot(kind='bar', ax=axes[0, 0], color=['red', 'green'], edgecolor='black')
axes[0, 0].set_xlabel('Gender')
axes[0, 0].set_ylabel('Count')
axes[0, 0].set_title('Survival Count by Gender')
axes[0, 0].legend(['Died', 'Survived'])
axes[0, 0].set_xticklabels(['Female', 'Male'], rotation=0)
axes[0, 0].grid(axis='y', alpha=0.3)

# Survival by Gender - Stacked
pd.crosstab(df['Sex'], df['Survived'], normalize='index').plot(
    kind='bar', stacked=True, ax=axes[0, 1], color=['red', 'green']
)
axes[0, 1].set_xlabel('Gender')
axes[0, 1].set_ylabel('Proportion')
axes[0, 1].set_title('Survival Rate by Gender (Stacked)')
axes[0, 1].legend(['Died', 'Survived'])
axes[0, 1].set_xticklabels(['Female', 'Male'], rotation=0)

# Survival by Class
pd.crosstab(df['Pclass'], df['Survived']).plot(
    kind='bar', ax=axes[1, 0], color=['red', 'green'], edgecolor='black'
)
axes[1, 0].set_xlabel('Passenger Class')
axes[1, 0].set_ylabel('Count')
axes[1, 0].set_title('Survival Count by Class')
axes[1, 0].legend(['Died', 'Survived'])
axes[1, 0].set_xticklabels(['1st', '2nd', '3rd'], rotation=0)
axes[1, 0].grid(axis='y', alpha=0.3)

# Class by Gender
pd.crosstab(df['Pclass'], df['Sex']).plot(
    kind='bar', ax=axes[1, 1], color=['pink', 'lightblue'], edgecolor='black'
)
axes[1, 1].set_xlabel('Passenger Class')
axes[1, 1].set_ylabel('Count')
axes[1, 1].set_title('Gender Distribution by Class')
axes[1, 1].legend(['Female', 'Male'])
axes[1, 1].set_xticklabels(['1st', '2nd', '3rd'], rotation=0)
axes[1, 1].grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.show()
```

### Multivariate Analysis(Titanic)

```py
print("\n" + "="*50)
print("MULTIVARIATE ANALYSIS")
print("="*50)

# === CORRELATION MATRIX ===
numerical_cols = ['Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare']
corr_matrix = df[numerical_cols].corr()

print("\nCorrelation Matrix:")
print(corr_matrix)

plt.figure(figsize=(12, 10))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0,
            square=True, linewidths=1, cbar_kws={"shrink": 0.8},
            fmt='.2f', vmin=-1, vmax=1)
plt.title('Correlation Heatmap - Titanic Dataset', fontsize=16)
plt.tight_layout()
plt.show()

# === PAIR PLOT ===
print("\nGenerating Pair Plot...")
sns.pairplot(df[['Age', 'Fare', 'Pclass', 'Survived']].dropna(),
             hue='Survived', diag_kind='kde',
             palette={0: 'red', 1: 'green'})
plt.suptitle('Pair Plot of Key Variables', y=1.02)
plt.show()

# === PIVOT TABLE ===
print("\nSurvival Rate by Class and Gender:")
pivot = df.pivot_table(values='Survived', index='Pclass',
                       columns='Sex', aggfunc='mean')
print(pivot)

plt.figure(figsize=(10, 6))
sns.heatmap(pivot, annot=True, cmap='RdYlGn', center=0.5,
            fmt='.3f', linewidths=1, cbar_kws={"label": "Survival Rate"})
plt.title('Survival Rate: Class × Gender', fontsize=14)
plt.xlabel('Gender')
plt.ylabel('Passenger Class')
plt.show()

# === GROUPED ANALYSIS ===
print("\nSurvival Statistics by Class and Gender:")
grouped = df.groupby(['Pclass', 'Sex'])['Survived'].agg([
    ('Count', 'count'),
    ('Survived', 'sum'),
    ('Rate', 'mean')
])
print(grouped)

# Visualize
survival_multi = df.groupby(['Pclass', 'Sex'])['Survived'].mean() * 100

plt.figure(figsize=(12, 6))
survival_multi.unstack().plot(kind='bar', color=['pink', 'lightblue'],
                               edgecolor='black')
plt.xlabel('Passenger Class', fontsize=12)
plt.ylabel('Survival Rate (%)', fontsize=12)
plt.title('Survival Rate by Class and Gender', fontsize=14)
plt.legend(title='Gender', labels=['Female', 'Male'])
plt.xticks(rotation=0)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()

# === FACET GRID ===
g = sns.FacetGrid(df, col='Pclass', row='Survived', height=3, aspect=1.2)
g.map(plt.hist, 'Age', bins=20, edgecolor='black', alpha=0.7, color='skyblue')
g.add_legend()
g.fig.suptitle('Age Distribution by Class and Survival', y=1.02, fontsize=14)
plt.show()

# === 3D SCATTER PLOT ===
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

colors = ['red' if s == 0 else 'green' for s in df['Survived']]
scatter = ax.scatter(df['Age'], df['Fare'], df['Pclass'],
                     c=colors, alpha=0.6, s=50, edgecolors='black')

ax.set_xlabel('Age', fontsize=12)
ax.set_ylabel('Fare', fontsize=12)
ax.set_zlabel('Pclass', fontsize=12)
ax.set_title('3D Scatter: Age vs Fare vs Class (colored by Survival)', fontsize=14)

from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], marker='o', color='w', markerfacecolor='r',
           markersize=10, label='Died'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='g',
           markersize=10, label='Survived')
]
ax.legend(handles=legend_elements, loc='upper right')
plt.show()

# === INTERACTION EFFECTS ===
print("\nInteraction Effects:")
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
df['IsAlone'] = (df['FamilySize'] == 1).astype(int)

print("\nSurvival by Family Size:")
print(df.groupby('FamilySize')['Survived'].agg(['count', 'mean']))

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Family Size effect
df.groupby('FamilySize')['Survived'].mean().plot(kind='bar', ax=axes[0],
                                                  color='skyblue', edgecolor='black')
axes[0].set_xlabel('Family Size')
axes[0].set_ylabel('Survival Rate')
axes[0].set_title('Survival Rate by Family Size')
axes[0].set_xticklabels(axes[0].get_xticklabels(), rotation=0)
axes[0].grid(axis='y', alpha=0.3)

# Alone vs Not Alone
pd.crosstab(df['IsAlone'], df['Survived'], normalize='index').plot(
    kind='bar', ax=axes[1], color=['red', 'green'], edgecolor='black'
)
axes[1].set_xlabel('Traveling Status')
axes[1].set_ylabel('Proportion')
axes[1].set_title('Survival Rate: Alone vs With Family')
axes[1].set_xticklabels(['With Family', 'Alone'], rotation=0)
axes[1].legend(['Died', 'Survived'])
axes[1].grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.show()

# === KEY INSIGHTS ===
print("\n" + "="*50)
print("KEY INSIGHTS FROM EDA")
print("="*50)

print("\n1. UNIVARIATE INSIGHTS:")
print(f"   - Average Age: {df['Age'].mean():.1f} years")
print(f"   - Overall Survival Rate: {df['Survived'].mean()*100:.1f}%")
print(f"   - Most passengers in Class: {df['Pclass'].mode()[0]}")
print(f"   - Age is slightly right-skewed (Skewness: {df['Age'].skew():.2f})")

print("\n2. BIVARIATE INSIGHTS:")
female_survival = df[df['Sex']=='female']['Survived'].mean()*100
male_survival = df[df['Sex']=='male']['Survived'].mean()*100
print(f"   - Female survival rate: {female_survival:.1f}%")
print(f"   - Male survival rate: {male_survival:.1f}%")
print(f"   - Class 1 survival rate: {df[df['Pclass']==1]['Survived'].mean()*100:.1f}%")
print(f"   - Class 3 survival rate: {df[df['Pclass']==3]['Survived'].mean()*100:.1f}%")

print("\n3. MULTIVARIATE INSIGHTS:")
best = df[(df['Sex']=='female') & (df['Pclass']==1)]['Survived'].mean()*100
worst = df[(df['Sex']=='male') & (df['Pclass']==3)]['Survived'].mean()*100
print(f"   - Best survival: Female in Class 1 ({best:.1f}%)")
print(f"   - Worst survival: Male in Class 3 ({worst:.1f}%)")
print(f"   - Fare and Pclass are negatively correlated (r={df['Fare'].corr(df['Pclass']):.3f})")
optimal_family = df.groupby('FamilySize')['Survived'].mean().idxmax()
print(f"   - Optimal family size for survival: {optimal_family}")

print("\n" + "="*50)
```

[⬆️ Go to Context](#context)

## **Advanced EDA Techniques**

### Data Quality Assessment

- **Duplicate Detection**: Identify and handle duplicate records
  - **Purpose**: Ensure data integrity, avoid bias in analysis
  - **Where used**: Data cleaning, preprocessing

    ```py
    # Check duplicates
    duplicates = df.duplicated().sum()
    print(f"Number of duplicate rows: {duplicates}")

    # Find duplicate rows
    duplicate_rows = df[df.duplicated(keep=False)]
    print(f"\nDuplicate records:\n{duplicate_rows}")

    # Check duplicates on specific columns
    dup_subset = df.duplicated(subset=['Name', 'Age', 'Ticket'], keep=False).sum()
    print(f"Duplicates based on Name, Age, Ticket: {dup_subset}")

    # Remove duplicates
    df_clean = df.drop_duplicates()
    print(f"Rows after removing duplicates: {len(df_clean)}")
    ```

- **Data Type Verification**: Ensure correct data types
  - **Purpose**: Prevent errors in analysis, optimize memory
  - **Where used**: Data validation, preprocessing

    ```py
    # Check data types
    print("Data Types:")
    print(df.dtypes)

    # Check memory usage
    print(f"\nMemory Usage:\n{df.memory_usage(deep=True)}")

    # Convert data types
    df['Pclass'] = df['Pclass'].astype('category')
    df['Sex'] = df['Sex'].astype('category')
    df['Embarked'] = df['Embarked'].astype('category')

    # Verify conversion
    print(f"\nMemory after conversion:\n{df.memory_usage(deep=True)}")
    ```

- **Cardinality Check**: Count unique values per variable
  - **Purpose**: Understand variable granularity, identify categorical vs numerical
  - **Where used**: Feature engineering decisions

    ```py
    # Unique value counts
    cardinality = pd.DataFrame({
        'Column': df.columns,
        'Unique_Values': [df[col].nunique() for col in df.columns],
        'Unique_Percentage': [df[col].nunique()/len(df)*100 for col in df.columns]
    })
    print(cardinality.sort_values('Unique_Values', ascending=False))

    # Identify high cardinality columns
    high_cardinality = cardinality[cardinality['Unique_Values'] > 50]
    print(f"\nHigh cardinality columns:\n{high_cardinality}")
    ```

- **Constant and Quasi-Constant Features**: Identify low-variance features
  - **Purpose**: Remove uninformative features
  - **Where used**: Feature selection, dimensionality reduction

    ```py
    # Constant features (all same value)
    constant_features = [col for col in df.columns
                        if df[col].nunique() == 1]
    print(f"Constant features: {constant_features}")

    # Quasi-constant features (>99% same value)
    quasi_constant = []
    threshold = 0.99
    for col in df.columns:
        if df[col].dtype in ['int64', 'float64', 'object', 'category']:
            predominant = (df[col].value_counts().iloc[0] / len(df))
            if predominant > threshold:
                quasi_constant.append(col)
    print(f"Quasi-constant features: {quasi_constant}")
    ```

[⬆️ Go to Context](#context)

### Outlier Analysis

- **Z-Score Method**: Identify outliers using standard deviations
  - **Formula**: z = (x - μ) / σ
  - **Threshold**: |z| > 3 typically considered outlier
  - **Where used**: Numerical outlier detection

    ```py
    from scipy import stats

    # Calculate Z-scores
    z_scores = np.abs(stats.zscore(df['Age'].dropna()))

    # Identify outliers (|z| > 3)
    outliers_z = df['Age'][z_scores > 3]
    print(f"Outliers using Z-score method: {len(outliers_z)}")
    print(outliers_z)

    # Visualize
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.scatter(range(len(df['Age'].dropna())), df['Age'].dropna(), alpha=0.5)
    plt.scatter(np.where(z_scores > 3)[0], outliers_z, color='red', label='Outliers')
    plt.xlabel('Index')
    plt.ylabel('Age')
    plt.title('Outliers using Z-Score Method')
    plt.legend()
    plt.grid(alpha=0.3)

    plt.subplot(1, 2, 2)
    plt.hist(z_scores, bins=30, edgecolor='black', alpha=0.7)
    plt.axvline(3, color='red', linestyle='--', label='Threshold')
    plt.axvline(-3, color='red', linestyle='--')
    plt.xlabel('Z-Score')
    plt.ylabel('Frequency')
    plt.title('Distribution of Z-Scores')
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()
    ```

- **IQR Method**: Identify outliers using quartiles
  - **Formula**: Lower = Q1 - 1.5×IQR, Upper = Q3 + 1.5×IQR
  - **Where used**: Robust outlier detection, less sensitive to extreme values

    ```py
    # Calculate IQR
    Q1 = df['Fare'].quantile(0.25)
    Q3 = df['Fare'].quantile(0.75)
    IQR = Q3 - Q1

    # Define bounds
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Identify outliers
    outliers_iqr = df[(df['Fare'] < lower_bound) | (df['Fare'] > upper_bound)]
    print(f"Outliers using IQR method: {len(outliers_iqr)}")
    print(f"Lower bound: {lower_bound:.2f}, Upper bound: {upper_bound:.2f}")

    # Visualize
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.boxplot(df['Fare'], vert=True)
    plt.ylabel('Fare')
    plt.title('Box Plot with Outliers')
    plt.grid(alpha=0.3)

    plt.subplot(1, 2, 2)
    plt.scatter(df.index, df['Fare'], alpha=0.5, label='Normal')
    plt.scatter(outliers_iqr.index, outliers_iqr['Fare'],
                color='red', alpha=0.7, label='Outliers')
    plt.axhline(lower_bound, color='green', linestyle='--', label='Bounds')
    plt.axhline(upper_bound, color='green', linestyle='--')
    plt.xlabel('Index')
    plt.ylabel('Fare')
    plt.title('Fare with IQR Outliers Highlighted')
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()
    ```

- **Isolation Forest**: Machine learning approach for outlier detection
  - **Purpose**: Detect outliers in multivariate data
  - **Where used**: Anomaly detection, fraud detection

    ```py
    from sklearn.ensemble import IsolationForest

    # Prepare data
    features = df[['Age', 'Fare', 'SibSp', 'Parch']].dropna()

    # Fit Isolation Forest
    iso_forest = IsolationForest(contamination=0.1, random_state=42)
    outliers_if = iso_forest.fit_predict(features)

    # -1 indicates outlier, 1 indicates normal
    outlier_indices = features[outliers_if == -1].index
    print(f"Outliers detected: {len(outlier_indices)}")

    # Visualize
    plt.figure(figsize=(10, 6))
    plt.scatter(features['Age'], features['Fare'],
                c=outliers_if, cmap='coolwarm', alpha=0.6, edgecolors='black')
    plt.xlabel('Age')
    plt.ylabel('Fare')
    plt.title('Outliers Detected using Isolation Forest')
    plt.colorbar(label='Outlier (-1) / Normal (1)')
    plt.grid(alpha=0.3)
    plt.show()
    ```

- **Local Outlier Factor (LOF)**: Density-based outlier detection
  - **Purpose**: Identify outliers based on local density
  - **Where used**: Anomaly detection in complex distributions

    ```py
    from sklearn.neighbors import LocalOutlierFactor

    # Fit LOF
    lof = LocalOutlierFactor(n_neighbors=20, contamination=0.1)
    outliers_lof = lof.fit_predict(features)

    # Get outlier scores
    outlier_scores = lof.negative_outlier_factor_

    print(f"Outliers detected: {(outliers_lof == -1).sum()}")

    # Visualize
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.scatter(features['Age'], features['Fare'],
                c=outliers_lof, cmap='coolwarm', alpha=0.6, edgecolors='black')
    plt.xlabel('Age')
    plt.ylabel('Fare')
    plt.title('Outliers using Local Outlier Factor')
    plt.colorbar(label='Outlier (-1) / Normal (1)')
    plt.grid(alpha=0.3)

    plt.subplot(1, 2, 2)
    plt.hist(outlier_scores, bins=30, edgecolor='black', alpha=0.7)
    plt.xlabel('LOF Score')
    plt.ylabel('Frequency')
    plt.title('Distribution of LOF Scores')
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()
    ```

[⬆️ Go to Context](#context)

### Distribution Analysis

- **Normality Tests**: Test if data follows normal distribution
  - **Tests**: Shapiro-Wilk, Kolmogorov-Smirnov, Anderson-Darling
  - **Where used**: Statistical test assumptions, transformation decisions

    ```py
    from scipy.stats import shapiro, normaltest, kstest, anderson

    # Shapiro-Wilk test (best for n < 5000)
    stat, p_value = shapiro(df['Age'].dropna())
    print(f"Shapiro-Wilk Test: statistic={stat:.4f}, p-value={p_value:.4f}")
    if p_value > 0.05:
        print("Data appears normally distributed")
    else:
        print("Data does NOT appear normally distributed")

    # D'Agostino-Pearson test
    stat, p_value = normaltest(df['Age'].dropna())
    print(f"\nD'Agostino-Pearson Test: statistic={stat:.4f}, p-value={p_value:.4f}")

    # Anderson-Darling test
    result = anderson(df['Age'].dropna())
    print(f"\nAnderson-Darling Test: statistic={result.statistic:.4f}")
    for i in range(len(result.critical_values)):
        sl, cv = result.significance_level[i], result.critical_values[i]
        if result.statistic < cv:
            print(f"  {sl}%: Data looks normal (stat < {cv:.3f})")
        else:
            print(f"  {sl}%: Data does NOT look normal (stat >= {cv:.3f})")
    ```

- **Distribution Fitting**: Fit data to theoretical distributions
  - **Purpose**: Understand underlying data generation process
  - **Where used**: Probability modeling, simulation

    ```py
    from scipy import stats

    # Fit multiple distributions
    data = df['Age'].dropna()
    distributions = [stats.norm, stats.expon, stats.gamma, stats.lognorm]

    best_dist = None
    best_params = None
    best_sse = np.inf

    for dist in distributions:
        # Fit distribution
        params = dist.fit(data)

        # Calculate SSE
        arg = params[:-2]
        loc = params[-2]
        scale = params[-1]
        pdf = dist.pdf(data, loc=loc, scale=scale, *arg)
        sse = np.sum((pdf - data)**2)

        if sse < best_sse:
            best_dist = dist
            best_params = params
            best_sse = sse

        print(f"{dist.name}: SSE={sse:.4f}")

    print(f"\nBest fit: {best_dist.name}")

    # Plot best fit
    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=30, density=True, alpha=0.7,
             edgecolor='black', label='Data')

    x = np.linspace(data.min(), data.max(), 100)
    pdf = best_dist.pdf(x, *best_params)
    plt.plot(x, pdf, 'r-', linewidth=2,
             label=f'{best_dist.name} fit')

    plt.xlabel('Age')
    plt.ylabel('Density')
    plt.title('Distribution Fitting')
    plt.legend()
    plt.grid(alpha=0.3)
    plt.show()
    ```

- **Probability Plots**: Visual assessment of distribution
  - **Purpose**: Visually check if data follows theoretical distribution
  - **Where used**: Distribution validation

    ```py
    from scipy import stats

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Normal Q-Q plot
    stats.probplot(df['Age'].dropna(), dist="norm", plot=axes[0, 0])
    axes[0, 0].set_title('Normal Q-Q Plot - Age')
    axes[0, 0].grid(alpha=0.3)

    # Exponential Q-Q plot
    stats.probplot(df['Fare'].dropna(), dist="expon", plot=axes[0, 1])
    axes[0, 1].set_title('Exponential Q-Q Plot - Fare')
    axes[0, 1].grid(alpha=0.3)

    # Histogram with normal curve
    age_data = df['Age'].dropna()
    mu, sigma = age_data.mean(), age_data.std()
    axes[1, 0].hist(age_data, bins=30, density=True, alpha=0.7, edgecolor='black')
    x = np.linspace(age_data.min(), age_data.max(), 100)
    axes[1, 0].plot(x, stats.norm.pdf(x, mu, sigma), 'r-', linewidth=2)
    axes[1, 0].set_xlabel('Age')
    axes[1, 0].set_ylabel('Density')
    axes[1, 0].set_title('Age Distribution with Normal Curve')
    axes[1, 0].grid(alpha=0.3)

    # Cumulative distribution
    sorted_data = np.sort(age_data)
    y = np.arange(1, len(sorted_data)+1) / len(sorted_data)
    axes[1, 1].plot(sorted_data, y, marker='.', linestyle='none', alpha=0.5)
    axes[1, 1].plot(x, stats.norm.cdf(x, mu, sigma), 'r-', linewidth=2)
    axes[1, 1].set_xlabel('Age')
    axes[1, 1].set_ylabel('Cumulative Probability')
    axes[1, 1].set_title('Empirical vs Theoretical CDF')
    axes[1, 1].grid(alpha=0.3)

    plt.tight_layout()
    plt.show()
    ```

[⬆️ Go to Context](#context)

### Feature Engineering for EDA

- **Binning (Discretization)**: Convert continuous to categorical
  - **Purpose**: Simplify analysis, handle non-linear relationships
  - **Where used**: Age groups, income brackets

    ```py
    # Equal-width binning
    df['Age_Bins'] = pd.cut(df['Age'], bins=5)
    print(df['Age_Bins'].value_counts().sort_index())

    # Custom bins
    bins = [0, 18, 35, 60, 100]
    labels = ['Child', 'Young Adult', 'Adult', 'Senior']
    df['Age_Group'] = pd.cut(df['Age'], bins=bins, labels=labels)

    print("\nAge Group Distribution:")
    print(df['Age_Group'].value_counts())

    # Quantile-based binning
    df['Fare_Quartile'] = pd.qcut(df['Fare'], q=4,
                                   labels=['Q1', 'Q2', 'Q3', 'Q4'])

    # Visualize
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    df['Age_Group'].value_counts().plot(kind='bar', color='skyblue', edgecolor='black')
    plt.xlabel('Age Group')
    plt.ylabel('Count')
    plt.title('Age Group Distribution')
    plt.xticks(rotation=45)
    plt.grid(axis='y', alpha=0.3)

    plt.subplot(1, 2, 2)
    survival_by_age = df.groupby('Age_Group')['Survived'].mean() * 100
    survival_by_age.plot(kind='bar', color='coral', edgecolor='black')
    plt.xlabel('Age Group')
    plt.ylabel('Survival Rate (%)')
    plt.title('Survival Rate by Age Group')
    plt.xticks(rotation=45)
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.show()
    ```

- **Feature Creation**: Derive new features from existing ones
  - **Purpose**: Extract hidden patterns, improve analysis
  - **Where used**: Domain-specific features

    ```py
    # Create new features
    df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
    df['IsAlone'] = (df['FamilySize'] == 1).astype(int)
    df['Title'] = df['Name'].str.extract(' ([A-Za-z]+)\.', expand=False)
    df['Deck'] = df['Cabin'].str[0]
    df['Fare_Per_Person'] = df['Fare'] / df['FamilySize']
    df['Age_Class'] = df['Age'] * df['Pclass']

    # Analyze new features
    print("Title Distribution:")
    print(df['Title'].value_counts())

    print("\nSurvival by Title:")
    print(df.groupby('Title')['Survived'].agg(['count', 'mean']))

    # Visualize
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Family Size
    df['FamilySize'].value_counts().sort_index().plot(kind='bar',
                                                       ax=axes[0, 0],
                                                       color='lightgreen',
                                                       edgecolor='black')
    axes[0, 0].set_xlabel('Family Size')
    axes[0, 0].set_ylabel('Count')
    axes[0, 0].set_title('Family Size Distribution')
    axes[0, 0].grid(axis='y', alpha=0.3)

    # Survival by Family Size
    df.groupby('FamilySize')['Survived'].mean().plot(kind='bar',
                                                      ax=axes[0, 1],
                                                      color='orange',
                                                      edgecolor='black')
    axes[0, 1].set_xlabel('Family Size')
    axes[0, 1].set_ylabel('Survival Rate')
    axes[0, 1].set_title('Survival Rate by Family Size')
    axes[0, 1].grid(axis='y', alpha=0.3)

    # Title distribution
    df['Title'].value_counts().head(10).plot(kind='barh',
                                              ax=axes[1, 0],
                                              color='purple',
                                              edgecolor='black')
    axes[1, 0].set_xlabel('Count')
    axes[1, 0].set_ylabel('Title')
    axes[1, 0].set_title('Top 10 Titles')
    axes[1, 0].grid(axis='x', alpha=0.3)

    # Fare per person
    axes[1, 1].hist(df['Fare_Per_Person'].dropna(), bins=30,
                    edgecolor='black', alpha=0.7, color='pink')
    axes[1, 1].set_xlabel('Fare Per Person')
    axes[1, 1].set_ylabel('Frequency')
    axes[1, 1].set_title('Fare Per Person Distribution')
    axes[1, 1].grid(alpha=0.3)

    plt.tight_layout()
    plt.show()
    ```

- **Encoding Categorical Variables**: Convert categories to numbers
  - **Types**: Label encoding, one-hot encoding, ordinal encoding
  - **Where used**: Preparing data for correlation, modeling

    ```py
    # Label Encoding
    from sklearn.preprocessing import LabelEncoder

    le = LabelEncoder()
    df['Sex_Encoded'] = le.fit_transform(df['Sex'])
    print("Label Encoding (Sex):")
    print(df[['Sex', 'Sex_Encoded']].drop_duplicates())

    # One-Hot Encoding
    embarked_dummies = pd.get_dummies(df['Embarked'], prefix='Embarked', drop_first=False)
    df_encoded = pd.concat([df, embarked_dummies], axis=1)

    print("\nOne-Hot Encoding (Embarked):")
    print(df_encoded[['Embarked', 'Embarked_C', 'Embarked_Q', 'Embarked_S']].head())

    # Ordinal Encoding (for ordered categories)
    pclass_mapping = {1: 'High', 2: 'Medium', 3: 'Low'}
    df['Pclass_Ordinal'] = df['Pclass'].map(pclass_mapping)

    # Visualize correlations after encoding
    encoded_cols = ['Survived', 'Pclass', 'Sex_Encoded', 'Age', 'Fare']
    corr_encoded = df[encoded_cols].corr()

    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_encoded, annot=True, cmap='coolwarm', center=0,
                square=True, linewidths=1, fmt='.2f')
    plt.title('Correlation Matrix with Encoded Variables')
    plt.tight_layout()
    plt.show()
    ```

- **Transformation**: Apply mathematical functions to data
  - **Types**: Log, square root, Box-Cox, power transforms
  - **Where used**: Normalizing skewed distributions

    ```py
    from scipy.stats import boxcox

    # Original distribution
    fare_original = df['Fare'].dropna()

    # Log transformation
    fare_log = np.log1p(fare_original)  # log(1 + x) to handle zeros

    # Square root transformation
    fare_sqrt = np.sqrt(fare_original)

    # Box-Cox transformation
    fare_boxcox, lambda_param = boxcox(fare_original + 1)  # +1 to handle zeros

    # Compare distributions
    fig, axes = plt.subplots(2, 4, figsize=(16, 8))

    # Original
    axes[0, 0].hist(fare_original, bins=30, edgecolor='black', alpha=0.7)
    axes[0, 0].set_title(f'Original (Skew: {fare_original.skew():.2f})')
    axes[0, 0].set_xlabel('Fare')
    axes[1, 0].boxplot(fare_original)
    axes[1, 0].set_title('Original Box Plot')

    # Log
    axes[0, 1].hist(fare_log, bins=30, edgecolor='black', alpha=0.7, color='orange')
    axes[0, 1].set_title(f'Log (Skew: {fare_log.skew():.2f})')
    axes[0, 1].set_xlabel('Log(Fare)')
    axes[1, 1].boxplot(fare_log)
    axes[1, 1].set_title('Log Box Plot')

    # Square root
    axes[0, 2].hist(fare_sqrt, bins=30, edgecolor='black', alpha=0.7, color='green')
    axes[0, 2].set_title(f'Sqrt (Skew: {fare_sqrt.skew():.2f})')
    axes[0, 2].set_xlabel('√Fare')
    axes[1, 2].boxplot(fare_sqrt)
    axes[1, 2].set_title('Sqrt Box Plot')

    # Box-Cox
    axes[0, 3].hist(fare_boxcox, bins=30, edgecolor='black', alpha=0.7, color='purple')
    axes[0, 3].set_title(f'Box-Cox (Skew: {fare_boxcox.skew():.2f}, λ={lambda_param:.2f})')
    axes[0, 3].set_xlabel('Transformed Fare')
    axes[1, 3].boxplot(fare_boxcox)
    axes[1, 3].set_title('Box-Cox Box Plot')

    plt.tight_layout()
    plt.show()

    print(f"Original Skewness: {fare_original.skew():.3f}")
    print(f"Log Skewness: {fare_log.skew():.3f}")
    print(f"Sqrt Skewness: {fare_sqrt.skew():.3f}")
    print(f"Box-Cox Skewness: {fare_boxcox.skew():.3f}")
    ```

[⬆️ Go to Context](#context)

### Time-Based Analysis (if applicable)

- **Temporal Patterns**: Analyze patterns over time
  - **Purpose**: Identify trends, seasonality, cycles
  - **Where used**: Time series data, temporal features

    ```py
    # Note: Titanic dataset doesn't have explicit time data,
    # but we can demonstrate with simulated dates

    # Simulate boarding dates
    np.random.seed(42)
    start_date = pd.to_datetime('1912-04-10')
    df['Boarding_Date'] = pd.date_range(start=start_date, periods=len(df), freq='H')

    # Extract temporal features
    df['Boarding_Hour'] = df['Boarding_Date'].dt.hour
    df['Boarding_Day'] = df['Boarding_Date'].dt.day_name()
    df['Boarding_Month'] = df['Boarding_Date'].dt.month

    # Analyze by time
    plt.figure(figsize=(14, 5))

    plt.subplot(1, 2, 1)
    df.groupby('Boarding_Hour')['Survived'].mean().plot(kind='line',
                                                         marker='o', linewidth=2)
    plt.xlabel('Hour of Day')
    plt.ylabel('Survival Rate')
    plt.title('Survival Rate by Boarding Hour')
    plt.grid(alpha=0.3)

    plt.subplot(1, 2, 2)
    hourly_counts = df['Boarding_Hour'].value_counts().sort_index()
    hourly_counts.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.xlabel('Hour of Day')
    plt.ylabel('Number of Passengers')
    plt.title('Passenger Boarding by Hour')
    plt.xticks(rotation=45)
    plt.grid(axis='y', alpha=0.3)

    plt.tight_layout()
    plt.show()
    ```

[⬆️ Go to Context](#context)

### Segmentation Analysis

- **Customer/Data Segmentation**: Group similar records
  - **Purpose**: Identify distinct groups, targeted analysis
  - **Where used**: Market segmentation, personalization

    ```py
    from sklearn.cluster import KMeans
    from sklearn.preprocessing import StandardScaler

    # Prepare features for clustering
    cluster_features = df[['Age', 'Fare', 'FamilySize']].dropna()
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(cluster_features)

    # Elbow method to find optimal clusters
    inertias = []
    K_range = range(2, 10)
    for k in K_range:
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(features_scaled)
        inertias.append(kmeans.inertia_)

    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.plot(K_range, inertias, marker='o', linewidth=2)
    plt.xlabel('Number of Clusters (k)')
    plt.ylabel('Inertia')
    plt.title('Elbow Method for Optimal k')
    plt.grid(alpha=0.3)

    # Apply K-Means with optimal k
    optimal_k = 3
    kmeans = KMeans(n_clusters=optimal_k, random_state=42)
    cluster_features['Cluster'] = kmeans.fit_predict(features_scaled)

    # Visualize clusters
    plt.subplot(1, 2, 2)
    scatter = plt.scatter(cluster_features['Age'], cluster_features['Fare'],
                         c=cluster_features['Cluster'], cmap='viridis',
                         alpha=0.6, edgecolors='black')
    plt.xlabel('Age')
    plt.ylabel('Fare')
    plt.title(f'Passenger Segments (k={optimal_k})')
    plt.colorbar(scatter, label='Cluster')
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()

    # Analyze clusters
    print("Cluster Characteristics:")
    cluster_summary = cluster_features.groupby('Cluster').agg({
        'Age': ['mean', 'std'],
        'Fare': ['mean', 'std'],
        'FamilySize': ['mean', 'std']
    })
    print(cluster_summary)
    ```

[⬆️ Go to Context](#context)

### Comprehensive EDA Report

```py
# === COMPLETE EDA SUMMARY REPORT ===
print("="*70)
print(" "*20 + "TITANIC DATASET - EDA REPORT")
print("="*70)

print("\n1. DATASET OVERVIEW")
print("-" * 70)
print(f"Total Records: {len(df)}")
print(f"Total Features: {df.shape[1]}")
print(f"Memory Usage: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
print(f"Duplicates: {df.duplicated().sum()}")

print("\n2. DATA QUALITY")
print("-" * 70)
missing_summary = pd.DataFrame({
    'Missing_Count': df.isnull().sum(),
    'Missing_Percent': (df.isnull().sum() / len(df) * 100).round(2)
})
print(missing_summary[missing_summary['Missing_Count'] > 0])

print("\n3. NUMERICAL VARIABLES SUMMARY")
print("-" * 70)
print(df.describe().T)

print("\n4. CATEGORICAL VARIABLES SUMMARY")
print("-" * 70)
for col in df.select_dtypes(include=['object', 'category']).columns[:5]:
    print(f"\n{col}:")
    print(df[col].value_counts().head())

print("\n5. KEY CORRELATIONS")
print("-" * 70)
numerical_cols = df.select_dtypes(include=[np.number]).columns
corr_with_survived = df[numerical_cols].corr()['Survived'].sort_values(ascending=False)
print(corr_with_survived)

print("\n6. SURVIVAL ANALYSIS")
print("-" * 70)
print(f"Overall Survival Rate: {df['Survived'].mean()*100:.2f}%")
print(f"\nBy Gender:")
print(df.groupby('Sex')['Survived'].agg(['count', 'sum', 'mean']))
print(f"\nBy Class:")
print(df.groupby('Pclass')['Survived'].agg(['count', 'sum', 'mean']))

print("\n7. OUTLIER DETECTION SUMMARY")
print("-" * 70)
for col in ['Age', 'Fare']:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    outliers = df[(df[col] < Q1 - 1.5*IQR) | (df[col] > Q3 + 1.5*IQR)]
    print(f"{col}: {len(outliers)} outliers ({len(outliers)/len(df)*100:.2f}%)")

print("\n8. DISTRIBUTION NORMALITY")
print("-" * 70)
for col in ['Age', 'Fare']:
    stat, p_value = shapiro(df[col].dropna())
    result = "Normal" if p_value > 0.05 else "Not Normal"
    print(f"{col}: {result} (p-value: {p_value:.4f})")

print("\n9. TOP INSIGHTS")
print("-" * 70)
print(f"✓ Women had {df[df['Sex']=='female']['Survived'].mean()*100:.1f}% survival rate")
print(f"✓ Men had {df[df['Sex']=='male']['Survived'].mean()*100:.1f}% survival rate")
print(f"✓ 1st class: {df[df['Pclass']==1]['Survived'].mean()*100:.1f}% survival")
print(f"✓ 3rd class: {df[df['Pclass']==3]['Survived'].mean()*100:.1f}% survival")
print(f"✓ Children (<18): {df[df['Age']<18]['Survived'].mean()*100:.1f}% survival")
print(f"✓ Adults (>=18): {df[df['Age']>=18]['Survived'].mean()*100:.1f}% survival")
optimal_family = df.groupby('FamilySize')['Survived'].mean().idxmax()
print(f"✓ Optimal family size for survival: {optimal_family} members")

print("\n" + "="*70)
print("END OF EDA REPORT")
print("="*70)
```

[⬆️ Go to Context](#context)

# [**Day 45 - Bivariate and Multivariate Analysis in EDA**](./Day%2045%20-%20Bivariate%20and%20Multivariate%20Analysis%20in%20EDA/)

## **Bivariate and Multivariate Analysis**

- [Bivariate Analysis](#bivariate-analysis)
- [Multivariate Analysis](#multivariate-analysis)

[⬆️ Go to Context](#context)

## **Automatic Analysis**

- **[ydata-profiling](https://pypi.org/project/ydata-profiling/) ([pandas-profiling](https://pypi.org/project/pandas-profiling/))**: Complete Statistical Profiling (Single Dataset)

  - Generates a detailed HTML report
  - Includes:
    - Descriptive statistics
    - Missing value analysis
    - Correlation matrices
    - Duplicates detection
    - Sample rows
    - Feature interactions
  - Ideal as the first step before model building

    ```py
    from ydata_profiling import ProfileReport

    profile = ProfileReport(df, title="EDA Report", explorative=True)
    profile.to_file("ydata_report.html")
    ```

- **[Sweetviz](https://pypi.org/project/sweetviz/)**: Dataset Comparison & Target Analysis

  - High-density visual HTML reports
  - Strong for:

    - Train vs Test comparison
    - Before vs After cleaning comparison
    - Target variable analysis
  - Useful for detecting data drift and leakage

    ```py
    import sweetviz as sv

    report = sv.analyze([df, "Dataset"])
    report.show_html("sweetviz_report.html")
    ```

  - Comparison example:

    ```py
    report = sv.compare(
        [train_df, "Train"],
        [test_df, "Test"],
        "Target_Column"
    )

    report.show_html("comparison_report.html")
    ```

- **[DataPrep](https://pypi.org/project/dataprep/) (dataprep.eda)**: Faster Reports on Larger DataFrames

  - Clean, modern interactive report
  - Good performance on medium/large datasets
  - Programmatic API control

    ```py
    from dataprep.eda import create_report

    create_report(df).show_browser()
    ```

- **[Lux](https://pypi.org/project/lux/)**: Automatic Visualization Suggestions in Jupyter

  - Works directly inside Jupyter Notebook
  - Automatically suggests meaningful visualizations
  - No need to manually define plots

    ```py
    import lux

    df  # Just displaying df shows visualization recommendations
    ```

  - To guide Lux:

    ```py
    df.intent = ["age", "salary"]
    df
    ```

- **[D-Tale](https://pypi.org/project/dtale/)** Interactive Spreadsheet-Like Exploration

  - Browser-based GUI
  - Filter, sort, group
  - Visualize columns
  - Generates Python code from UI actions
  - Helpful for messy datasets

    ```py
    import dtale

    d = dtale.show(df)
    d.open_browser()
    ```

- **[AutoViz](https://pypi.org/project/autoviz/)**: Automatic Visual Storytelling

  - Automatically selects impactful charts
  - Generates:

    - Scatter plots
    - Box plots
    - Violin plots
    - Histograms
    - Heatmaps
  - Handles larger datasets with sampling

    ```py
    from autoviz.AutoViz_Class import AutoViz_Class

    AV = AutoViz_Class()
    AV.AutoViz("", dfte=df)
    ```

- **[PandasGUI](https://pypi.org/project/pandasgui/)**: No-Code Interactive GUI

  - Desktop-style GUI for DataFrames
  - Browse, filter, sort
  - Create plots visually
  - Good for exploratory inspection

    ```py
    from pandasgui import show

    show(df)
    ```

- All tools compare

  | Package             | Strength           | Best Use Case                           |
  | ------------------- | ------------------ | --------------------------------------- |
  | **ydata-profiling** | Deep statistics    | Full statistical overview of a dataset  |
  | **Sweetviz**        | Comparison-focused | Train/Test comparison & target analysis |
  | **DataPrep**        | Performance        | Faster reports for larger datasets      |
  | **Lux**             | Notebook visuals   | Auto chart suggestions inside Jupyter   |
  | **D-Tale**          | Interactive GUI    | Manual exploration & cleaning           |
  | **AutoViz**         | Chart diversity    | Quick visual discovery                  |
  | **PandasGUI**       | No-code interface  | GUI-based exploration                   |

[⬆️ Go to Context](#context)

# **Day 46 - EDA Project - Titanic Data**

## **Titanic EDA**

- [Titanic Dataset EDA](#titanic-dataset-eda)

[⬆️ Go to Context](#context)
