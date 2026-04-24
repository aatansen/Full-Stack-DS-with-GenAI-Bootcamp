# **Context**

- [**Context**](#context)
- [**Day 54 - Excel Part 01**](#day-54---excel-part-01)
  - [**Fact Table (The Measurable Data)**](#fact-table-the-measurable-data)
  - [**Dimension Table (Descriptive Information)**](#dimension-table-descriptive-information)
  - [**Fact Table Vs Dimension Table**](#fact-table-vs-dimension-table)
    - [Duplicate Data in a Fact Table](#duplicate-data-in-a-fact-table)
    - [Duplicate Data in a Dimension Table](#duplicate-data-in-a-dimension-table)
  - [**Excel Powerful Formulas \& Features**](#excel-powerful-formulas--features)
    - [1. VLOOKUP / HLOOKUP / XLOOKUP](#1-vlookup--hlookup--xlookup)
      - [VLOOKUP (Vertical Lookup)](#vlookup-vertical-lookup)
      - [HLOOKUP (Horizontal Lookup)](#hlookup-horizontal-lookup)
      - [XLOOKUP (Modern replacement)](#xlookup-modern-replacement)
    - [2. SUMIF / SUMIFS](#2-sumif--sumifs)
      - [SUMIF](#sumif)
      - [SUMIFS](#sumifs)
    - [3. FILTER](#3-filter)
    - [4. Table Design](#4-table-design)
    - [5. Pivot Table](#5-pivot-table)
    - [6. Slicer](#6-slicer)
    - [7. Chart](#7-chart)
    - [8. Dashboard Design](#8-dashboard-design)
  - [**Excel and Python Workflow I**](#excel-and-python-workflow-i)
- [**Day 55 - Excel Part 02**](#day-55---excel-part-02)
  - [**Excel Data Processing \& Dashboard Tools**](#excel-data-processing--dashboard-tools)
    - [1. Power Query](#1-power-query)
    - [2. ETL (Extract Transform Load)](#2-etl-extract-transform-load)
      - [Extract](#extract)
      - [Transform](#transform)
      - [Load](#load)
    - [3. Pivot Table (Advanced Usage)](#3-pivot-table-advanced-usage)
    - [4. Slicers](#4-slicers)
    - [5. Charts (Business Analytics)](#5-charts-business-analytics)
    - [6. HR Dashboard Example](#6-hr-dashboard-example)
  - [**Excel and Python Workflow II**](#excel-and-python-workflow-ii)
- [**Day 56 - Excel Part 03**](#day-56---excel-part-03)
  - [**Power Query Editor**](#power-query-editor)
  - [**Pivot Table**](#pivot-table)
  - [**Slicer And Filtering**](#slicer-and-filtering)
  - [**Chart, Dashboard Design**](#chart-dashboard-design)
  - [**Dashboard Design Principles**](#dashboard-design-principles)

# **Day 54 - Excel Part 01**

## **Fact Table (The Measurable Data)**

A **Fact Table** stores the **numbers you want to analyze**. For example **event or transaction record**.

- Example: Sales Data

  | DateID | ProductID | CustomerID | Quantity | Revenue |
  | ------ | --------- | ---------- | -------- | ------- |
  | 101    | P01       | C12        | 2        | 400     |
  | 101    | P02       | C20        | 1        | 250     |
  | 102    | P01       | C12        | 3        | 600     |

Here:

- **Quantity**
- **Revenue**

are called **facts (measures)** because they are **numeric values you calculate**.

Typical calculations:

- SUM
- AVERAGE
- COUNT
- MIN / MAX

Example questions answered by fact tables:

- Total sales?
- Total orders?
- Average revenue?

[⬆️ Go to Context](#context)

## **Dimension Table (Descriptive Information)**

A **Dimension Table** stores **descriptive attributes** that explain the facts.

- Example: Product Table

  | ProductID | ProductName | Category    | Brand    |
  | --------- | ----------- | ----------- | -------- |
  | P01       | Laptop      | Electronics | Dell     |
  | P02       | Mouse       | Accessories | Logitech |

- Example: Customer Table

  | CustomerID | CustomerName | City       |
  | ---------- | ------------ | ---------- |
  | C12        | Rahim        | Dhaka      |
  | C20        | Karim        | Chittagong |

These tables help answer questions like:

- Sales **by city**
- Sales **by product category**
- Sales **by brand**

[⬆️ Go to Context](#context)

## **Fact Table Vs Dimension Table**

### Duplicate Data in a Fact Table

- Duplicates are **often valid** in a Fact table.

  **Reason**:
  A fact table stores **transactions or events**, and many events can share the same dimension values.

- Example

  | DateID | ProductID | CustomerID | Quantity | Revenue |
  | ------ | --------- | ---------- | -------- | ------- |
  | 101    | P01       | C12        | 2        | 400     |
  | 101    | P01       | C12        | 1        | 200     |
  | 101    | P01       | C12        | 3        | 600     |

These rows look similar but they represent **different transactions**.

Possible reasons:

- Different orders
- Different invoices
- Different times
- Different stores

So **duplicate dimension keys are normal** in fact tables.

[⬆️ Go to Context](#context)

### Duplicate Data in a Dimension Table

- In dimension tables, duplicates are usually **NOT allowed** for the **key column**.

- Example product dimension:

  | ProductID | ProductName | Category    |
  | --------- | ----------- | ----------- |
  | P01       | Laptop      | Electronics |
  | P02       | Mouse       | Accessories |

- If this happens:

  | ProductID | ProductName | Category    |
  | --------- | ----------- | ----------- |
  | P01       | Laptop      | Electronics |
  | P01       | Laptop      | Electronics |

*This causes **relationship errors**.*

Why?

Because data models require:

  ```xlsx
  Fact Table → Many
  Dimension Table → One
  ```

This is called a **Many-to-One relationship**.

- Correct Relationship Model

```xlsx
Fact Table (many rows)
        |
        | ProductID
        |
Dimension Table (unique ProductID)
```

Example:

Fact Table

| ProductID | Sales |
| --------- | ----- |
| P01       | 400   |
| P01       | 200   |
| P02       | 300   |

Dimension Table

| ProductID | Category    |
| --------- | ----------- |
| P01       | Electronics |
| P02       | Accessories |

[⬆️ Go to Context](#context)

## **Excel Powerful Formulas & Features**

### 1. VLOOKUP / HLOOKUP / XLOOKUP

#### VLOOKUP (Vertical Lookup)

- Searches **vertically in the first column** of a table.
- Returns a value from another column in the **same row**.

  ```xlsx
  =VLOOKUP(lookup_value, table_array, col_index_num, [range_lookup])
  ```

  ```xlsx
  =VLOOKUP(A2, A1:D10, 3, FALSE)
  ```

  ```py
  import pandas as pd

  df1 = pd.DataFrame({
      "id":[1,2,3],
      "name":["A","B","C"]
  })

  df2 = pd.DataFrame({
      "id":[1,2,3],
      "salary":[500,600,700]
  })

  result = pd.merge(df1, df2, on="id")
  print(result)
  ```

  - Finds value of `A2` in column A
  - Returns value from **3rd column**

- **Limitation**
  - Can only search **left → right**

[⬆️ Go to Context](#context)

#### HLOOKUP (Horizontal Lookup)

- Searches **horizontally in the first row** of a table.

  ```xlsx
  =HLOOKUP(lookup_value, table_array, row_index_num, [range_lookup])
  ```

  ```xlsx
  =HLOOKUP("Sales", A1:G5, 3, FALSE)
  ```

[⬆️ Go to Context](#context)

#### XLOOKUP (Modern replacement)

- Works **both directions**
- No column index needed
- Much easier and safer

  ```xlsx
  =XLOOKUP(lookup_value, lookup_array, return_array)
  ```

  ```xlsx
  =XLOOKUP(A2, A2:A10, C2:C10)
  ```

- **Advantages**
  - Left or right lookup
  - Exact match by default
  - Handles errors easily

[⬆️ Go to Context](#context)

### 2. SUMIF / SUMIFS

#### SUMIF

- Adds numbers **based on one condition**

  ```xlsx
  =SUMIF(range, criteria, sum_range)
  ```

  ```xlsx
  =SUMIF(A2:A10,"Apple",B2:B10)
  ```

  ```py
  df[df["product"]=="Apple"]["sales"].sum()
  ```

Sum values in column B where column A = Apple.

[⬆️ Go to Context](#context)

#### SUMIFS

- Adds numbers **based on multiple conditions**

  ```xlsx
  =SUMIFS(sum_range, criteria_range1, criteria1, criteria_range2, criteria2)
  ```

  ```xlsx
  =SUMIFS(C2:C10, A2:A10, "Apple", B2:B10, ">50")
  ```

  ```py
  df[(df["product"]=="Apple") & (df["qty"]>50)]["sales"].sum()
  ```

  - Sum sales where
  - Product = Apple
  - and Quantity > 50

[⬆️ Go to Context](#context)

### 3. FILTER

- Extracts **specific rows that match conditions**.

  ```xlsx
  =FILTER(array, include)
  ```

  ```xlsx
  =FILTER(A2:C10, B2:B10="Apple")
  ```

  ```py
  df[df["product"]=="Apple"]
  ```

Returns rows where column B = Apple.

[⬆️ Go to Context](#context)

### 4. Table Design

Excel Tables help organize data.

- **Features**
  - Auto formatting
  - Automatic formulas
  - Structured references
  - Easy sorting and filtering

- **Create Table**

  ```xlsx
  Ctrl + T
  ```

  ```py
  df = pd.read_csv("data.csv")
  ```

Benefits

- Dynamic ranges
- Cleaner formulas
- Better for dashboards

[⬆️ Go to Context](#context)

### 5. Pivot Table

Used for **summarizing large datasets quickly**.

- Can calculate:
  - Sum
  - Count
  - Average
  - Min / Max

- Convert this

  | Product | Sales |
  | ------- | ----- |
  | Apple   | 50    |
  | Banana  | 30    |

- Into

  | Product | Total Sales |
  | ------- | ----------- |
  | Apple   | 200         |
  | Banana  | 120         |

- **Create**

  ```xlsx
  Insert → PivotTable
  ```

  ```py
  df.pivot_table(
      values="sales",
      index="product",
      aggfunc="sum"
  )
  ```

  ```py
  df.groupby("product")["sales"].sum()
  ```

[⬆️ Go to Context](#context)

### 6. Slicer

A **visual filter for Pivot Tables**.

- Features
  - Clickable buttons
  - Easy filtering
  - Used in dashboards

- Example filter by:
  - Year
  - Department
  - Product

- Python equivalent tools:
  - plotly
  - streamlit
  - dash

  ```py
  import streamlit as st

  product = st.selectbox("Select product", df["product"].unique())

  filtered = df[df["product"] == product]

  st.write(filtered)
  ```

[⬆️ Go to Context](#context)

### 7. Chart

Charts visualize data.

- Common charts
  - Bar chart
  - Line chart
  - Pie chart
  - Area chart
  - Scatter plot

- **Create**

  ```xlsx
  Insert → Chart
  ```

- Common ones in python:
  - matplotlib
  - seaborn
  - plotly

  ```py
  import matplotlib.pyplot as plt

  df.groupby("product")["sales"].sum().plot(kind="bar")

  plt.show()
  ```

- Best practice
  - Keep charts simple
  - Use labels
  - Avoid too many colors

[⬆️ Go to Context](#context)

### 8. Dashboard Design

Dashboard = **visual summary of data**

- Usually contains:
  - KPIs (Key Performance Indicators)
  - Charts
  - Pivot Tables
  - Slicers
  - Key metrics

- Example metrics
  - Total Sales
  - Employees
  - Profit
  - Growth

- Good dashboard rules*
  - Simple layout
  - Consistent colors
  - Interactive filters
  - Clear titles

- Most Excel dashboards rely mainly on:
  - Tables
  - Pivot Tables
  - Charts
  - Slicers
  - XLOOKUP
  - SUMIFS
  - FILTER

- Popular tools in python:
  - Streamlit
  - Dash
  - Plotly

  ```py
  import streamlit as st
  import pandas as pd

  df = pd.read_csv("sales.csv")

  st.title("Sales Dashboard")

  st.bar_chart(df.groupby("product")["sales"].sum())
  ```

[⬆️ Go to Context](#context)

## **Excel and Python Workflow I**

  | Excel Feature     | What it Does                     | Python Equivalent                          |
  | ----------------- | -------------------------------- | ------------------------------------------ |
  | VLOOKUP / XLOOKUP | Lookup values from another table | `pandas.merge()`                           |
  | SUMIF / SUMIFS    | Conditional aggregation          | `groupby()` + `sum()` or boolean filtering |
  | FILTER            | Extract rows based on condition  | Boolean indexing                           |
  | Table Design      | Structured data table            | `pandas.DataFrame`                         |
  | Pivot Table       | Data summarization               | `pivot_table()` or `groupby()`             |
  | Slicer            | Interactive filtering            | Dashboard tools (Plotly, Streamlit, Dash)  |
  | Chart             | Data visualization               | `matplotlib`, `seaborn`, `plotly`          |
  | Dashboard         | Visual reporting                 | `Streamlit`, `Dash`, `Power BI`, `Tableau` |

[⬆️ Go to Context](#context)

# **Day 55 - Excel Part 02**

## **Excel Data Processing & Dashboard Tools**

### 1. Power Query

Power Query is Excel’s **data preparation tool**.

- Used to:

  - Import data
  - Clean data
  - Transform data
  - Combine multiple datasets

- It works like a **data pipeline inside Excel**.

- Example tasks:

  - Remove duplicates
  - Split columns
  - Change data types
  - Merge datasets
  - Load data from files, databases, APIs

- **Open Power Query**

  ```xlsx
  Data → Get Data
  ```

- Example workflow

  1. Import CSV
  2. Clean columns
  3. Remove nulls
  4. Load to Excel table

  ```py
  import pandas as pd

  df = pd.read_csv("sales.csv")

  # cleaning
  df = df.drop_duplicates()
  df = df.dropna()

  df["date"] = pd.to_datetime(df["date"])

  print(df.head())
  ```

Power Query is basically **Excel’s visual version of pandas data cleaning**.

[⬆️ Go to Context](#context)

### 2. ETL (Extract Transform Load)

ETL is a **core concept in Data Engineering and Data Analytics**.

#### Extract

- Collect data from sources:

  - Excel
  - CSV
  - Databases
  - APIs

  ```py
  df = pd.read_csv("sales.csv")
  ```

#### Transform

- Clean and modify data

Examples:

- remove nulls
- convert data types
- create new columns

  ```py
  df["profit"] = df["revenue"] - df["cost"]
  ```

#### Load

- Store processed data

Examples:

- Excel file
- Database
- Dashboard

```py
df.to_csv("clean_sales.csv", index=False)
```

Excel Power Query performs **ETL visually without coding**.

Common ETL workflow:

  ```xlsx
  Raw Data → Cleaning → Transformation → Analysis
  ```

[⬆️ Go to Context](#context)

### 3. Pivot Table (Advanced Usage)

Pivot Tables are used to **summarize and analyze data quickly**.

Example dataset

| Department | Employee | Salary |
| ---------- | -------- | ------ |
| HR         | A        | 500    |
| HR         | B        | 600    |
| IT         | C        | 800    |

Pivot Table result

| Department | Avg Salary |
| ---------- | ---------- |
| HR         | 550        |
| IT         | 800        |

Common operations

- Sum
- Average
- Count
- Percentage of total
- Grouping by date/month/year

- Create Pivot Table

  ```xlsx
  Insert → PivotTable
  ```

  ```py
  df.pivot_table(
      values="salary",
      index="department",
      aggfunc="mean"
  )
  ```

- Another common approach

  ```py
  df.groupby("department")["salary"].mean()
  ```

Pivot Tables are heavily used in **business reporting and HR analytics**.

[⬆️ Go to Context](#context)

### 4. Slicers

Slicers are **interactive filters for Pivot Tables and charts**.

Instead of dropdown filters, slicers provide **visual buttons**.

Example slicer filters:

- Department
- Year
- Region
- Product

Benefits

- Easy filtering
- Interactive dashboards
- Works with multiple Pivot Tables simultaneously

- Add slicer

  ```xlsx
  Insert → Slicer
  ```

- Python dashboard

  ```py
  import streamlit as st
  import pandas as pd

  df = pd.read_csv("employees.csv")

  department = st.selectbox(
      "Select Department",
      df["department"].unique()
  )

  filtered = df[df["department"] == department]

  st.write(filtered)
  ```

Slicers are widely used in **Excel dashboards for business users**.

[⬆️ Go to Context](#context)

### 5. Charts (Business Analytics)

Charts convert **raw numbers into visual insights**.

Most used charts in business analysis

- Bar chart → category comparison
- Line chart → trends over time
- Pie chart → percentage distribution
- Scatter plot → correlation analysis
- Area chart → cumulative trends

- Create chart

  ```xlsx
  Insert → Chart
  ```

```py
import matplotlib.pyplot as plt

sales = df.groupby("product")["sales"].sum()

sales.plot(kind="bar")

plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")

plt.show()
```

Best practices

- Label axes
- Keep charts simple
- Avoid unnecessary colors
- Use clear titles

[⬆️ Go to Context](#context)

### 6. HR Dashboard Example

HR dashboards help analyze **employee and workforce data**.

Typical HR dataset

| Employee | Department | Salary | Join Year |
| -------- | ---------- | ------ | --------- |
| A        | HR         | 500    | 2021      |
| B        | IT         | 800    | 2020      |

Common HR metrics

- Total Employees
- Average Salary
- Employees per Department
- Hiring Trend
- Gender distribution
- Attrition rate

Example Excel dashboard components

- Pivot Tables
- Charts
- KPI cards
- Slicers
- Tables

  ```py
  import streamlit as st
  import pandas as pd

  df = pd.read_csv("employees.csv")

  st.title("HR Dashboard")

  st.metric("Total Employees", len(df))

  dept_count = df["department"].value_counts()

  st.bar_chart(dept_count)
  ```

- Typical HR dashboard layout

  ```txt
  KPI Cards
  ↓
  Employee Distribution Chart
  ↓
  Department Salary Chart
  ↓
  Filters (Slicers)
  ```

Excel dashboards are widely used because **they require no coding** and are easy for business teams.

[⬆️ Go to Context](#context)

## **Excel and Python Workflow II**

  | Excel Tool   | Purpose                          | Python Equivalent                 |
  | ------------ | -------------------------------- | --------------------------------- |
  | Power Query  | Data cleaning and transformation | `pandas` data processing          |
  | ETL          | Data pipeline                    | `pandas` + ETL frameworks         |
  | Pivot Table  | Data summarization               | `pivot_table()` / `groupby()`     |
  | Slicer       | Interactive filtering            | `Streamlit`, `Dash`, `Plotly`     |
  | Charts       | Data visualization               | `matplotlib`, `seaborn`, `plotly` |
  | HR Dashboard | Business reporting               | `Streamlit`, `Dash` dashboards    |

[⬆️ Go to Context](#context)

# **Day 56 - Excel Part 03**

## **Power Query Editor**

Power Query Editor is the **visual interface used to clean and transform data** after importing it into Excel.

- It is part of **Power Query**, but this is where the **actual data transformation happens**.

- Used to:

  - Clean messy data
  - Transform columns
  - Filter rows
  - Combine datasets
  - Build repeatable data pipelines

- It records each step as a **query step**, so the process can be **reapplied automatically when data refreshes**.

- Open Power Query Editor

  ```xlsx
  Data → Get Data → Transform Data
  ```

- Common tools inside Power Query Editor

  - Remove rows
  - Replace values
  - Split column
  - Merge queries
  - Change data types
  - Filter rows
  - Add custom column

Example workflow

1. Import raw CSV
2. Remove unnecessary columns
3. Convert date column
4. Remove duplicates
5. Load cleaned data into Excel

- Python equivalent

  ```py
  import pandas as pd

  df = pd.read_csv("sales.csv")

  # remove unnecessary column
  df = df.drop(columns=["temp_column"])

  # convert date
  df["date"] = pd.to_datetime(df["date"])

  # remove duplicates
  df = df.drop_duplicates()

  print(df.head())
  ```

Power Query Editor works like a **visual data transformation engine similar to pandas pipelines**.

[⬆️ Go to Context](#context)

## **Pivot Table**

Pivot Tables allow **dynamic data summarization and analysis** without writing formulas.

They help answer questions like:

- Total sales by region
- Average salary per department
- Monthly revenue trends
- Product performance

Example dataset

  | Product | Region | Sales |
  | ------- | ------ | ----- |
  | A       | East   | 100   |
  | B       | West   | 200   |
  | A       | West   | 150   |

Pivot result

  | Product | Total Sales |
  | ------- | ----------- |
  | A       | 250         |
  | B       | 200         |

Create Pivot Table

  ```xlsx
  Insert → PivotTable
  ```

Pivot Table structure

- **Rows** → Categories to group data
- **Columns** → Additional grouping
- **Values** → Calculations (sum, average, count)
- **Filters** → Dataset filters

Example

  | Rows       | Values         |
  | ---------- | -------------- |
  | Department | Average Salary |

- Python equivalent

  ```py
  import pandas as pd

  df = pd.read_csv("sales.csv")

  pivot = df.pivot_table(
      values="sales",
      index="product",
      aggfunc="sum"
  )

  print(pivot)
  ```

- Another common method

  ```py
  df.groupby("product")["sales"].sum()
  ```

Pivot Tables are heavily used in **finance, HR analytics, and business reporting**.

[⬆️ Go to Context](#context)

## **Slicer And Filtering**

Slicers provide **interactive filtering controls for Pivot Tables and Excel dashboards**.

Instead of using dropdown filters, slicers show **visual buttons that users can click**.

Example slicer filters

- Department
- Region
- Product
- Year

Benefits

- Easy for non-technical users
- Real-time filtering
- Can control **multiple Pivot Tables simultaneously**
- Ideal for dashboards

Add slicer

```xlsx
Insert → Slicer
```

Example scenario

A sales dashboard might include slicers for:

- Region
- Product Category
- Year

Clicking **Region = Asia** instantly updates all charts and Pivot Tables.

- Python dashboard equivalent

  ```py
  import streamlit as st
  import pandas as pd

  df = pd.read_csv("sales.csv")

  region = st.selectbox(
      "Select Region",
      df["region"].unique()
  )

  filtered = df[df["region"] == region]

  st.write(filtered)
  ```

Slicers are a key component of **interactive Excel dashboards**.

[⬆️ Go to Context](#context)

## **Chart, Dashboard Design**

Charts transform **raw data into visual insights**.

They help stakeholders quickly understand trends, patterns, and comparisons.

Common business charts

- **Bar Chart** → Compare categories
- **Line Chart** → Time trends
- **Pie Chart** → Percentage distribution
- **Scatter Plot** → Relationship between variables
- **Area Chart** → Growth over time

Create chart

  ```xlsx
  Insert → Charts
  ```

- Example using Python

  ```py
  import matplotlib.pyplot as plt
  import pandas as pd

  df = pd.read_csv("sales.csv")

  sales = df.groupby("product")["sales"].sum()

  sales.plot(kind="bar")

  plt.title("Sales by Product")
  plt.xlabel("Product")
  plt.ylabel("Sales")

  plt.show()
  ```

## **Dashboard Design Principles**

A good dashboard should be **simple, clear, and actionable**.

- Typical dashboard layout

  ```txt
  KPI Cards
  ↓
  Main Business Chart
  ↓
  Category Breakdown Chart
  ↓
  Detailed Table
  ↓
  Filters (Slicers)
  ```

Common dashboard components

- KPI cards
- Charts
- Pivot Tables
- Tables
- Slicers / filters

Example KPI metrics

- Total Revenue
- Total Employees
- Average Salary
- Monthly Sales
- Growth Rate

Python dashboard example

  ```py
  import streamlit as st
  import pandas as pd

  df = pd.read_csv("sales.csv")

  st.title("Sales Dashboard")

  st.metric("Total Sales", df["sales"].sum())

  product_sales = df.groupby("product")["sales"].sum()

  st.bar_chart(product_sales)
  ```

[⬆️ Go to Context](#context)
