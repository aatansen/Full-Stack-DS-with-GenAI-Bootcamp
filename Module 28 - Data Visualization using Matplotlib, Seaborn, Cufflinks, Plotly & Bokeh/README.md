# **Context**

- [**Context**](#context)
- [**Day 33 - Data Visualization using Matplotlib, Seaborn, Cufflinks, Plotly \& Bokeh**](#day-33---data-visualization-using-matplotlib-seaborn-cufflinks-plotly--bokeh)
  - [**Matplotlib**](#matplotlib)
    - [Basic Plot (Line Chart)](#basic-plot-line-chart)
    - [Plot with Labels \& Title](#plot-with-labels--title)
    - [Multiple Lines in One Plot](#multiple-lines-in-one-plot)
    - [Line Styles \& Markers](#line-styles--markers)
    - [Bar Chart using Matplotlib](#bar-chart-using-matplotlib)
    - [Histogram using Matplotlib](#histogram-using-matplotlib)
    - [Scatter Plot using Matplotlib](#scatter-plot-using-matplotlib)
    - [Figure Size \& DPI](#figure-size--dpi)
    - [Subplots (Multiple Plots)](#subplots-multiple-plots)
    - [Grid \& Axis Control](#grid--axis-control)
    - [Ticks \& Labels Customization](#ticks--labels-customization)
    - [Saving Plots to File](#saving-plots-to-file)
    - [Working with NumPy Arrays](#working-with-numpy-arrays)
    - [Object-Oriented (OO) Style](#object-oriented-oo-style)
    - [Common Plot Types](#common-plot-types)
    - [Matplotlib vs Seaborn](#matplotlib-vs-seaborn)
    - [When to Use Matplotlib](#when-to-use-matplotlib)
    - [Iris Dataset Visualization using Matplotlib](#iris-dataset-visualization-using-matplotlib)
      - [Loading Iris Dataset](#loading-iris-dataset)
      - [Simple Scatter Plot (Sepal Length vs Sepal Width)](#simple-scatter-plot-sepal-length-vs-sepal-width)
      - [Scatter Plot with Class Separation](#scatter-plot-with-class-separation)
      - [Petal Length vs Petal Width (Best Separation)](#petal-length-vs-petal-width-best-separation)
      - [Multiple Subplots (Feature Comparison)](#multiple-subplots-feature-comparison)
      - [Histogram of Iris Features](#histogram-of-iris-features)
      - [ML Workflow Using Iris](#ml-workflow-using-iris)
  - [**Seaborn**](#seaborn)
    - [Why Seaborn?](#why-seaborn)
    - [Built-in Datasets](#built-in-datasets)
    - [Basic Scatter Plot](#basic-scatter-plot)
    - [Scatter Plot with Hue (Class Separation)](#scatter-plot-with-hue-class-separation)
    - [Line Plot using Matplotlib](#line-plot-using-matplotlib)
    - [Histogram \& KDE](#histogram--kde)
    - [Box Plot](#box-plot)
    - [Violin Plot](#violin-plot)
    - [Count Plot (Categorical Frequency)](#count-plot-categorical-frequency)
    - [Pair Plot (Very Important)](#pair-plot-very-important)
    - [Heatmap (Correlation Matrix)](#heatmap-correlation-matrix)
    - [FacetGrid (Small Multiples)](#facetgrid-small-multiples)
    - [Styling \& Themes](#styling--themes)
    - [Figure Size \& Context](#figure-size--context)
    - [Saving Seaborn Plots](#saving-seaborn-plots)
    - [Seaborn: Axes-level vs Figure-level Functions](#seaborn-axes-level-vs-figure-level-functions)
    - [Seaborn vs Matplotlib](#seaborn-vs-matplotlib)
    - [When to Use Seaborn](#when-to-use-seaborn)
    - [Iris Dataset Examples in Seaborn](#iris-dataset-examples-in-seaborn)
  - [**Plotly**](#plotly)
    - [Why Plotly?](#why-plotly)
    - [Built-in Datasets (Plotly Express)](#built-in-datasets-plotly-express)
    - [Basic Line Plot using Plotly](#basic-line-plot-using-plotly)
    - [Line Plot Using DataFrame](#line-plot-using-dataframe)
    - [Scatter Plot using Plotly](#scatter-plot-using-plotly)
    - [Scatter Plot with Color (Class Separation)](#scatter-plot-with-color-class-separation)
    - [Bar Chart using Plotly](#bar-chart-using-plotly)
    - [Histogram using Plotly](#histogram-using-plotly)
    - [Box Plot using Plotly](#box-plot-using-plotly)
    - [Violin Plot using Plotly](#violin-plot-using-plotly)
    - [Subplots (Multiple Charts)](#subplots-multiple-charts)
    - [Customizing Layout](#customizing-layout)
    - [Saving Plotly Figures](#saving-plotly-figures)
    - [Plotly Express vs Graph Objects](#plotly-express-vs-graph-objects)
    - [Plotly vs Matplotlib vs Seaborn](#plotly-vs-matplotlib-vs-seaborn)
    - [When to Use Plotly](#when-to-use-plotly)
    - [Iris Dataset Visualization using Plotly](#iris-dataset-visualization-using-plotly)
  - [**Bokeh**](#bokeh)
    - [Setup Output](#setup-output)
    - [Basic Line Plot using Bokeh](#basic-line-plot-using-bokeh)
    - [Scatter Plot using Bokeh](#scatter-plot-using-bokeh)
    - [Bar Chart using Bokeh](#bar-chart-using-bokeh)
    - [Working with ColumnDataSource](#working-with-columndatasource)
    - [Hover Tool](#hover-tool)
    - [Multiple Lines / Plots](#multiple-lines--plots)
    - [Layouts (Grid, Column, Row)](#layouts-grid-column-row)
    - [Iris Dataset Example (Bokeh)](#iris-dataset-example-bokeh)
    - [When to Use Bokeh](#when-to-use-bokeh)
  - [**Cufflinks**](#cufflinks)
    - [Basic Line Plot using Cufflinks](#basic-line-plot-using-cufflinks)
    - [Bar Chart using Cufflinks](#bar-chart-using-cufflinks)
    - [Scatter Plot using Cufflinks](#scatter-plot-using-cufflinks)
    - [Histogram using Cufflinks](#histogram-using-cufflinks)
    - [Box Plot using Cufflinks](#box-plot-using-cufflinks)
    - [Cufflinks + Built-in Datasets (Iris)](#cufflinks--built-in-datasets-iris)
    - [Multiple Lines / Columns](#multiple-lines--columns)
    - [Styling \& Layout](#styling--layout)
    - [When to Use Cufflinks](#when-to-use-cufflinks)

# [**Day 33 - Data Visualization using Matplotlib, Seaborn, Cufflinks, Plotly & Bokeh**](./Day%2033%20-%20Data%20Visualization%20using%20Matplotlib,%20Seaborn,%20Cufflinks,%20Plotly%20&%20Bokeh/)

- Create [venv](../Module%2010%20-%20Virtual%20Environment%20&%20Requirements/)
- Install [ipykernel](https://pypi.org/project/ipykernel/), [matplotlib](https://pypi.org/project/matplotlib/), [seaborn](https://pypi.org/project/seaborn/), [plotly](https://pypi.org/project/plotly/), [bokeh](https://pypi.org/project/bokeh/) & [cufflinks](https://pypi.org/project/cufflinks/)

## **Matplotlib**

- Import Matplotlib

  ```py
  import matplotlib.pyplot as plt
  ```

- Common alias convention

  - `plt` → pyplot (most commonly used interface)

[⬆️ Go to Context](#context)

### Basic Plot (Line Chart)

- Simple line plot

  ```py
  import matplotlib.pyplot as plt

  x = [1, 2, 3, 4]
  y = [10, 20, 25, 30]

  plt.plot(x, y)
  plt.show()
  ```

- What `plt.show()` does

  - Renders the plot window
  - Required in scripts (optional in notebooks)

[⬆️ Go to Context](#context)

### Plot with Labels & Title

- Adding title and axis labels

  ```py
  plt.plot(x, y)
  plt.title("Simple Line Plot")
  plt.xlabel("X Axis")
  plt.ylabel("Y Axis")
  plt.show()
  ```

[⬆️ Go to Context](#context)

### Multiple Lines in One Plot

- Plot multiple datasets

  ```py
  x = [1, 2, 3, 4]
  y1 = [10, 20, 30, 40]
  y2 = [40, 30, 20, 10]

  plt.plot(x, y1, label="Line A")
  plt.plot(x, y2, label="Line B")

  plt.legend()
  plt.show()
  ```

[⬆️ Go to Context](#context)

### Line Styles & Markers

- Markers and line styles

  ```py
  plt.plot(x, y, marker="o", linestyle="--")
  plt.show()
  ```

- Common markers

  - `o` → circle
  - `s` → square
  - `^` → triangle

- Common line styles

  - `-` → solid
  - `--` → dashed
  - `:` → dotted

[⬆️ Go to Context](#context)

### Bar Chart using Matplotlib

- Basic bar chart

  ```py
  names = ["A", "B", "C"]
  values = [10, 25, 15]

  plt.bar(names, values)
  plt.show()
  ```

- Horizontal bar chart

  ```py
  plt.barh(names, values)
  plt.show()
  ```

[⬆️ Go to Context](#context)

### Histogram using Matplotlib

- Simple histogram

  ```py
  import numpy as np

  data = np.random.randn(1000)

  plt.hist(data, bins=30)
  plt.show()
  ```

- Use cases

  - Distribution analysis
  - Data spread visualization

[⬆️ Go to Context](#context)

### Scatter Plot using Matplotlib

- Scatter plot (points only)

  ```py
  x = [1, 2, 3, 4, 5]
  y = [5, 7, 4, 8, 6]

  plt.scatter(x, y)
  plt.show()
  ```

- Common use

  - Correlation analysis
  - ML data visualization

[⬆️ Go to Context](#context)

### Figure Size & DPI

- Control plot size

  ```py
  plt.figure(figsize=(8, 4))
  plt.plot(x, y)
  plt.show()
  ```

- Parameters

  - `figsize=(width, height)` → inches
  - `dpi` → resolution

[⬆️ Go to Context](#context)

### Subplots (Multiple Plots)

- Multiple plots in one figure

  ```py
  plt.subplot(1, 2, 1)
  plt.plot(x, y)
  plt.title("Plot 1")

  plt.subplot(1, 2, 2)
  plt.plot(y, x)
  plt.title("Plot 2")

  plt.show()
  ```

- Format

  - `subplot(rows, cols, index)`

[⬆️ Go to Context](#context)

### Grid & Axis Control

- Enable grid

  ```py
  plt.grid(True)
  ```

- Set axis limits

  ```py
  plt.xlim(0, 10)
  plt.ylim(0, 50)
  ```

[⬆️ Go to Context](#context)

### Ticks & Labels Customization

- Custom ticks

  ```py
  plt.xticks([1, 2, 3, 4])
  plt.yticks([10, 20, 30, 40])
  ```

- Rotate labels

  ```py
  plt.xticks(rotation=45)
  ```

[⬆️ Go to Context](#context)

### Saving Plots to File

- Save figure

  ```py
  plt.plot(x, y)
  plt.savefig("plot.png")
  ```

- Save before `plt.show()` (best practice)

[⬆️ Go to Context](#context)

### Working with NumPy Arrays

- Matplotlib + NumPy (very common)

  ```py
  x = np.linspace(0, 10, 100)
  y = np.sin(x)

  plt.plot(x, y)
  plt.show()
  ```

[⬆️ Go to Context](#context)

### Object-Oriented (OO) Style

- Basic OO approach

  ```py
  fig, ax = plt.subplots()

  ax.plot(x, y)
  ax.set_title("OO Style Plot")
  ax.set_xlabel("X")
  ax.set_ylabel("Y")

  plt.show()
  ```

- Why OO style

  - Cleaner
  - Scales better
  - Preferred in production & ML pipelines

[⬆️ Go to Context](#context)

### Common Plot Types

- Line plot → trends
- Bar chart → comparison
- Histogram → distribution
- Scatter plot → relationships
- Subplots → dashboards

[⬆️ Go to Context](#context)

### Matplotlib vs Seaborn

- Matplotlib

  - Low-level
  - Highly customizable
  - Base plotting library

- Seaborn

  - Built on Matplotlib
  - Statistical plots
  - Cleaner defaults

[⬆️ Go to Context](#context)

### When to Use Matplotlib

- Data analysis
- ML experiment visualization
- Reports & dashboards
- Debugging model behavior

[⬆️ Go to Context](#context)

### Iris Dataset Visualization using Matplotlib

- Small & clean dataset
- Balanced classes
- Easy visualization
- Perfect for:
  - Classification demos
  - Data visualization
  - ML algorithm comparison

- About Iris Dataset

  - Built into `scikit-learn`
  - 150 samples

- 4 features:
  - sepal length
  - sepal width
  - petal length
  - petal width

- 3 classes:
  - Setosa
  - Versicolor
  - Virginica

[⬆️ Go to Context](#context)

#### Loading Iris Dataset

- Load dataset from `sklearn`

  ```py
  from sklearn.datasets import load_iris

  iris = load_iris()
  ```

- Features and labels

  ```py
  X = iris.data        # shape: (150, 4)
  y = iris.target      # shape: (150,)
  ```

- Feature names & class names

  ```py
  iris.feature_names
  iris.target_names
  ```

[⬆️ Go to Context](#context)

#### Simple Scatter Plot (Sepal Length vs Sepal Width)

- Visualize two features

  ```py
  import matplotlib.pyplot as plt

  plt.scatter(X[:, 0], X[:, 1])
  plt.xlabel("Sepal Length")
  plt.ylabel("Sepal Width")
  plt.title("Iris Dataset: Sepal Length vs Width")
  plt.show()
  ```

- What this shows

  - Overall data spread
  - No class separation yet

[⬆️ Go to Context](#context)

#### Scatter Plot with Class Separation

- Plot each class separately

  ```py
  for i, name in enumerate(iris.target_names):
      plt.scatter(
          X[y == i, 0],
          X[y == i, 1],
          label=name
      )

  plt.xlabel("Sepal Length")
  plt.ylabel("Sepal Width")
  plt.title("Iris Dataset (Class-wise)")
  plt.legend()
  plt.show()
  ```

- Why this is important

  - Helps visually inspect class separability
  - Common first step in ML workflows

[⬆️ Go to Context](#context)

#### Petal Length vs Petal Width (Best Separation)

- Most informative feature pair

  ```py
  for i, name in enumerate(iris.target_names):
      plt.scatter(
          X[y == i, 2],
          X[y == i, 3],
          label=name
      )

  plt.xlabel("Petal Length")
  plt.ylabel("Petal Width")
  plt.title("Iris Dataset: Petal Length vs Width")
  plt.legend()
  plt.show()
  ```

- ML Insight

  - Petal features separate classes much better
  - Often used in classification demos

[⬆️ Go to Context](#context)

#### Multiple Subplots (Feature Comparison)

- Compare multiple feature pairs

  ```py
  plt.figure(figsize=(10, 4))

  plt.subplot(1, 2, 1)
  plt.scatter(X[:, 0], X[:, 1])
  plt.xlabel("Sepal Length")
  plt.ylabel("Sepal Width")
  plt.title("Sepal Features")

  plt.subplot(1, 2, 2)
  plt.scatter(X[:, 2], X[:, 3])
  plt.xlabel("Petal Length")
  plt.ylabel("Petal Width")
  plt.title("Petal Features")

  plt.show()
  ```

[⬆️ Go to Context](#context)

#### Histogram of Iris Features

- Distribution of a single feature

  ```py
  plt.hist(X[:, 2], bins=20)
  plt.xlabel("Petal Length")
  plt.ylabel("Frequency")
  plt.title("Distribution of Petal Length")
  plt.show()
  ```

- Use case

  - Understand feature distribution
  - Spot skewness or outliers

[⬆️ Go to Context](#context)

#### ML Workflow Using Iris

- Load dataset
- Visualize with Matplotlib
- Preprocess features
- Train ML model
- Plot results

[⬆️ Go to Context](#context)

## **Seaborn**

- Import Seaborn

  ```py
  import seaborn as sns
  import matplotlib.pyplot as plt
  ```

- Common alias convention

  - `sns` → seaborn (high-level plotting built on Matplotlib)

[⬆️ Go to Context](#context)

### Why Seaborn?

- Built on Matplotlib for statistical plotting
- Cleaner defaults and less boilerplate for common EDA plots

[⬆️ Go to Context](#context)

### Built-in Datasets

- Load a built-in dataset

  ```py
  df = sns.load_dataset("iris")
  ```

- View dataset

  ```py
  df.head()
  ```

- Common built-in datasets

  - `iris`
  - `tips`
  - `titanic`
  - `flights`

[⬆️ Go to Context](#context)

### Basic Scatter Plot

- Simple scatter plot (column-based)

  ```py
  sns.scatterplot(
      x="sepal_length",
      y="sepal_width",
      data=df
  )
  plt.show()
  ```

- Difference from Matplotlib

  - Uses DataFrame columns directly (no manual slicing)

[⬆️ Go to Context](#context)

### Scatter Plot with Hue (Class Separation)

- Color points by category

  ```py
  sns.scatterplot(
      x="petal_length",
      y="petal_width",
      hue="species",
      data=df
  )
  plt.show()
  ```

- Why `hue` is useful

  - Automatic grouping, coloring, and legend creation

[⬆️ Go to Context](#context)

### Line Plot using Matplotlib

- Line plot using DataFrame

  ```py
  sns.lineplot(
      x="sepal_length",
      y="sepal_width",
      data=df
  )
  plt.show()
  ```

- Best for

  - Trends and time-series-like visualizations

[⬆️ Go to Context](#context)

### Histogram & KDE

- Histogram

  ```py
  sns.histplot(
      x="petal_length",
      data=df,
      bins=20
  )
  plt.show()
  ```

- Histogram with KDE

  ```py
  sns.histplot(
      x="petal_length",
      data=df,
      kde=True
  )
  plt.show()
  ```

- KDE (Kernel Density Estimate)

  - Smooth estimate of distribution (good for visualizing shape)

[⬆️ Go to Context](#context)

### Box Plot

- Box plot for distribution & outliers

  ```py
  sns.boxplot(
      x="species",
      y="petal_length",
      data=df
  )
  plt.show()
  ```

- Shows

  - Median, quartiles, and outliers

[⬆️ Go to Context](#context)

### Violin Plot

- Violin plot (boxplot + KDE)

  ```py
  sns.violinplot(
      x="species",
      y="petal_length",
      data=df
  )
  plt.show()
  ```

- Best for

  - Observing distribution shape and density per category

[⬆️ Go to Context](#context)

### Count Plot (Categorical Frequency)

- Count values in categories

  ```py
  sns.countplot(
      x="species",
      data=df
  )
  plt.show()
  ```

- Common use

  - Check class balance quickly

[⬆️ Go to Context](#context)

### Pair Plot (Very Important)

- One-line EDA for all numeric relationships

  ```py
  sns.pairplot(df, hue="species")
  ```

- Why it’s powerful

  - Shows pairwise scatterplots + histograms/diagonals for quick insight

[⬆️ Go to Context](#context)

### Heatmap (Correlation Matrix)

- Create correlation matrix

  ```py
  corr = df.corr(numeric_only=True)
  ```

- Plot heatmap

  ```py
  sns.heatmap(corr, annot=True)
  plt.show()
  ```

- ML use

  - Spot correlated features and multicollinearity

[⬆️ Go to Context](#context)

### FacetGrid (Small Multiples)

- Facet by category (useful for comparing distributions)

  ```py
  g = sns.FacetGrid(df, col="species")
  g.map(sns.histplot, "petal_length")
  plt.show()
  ```

- Why

  - Easy comparison across subgroups without manual filtering

[⬆️ Go to Context](#context)

### Styling & Themes

- Set global style

  ```py
  sns.set_style("whitegrid")
  ```

- Common styles

  - `whitegrid`, `darkgrid`, `ticks`, `white`

[⬆️ Go to Context](#context)

### Figure Size & Context

- Control figure size

  ```py
  plt.figure(figsize=(8, 4))
  sns.scatterplot(x="petal_length", y="petal_width", hue="species", data=df)
  plt.show()
  ```

- Set plotting context (affects scale of elements)

  ```py
  sns.set_context("talk")  # options: paper, notebook, talk, poster
  ```

[⬆️ Go to Context](#context)

### Saving Seaborn Plots

- Save the current Matplotlib figure

  ```py
  plt.savefig("seaborn_plot.png", bbox_inches="tight")
  ```

- Save before `plt.show()` (recommended)

[⬆️ Go to Context](#context)

### Seaborn: Axes-level vs Figure-level Functions

- Axes-level (return an `Axes` object)

  - `sns.scatterplot`, `sns.boxplot`, `sns.histplot`
  - Integrates with Matplotlib `ax` and `plt`

- Figure-level (manage their own figure)

  - `sns.pairplot`, `sns.catplot`, `sns.relplot`
  - Useful for quick multi-plot grids

[⬆️ Go to Context](#context)

### Seaborn vs Matplotlib

- Seaborn

  - High-level, nicer defaults, fast EDA for statistical plots

- Matplotlib

  - Low-level, fine-grained control, more flexible for custom layouts

[⬆️ Go to Context](#context)

### When to Use Seaborn

- Exploratory Data Analysis (EDA)
- Quick visual comparisons between categories
- Statistical visualization with minimal code

[⬆️ Go to Context](#context)

### Iris Dataset Examples in Seaborn

- Load Iris (again)

  ```py
  df = sns.load_dataset("iris")
  ```

- Scatter plot with hue (petal features)

  ```py
  sns.scatterplot(x="petal_length", y="petal_width", hue="species", data=df)
  plt.title("Iris: Petal Length vs Width (Seaborn)")
  plt.show()
  ```

- Pairplot for full EDA

  ```py
  sns.pairplot(df, hue="species", corner=True)
  ```

[⬆️ Go to Context](#context)

## **Plotly**

- Import Plotly (recommended interface)

  ```py
  import plotly.express as px
  import plotly.graph_objects as go
  ```

- Plotly interfaces

  - `plotly.express (px)` → high-level, quick plots (like Seaborn)
  - `plotly.graph_objects (go)` → low-level, full control (like Matplotlib OO)

[⬆️ Go to Context](#context)

### Why Plotly?

- Interactive plots (zoom, hover, pan)
- Works well in Jupyter & web apps
- Ideal for dashboards and presentations

[⬆️ Go to Context](#context)

### Built-in Datasets (Plotly Express)

- Load built-in dataset

  ```py
  df = px.data.iris()
  ```

- Preview data

  ```py
  df.head()
  ```

- Common built-in datasets

  - `iris`
  - `tips`
  - `gapminder`
  - `election`

[⬆️ Go to Context](#context)

### Basic Line Plot using Plotly

- Simple interactive line plot

  ```py
  fig = px.line(
      x=[1, 2, 3, 4],
      y=[10, 20, 25, 30],
      title="Basic Line Plot"
  )

  fig.show()
  ```

- Key difference from Matplotlib

  - No `plt.show()`
  - Plot opens with interactivity

[⬆️ Go to Context](#context)

### Line Plot Using DataFrame

- Column-based plotting

  ```py
  fig = px.line(
      df,
      x="sepal_length",
      y="sepal_width",
      title="Sepal Length vs Width"
  )

  fig.show()
  ```

[⬆️ Go to Context](#context)

### Scatter Plot using Plotly

- Basic scatter plot

  ```py
  fig = px.scatter(
      df,
      x="sepal_length",
      y="sepal_width"
  )

  fig.show()
  ```

- Use case

  - Relationship & correlation analysis

[⬆️ Go to Context](#context)

### Scatter Plot with Color (Class Separation)

- Color points by category

  ```py
  fig = px.scatter(
      df,
      x="petal_length",
      y="petal_width",
      color="species",
      title="Iris Dataset (Class-wise)"
  )

  fig.show()
  ```

- What Plotly adds

  - Hover tooltips
  - Toggle classes on/off

[⬆️ Go to Context](#context)

### Bar Chart using Plotly

- Simple bar chart

  ```py
  fig = px.bar(
      x=["A", "B", "C"],
      y=[10, 25, 15],
      title="Basic Bar Chart"
  )

  fig.show()
  ```

- Bar chart from DataFrame

  ```py
  fig = px.bar(
      df,
      x="species",
      y="petal_length"
  )

  fig.show()
  ```

[⬆️ Go to Context](#context)

### Histogram using Plotly

- Histogram of a feature

  ```py
  fig = px.histogram(
      df,
      x="petal_length",
      nbins=20,
      title="Petal Length Distribution"
  )

  fig.show()
  ```

- Interactive benefit

  - Hover count
  - Zoom on bins

[⬆️ Go to Context](#context)

### Box Plot using Plotly

- Box plot by category

  ```py
  fig = px.box(
      df,
      x="species",
      y="petal_length",
      title="Petal Length by Species"
  )

  fig.show()
  ```

- Shows

  - Median
  - Quartiles
  - Outliers (interactive)

[⬆️ Go to Context](#context)

### Violin Plot using Plotly

- Violin plot for distribution shape

  ```py
  fig = px.violin(
      df,
      x="species",
      y="petal_length",
      box=True,
      points="all"
  )

  fig.show()
  ```

- Advantage

  - Distribution + individual points together

[⬆️ Go to Context](#context)

### Subplots (Multiple Charts)

- Create subplots manually

  ```py
  from plotly.subplots import make_subplots

  fig = make_subplots(rows=1, cols=2)

  fig.add_scatter(x=df["sepal_length"], y=df["sepal_width"], row=1, col=1)
  fig.add_scatter(x=df["petal_length"], y=df["petal_width"], row=1, col=2)

  fig.show()
  ```

- Why

  - Dashboards
  - Comparative analysis

[⬆️ Go to Context](#context)

### Customizing Layout

- Update titles & labels

  ```py
  fig.update_layout(
      title="Customized Plot",
      xaxis_title="X Axis",
      yaxis_title="Y Axis"
  )
  ```

- Update trace style

  ```py
  fig.update_traces(marker=dict(size=10))
  ```

[⬆️ Go to Context](#context)

### Saving Plotly Figures

- Save as HTML (interactive)

  ```py
  fig.write_html("plot.html")
  ```

- Save as image (requires extra engine)

  ```py
  fig.write_image("plot.png")
  ```

[⬆️ Go to Context](#context)

### Plotly Express vs Graph Objects

- Plotly Express (`px`)

  - Faster
  - Less code
  - Ideal for EDA

- Graph Objects (`go`)

  - Full control
  - Production-level dashboards
  - Complex layouts

[⬆️ Go to Context](#context)

### Plotly vs Matplotlib vs Seaborn

- Plotly

  - Interactive
  - Web & dashboard friendly
  - Hover + zoom built-in

- Seaborn

  - Statistical EDA
  - Clean defaults

- Matplotlib

  - Maximum control
  - Static plots

[⬆️ Go to Context](#context)

### When to Use Plotly

- Interactive data exploration
- Dashboards (Dash, Streamlit)
- Presentations & reports
- ML result visualization

[⬆️ Go to Context](#context)

### Iris Dataset Visualization using Plotly

- Scatter plot (best separation)

  ```py
  fig = px.scatter(
      df,
      x="petal_length",
      y="petal_width",
      color="species",
      title="Iris Dataset: Petal Length vs Width"
  )

  fig.show()
  ```

- ML Insight

  - Easy visual separation
  - Interactive inspection of data points

[⬆️ Go to Context](#context)

## **Bokeh**

- Import Bokeh

  ```py
  from bokeh.plotting import figure, show, output_file
  from bokeh.models import ColumnDataSource
  ```

- Key points

  - Bokeh → Interactive visualizations for web
  - Outputs can be HTML, notebook, or server
  - Focus on streaming, dashboards, and large datasets

[⬆️ Go to Context](#context)

### Setup Output

- Save to HTML file

  ```py
  output_file("bokeh_plot.html")
  ```

- Or display in notebook

  ```py
  from bokeh.io import output_notebook
  output_notebook()
  ```

[⬆️ Go to Context](#context)

### Basic Line Plot using Bokeh

- Simple interactive line

  ```py
  p = figure(title="Basic Line Plot", x_axis_label="X", y_axis_label="Y")
  p.line([1, 2, 3, 4], [10, 20, 25, 30], line_width=2)
  show(p)
  ```

- Features

  - Hover and zoom enabled by default
  - Output is interactive HTML

[⬆️ Go to Context](#context)

### Scatter Plot using Bokeh

- Interactive scatter plot

  ```py
  p = figure(title="Scatter Plot", x_axis_label="X", y_axis_label="Y")
  p.circle([1, 2, 3, 4, 5], [5, 7, 4, 8, 6], size=10, color="green")
  show(p)
  ```

- `circle`, `triangle`, `square` → shape markers

[⬆️ Go to Context](#context)

### Bar Chart using Bokeh

- Vertical bar chart

  ```py
  x = ['A', 'B', 'C']
  y = [10, 25, 15]

  p = figure(x_range=x, title="Bar Chart", y_axis_label="Values")
  p.vbar(x=x, top=y, width=0.5, color="navy")
  show(p)
  ```

- Horizontal bars

  ```py
  p.hbar(y=x, right=y, height=0.5, color="orange")
  show(p)
  ```

[⬆️ Go to Context](#context)

### Working with ColumnDataSource

- ColumnDataSource → central data structure

  ```py
  source = ColumnDataSource(data=dict(
      x=[1, 2, 3, 4],
      y=[10, 20, 25, 30]
  ))

  p = figure(title="CDS Example")
  p.line('x', 'y', source=source)
  show(p)
  ```

- Advantage

  - Needed for interactive widgets
  - Updates dynamically

[⬆️ Go to Context](#context)

### Hover Tool

- Add interactive tooltips

  ```py
  from bokeh.models import HoverTool

  p = figure(title="Hover Example", x_axis_label="X", y_axis_label="Y")
  p.circle([1,2,3], [4,5,6], size=10)

  hover = HoverTool(tooltips=[("X", "@x"), ("Y", "@y")])
  p.add_tools(hover)

  show(p)
  ```

- Allows interactive inspection of points

[⬆️ Go to Context](#context)

### Multiple Lines / Plots

- Multiple lines on same figure

  ```py
  p = figure(title="Multiple Lines")
  p.line([1, 2, 3], [4, 5, 6], color="red", legend_label="Line 1")
  p.line([1, 2, 3], [6, 5, 4], color="blue", legend_label="Line 2")
  p.legend.location = "top_left"
  show(p)
  ```

[⬆️ Go to Context](#context)

### Layouts (Grid, Column, Row)

- Combine multiple plots

  ```py
  from bokeh.layouts import column, row

  p1 = figure(title="Plot 1")
  p1.line([1,2,3], [4,5,6])

  p2 = figure(title="Plot 2")
  p2.circle([1,2,3], [6,5,4])

  layout = row(p1, p2)
  show(layout)
  ```

- Useful for dashboards

[⬆️ Go to Context](#context)

### Iris Dataset Example (Bokeh)

- Load Iris from `plotly` / `seaborn` (or `sklearn`)

  ```py
  from sklearn.datasets import load_iris
  import pandas as pd

  iris = load_iris()
  df = pd.DataFrame(iris.data, columns=iris.feature_names)
  df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
  ```

- Scatter plot: Petal Length vs Width

  ```py
  species_list = df['species'].unique()
  colors = ["red", "green", "blue"]

  p = figure(title="Iris Dataset (Bokeh)", x_axis_label="Petal Length", y_axis_label="Petal Width")

  for spec, color in zip(species_list, colors):
      subset = df[df['species']==spec]
      p.circle(subset['petal length (cm)'], subset['petal width (cm)'], size=8, color=color, legend_label=spec)

  p.legend.location = "top_left"
  show(p)
  ```

- Interactive benefits

  - Zoom, pan, and hover
  - Works as standalone HTML for dashboards

[⬆️ Go to Context](#context)

### When to Use Bokeh

- Web dashboards & interactive apps
- Large datasets with streaming updates
- Interactive data exploration in Python
- Integrates well with Flask / Django / Jupyter

[⬆️ Go to Context](#context)

## **Cufflinks**

- Import Cufflinks

  ```py
  import pandas as pd
  import cufflinks as cf
  cf.go_offline()  # For offline plotting
  cf.set_config_file(offline=True, world_readable=True)
  ```

- Key points

  - Cufflinks connects **Pandas DataFrames** directly to **Plotly**
  - Quick interactive plots with minimal code
  - Great for exploratory data analysis (EDA)

[⬆️ Go to Context](#context)

### Basic Line Plot using Cufflinks

- Plot directly from a DataFrame

  ```py
  import numpy as np

  df = pd.DataFrame(np.random.randn(10, 2), columns=['A', 'B'])
  df.iplot(kind='line', title='Basic Line Plot')
  ```

- Features

  - Interactive by default
  - Hover, zoom, and pan included

[⬆️ Go to Context](#context)

### Bar Chart using Cufflinks

- Vertical bar chart

  ```py
  df.iplot(kind='bar', title='Bar Chart')
  ```

- Horizontal bar chart

  ```py
  df.iplot(kind='barh', title='Horizontal Bar Chart')
  ```

[⬆️ Go to Context](#context)

### Scatter Plot using Cufflinks

- Scatter plot from DataFrame

  ```py
  df.iplot(kind='scatter', x='A', y='B', mode='markers', title='Scatter Plot')
  ```

- Parameters

  - `mode='markers'` → points only
  - `mode='lines'` → lines only
  - `mode='lines+markers'` → both

[⬆️ Go to Context](#context)

### Histogram using Cufflinks

- Histogram of a DataFrame column

  ```py
  df['A'].iplot(kind='hist', bins=10, title='Histogram of A')
  ```

- Useful for

  - Distribution analysis
  - Quick insights

[⬆️ Go to Context](#context)

### Box Plot using Cufflinks

- Box plot per column

  ```py
  df.iplot(kind='box', title='Box Plot')
  ```

- Shows

  - Median, quartiles, outliers

[⬆️ Go to Context](#context)

### Cufflinks + Built-in Datasets (Iris)

- Load Iris dataset

  ```py
  from sklearn.datasets import load_iris
  import pandas as pd

  iris = load_iris()
  df = pd.DataFrame(iris.data, columns=iris.feature_names)
  df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
  ```

- Scatter plot: Petal Length vs Width

  ```py
  df.iplot(
      kind='scatter',
      x='petal length (cm)',
      y='petal width (cm)',
      mode='markers',
      categories='species',
      title='Iris Dataset: Petal Length vs Width'
  )
  ```

- Features

  - Color-coded by species
  - Interactive hover and zoom

[⬆️ Go to Context](#context)

### Multiple Lines / Columns

- Plot multiple columns at once

  ```py
  df[['sepal length (cm)', 'sepal width (cm)']].iplot(kind='line', title='Multiple Lines')
  ```

- Benefit

  - Quick comparison across features
  - Interactive legend for toggling columns

[⬆️ Go to Context](#context)

### Styling & Layout

- Customize plots

  ```py
  df.iplot(
      kind='scatter',
      x='sepal length (cm)',
      y='sepal width (cm)',
      mode='markers',
      size=10,
      colors=['red', 'green', 'blue'],
      title='Styled Scatter Plot'
  )
  ```

- Options

  - `size` → marker size
  - `colors` → array of colors
  - `title` → chart title

[⬆️ Go to Context](#context)

### When to Use Cufflinks

- Quick interactive plots from Pandas
- Exploratory Data Analysis (EDA)
- Dashboard visualizations (offline HTML or notebooks)
- Interactive inspection of ML datasets

[⬆️ Go to Context](#context)
