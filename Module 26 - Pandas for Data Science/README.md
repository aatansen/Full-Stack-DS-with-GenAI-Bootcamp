# **Context**

- [**Context**](#context)
- [**Day 31 - Pandas for Data Science**](#day-31---pandas-for-data-science)
  - [**Pandas Setup**](#pandas-setup)
  - [**Pandas Intro**](#pandas-intro)
  - [**Loading DataFrames from Files**](#loading-dataframes-from-files)
  - [**Viewing \& Sampling Data**](#viewing--sampling-data)
  - [**Accessing Data with loc and iloc**](#accessing-data-with-loc-and-iloc)
  - [**Index Manipulation**](#index-manipulation)
  - [**Setting \& Updating Values**](#setting--updating-values)
  - [**Column Access Techniques**](#column-access-techniques)
  - [**Sorting Data**](#sorting-data)
  - [**Iterating Over DataFrame (Not Recommended for Big Data)**](#iterating-over-dataframe-not-recommended-for-big-data)
  - [**Filtering Data**](#filtering-data)
  - [**Adding, Removing \& Renaming Columns**](#adding-removing--renaming-columns)
  - [**Date \& Time Handling**](#date--time-handling)
  - [**Exporting Data**](#exporting-data)
  - [**Row-wise Logic with apply()**](#row-wise-logic-with-apply)
  - [**Merging \& Joining DataFrames**](#merging--joining-dataframes)
  - [**Handling Missing (NaN) Values**](#handling-missing-nan-values)
  - [**Aggregation \& Grouping**](#aggregation--grouping)
  - [**Pivot Tables (Reshaping Data)**](#pivot-tables-reshaping-data)

# [**Day 31 - Pandas for Data Science**](./Day%2031%20-%20Pandas%20for%20Data%20Science/)

## **Pandas Setup**

- Create [venv](../Module%2010%20-%20Virtual%20Environment%20&%20Requirements/)
- Install [ipykernel](https://pypi.org/project/ipykernel/), [pandas](https://pypi.org/project/pandas/)
- pandas [docs](https://pandas.pydata.org/docs/)

[⬆️ Go to Context](#context)

## **Pandas Intro**

- Import pandas library.

  ```py
  import pandas as pd
  ```

- Create a DataFrame from a 2D list with custom columns and index.

  ```py
  df = pd.DataFrame(
      [[1,2,3],[4,5,6],[7,8,9],[10,11,12]],
      columns=['A', 'B', 'C'],
      index=["x1", "x2", "x3", "x4"]
  )
  df
  ```

- View first N rows of DataFrame.

  ```py
  df.head(2)
  ```

- View last N rows of DataFrame.

  ```py
  df.tail(2)
  ```

- Access column index object.

  ```py
  df.columns
  ```

- Convert column index to Python list.

  ```py
  df.columns.to_list()
  ```

- Access row index object.

  ```py
  df.index
  ```

- Convert row index to Python list.

  ```py
  df.index.to_list()
  ```

- Show structure, datatypes, and memory usage.

  ```py
  df.info()
  ```

- Generate statistical summary of numeric columns.

  ```py
  df.describe()
  ```

- Count unique values per column.

  ```py
  df.nunique()
  ```

- Count unique values in a specific column.

  ```py
  df["A"].nunique()
  ```

- Get unique values of a column.

  ```py
  df["A"].unique()
  ```

- Get shape as (rows, columns).

  ```py
  df.shape
  ```

- Get total number of elements (rows × columns).

  ```py
  df.size
  ```

[⬆️ Go to Context](#context)

## **Loading DataFrames from Files**

- Load CSV file into DataFrame.

  ```py
  coffee = pd.read_csv("warmup-data/coffee.csv")
  coffee.head()
  ```

- Load Parquet file into DataFrame.

  ```py
  results = pd.read_parquet("data/results.parquet")
  results.head()
  ```

- Load another CSV file.

  ```py
  bios = pd.read_csv("data/bios.csv")
  bios.head()
  ```

- Load Excel file with specific sheet.

  ```py
  olympics_data = pd.read_excel(
      "data/olympics-data.xlsx",
      sheet_name='results'
  )
  olympics_data.head()
  ```

[⬆️ Go to Context](#context)

## **Viewing & Sampling Data**

- Print entire DataFrame (console).

  ```py
  print(coffee)
  ```

- Display DataFrame nicely in notebooks.

  ```py
  display(coffee)
  ```

- Randomly sample rows.

  ```py
  coffee.sample(5)
  ```

[⬆️ Go to Context](#context)

## **Accessing Data with loc and iloc**

- Access a full row by label-based index.

  ```py
  coffee.loc[0]
  ```

- Access a specific cell using labels.

  ```py
  coffee.loc[0, "Coffee Type"]
  ```

- Access multiple rows by labels.

  ```py
  coffee.loc[[0,1,2]]
  ```

- Access a cell using integer positions.

  ```py
  coffee.iloc[0, 1]
  ```

- Select all rows but specific columns by position.

  ```py
  coffee.iloc[:, [0,2]]
  ```

[⬆️ Go to Context](#context)

## **Index Manipulation**

- Change DataFrame index to a column.

  ```py
  coffee.index = coffee["Day"]
  coffee.head()
  ```

- Access row using new index label.

  ```py
  coffee.loc["Monday", "Coffee Type"]
  ```

[⬆️ Go to Context](#context)

## **Setting & Updating Values**

- Reload DataFrame to reset changes.

  ```py
  coffee = pd.read_csv('./warmup-data/coffee.csv')
  ```

- Update a column value for a slice of rows.

  ```py
  coffee.loc[1:3, "Units Sold"] = 10
  coffee.head()
  ```

[⬆️ Go to Context](#context)

## **Column Access Techniques**

- Access column using bracket notation.

  ```py
  coffee["Day"]
  ```

- Access column using dot notation.

  ```py
  coffee.Day
  ```

- Store a column as Series (1D).

  ```py
  s = coffee['Coffee Type']
  s
  ```

[⬆️ Go to Context](#context)

## **Sorting Data**

- Sort DataFrame by one column descending.

  ```py
  coffee.sort_values(["Units Sold"], ascending=False)
  ```

- Sort by multiple columns with mixed order.

  ```py
  coffee.sort_values(
      ["Units Sold", "Coffee Type"],
      ascending=[1, 0]
  )
  ```

[⬆️ Go to Context](#context)

## **Iterating Over DataFrame (Not Recommended for Big Data)**

- Iterate row-by-row using iterrows().

  ```py
  for index, row in coffee.iterrows():
      print(f"Index: {index}")
      print(f"Row Data:\n{row}")
      print(f"Coffee Type: {row['Coffee Type']}")
      print("--")
  ```

[⬆️ Go to Context](#context)

## **Filtering Data**

- Create boolean mask from condition.

  ```py
  bios["height_cm"] > 215
  ```

- Filter rows using boolean mask.

  ```py
  temp = bios.loc[bios["height_cm"] > 215]
  temp.head()
  ```

- Filter rows and select columns.

  ```py
  bios.loc[bios["height_cm"] > 215, ["name", "height_cm"]]
  ```

- Shorthand filtering without `.loc`.

  ```py
  bios[bios['height_cm'] > 215][["name", "height_cm"]]
  ```

- Apply multiple filter conditions.

  ```py
  bios[
      (bios['height_cm'] > 215) &
      (bios['born_country'] == 'USA')
  ]
  ```

- Filter rows using string matching.

  ```py
  bios[bios['name'].str.contains("keith", case=False)]
  ```

- Use query syntax for readable filtering.

  ```py
  bios.query('born_country == "USA" and born_city == "Seattle"')
  ```

[⬆️ Go to Context](#context)

## **Adding, Removing & Renaming Columns**

- Add constant-value column.

  ```py
  coffee["price"] = 4.99
  ```

- Conditionally assign values using NumPy.

  ```py
  import numpy as np

  coffee["new_price"] = np.where(
      coffee["Coffee Type"] == "Espresso",
      3.99,
      5.99
  )
  ```

- Remove a column from DataFrame.

  ```py
  coffee.drop(columns=["price"], inplace=True)
  ```

- Create computed column from arithmetic.

  ```py
  coffee["revenue"] = coffee["Units Sold"] * coffee["new_price"]
  ```

- Rename column names.

  ```py
  coffee.rename(columns={"new_price": "price"}, inplace=True)
  ```

[⬆️ Go to Context](#context)

## **Date & Time Handling**

- Convert string column to datetime.

  ```py
  bios["died_datetime"] = pd.to_datetime(bios["died_date"])
  ```

- Extract year from datetime column.

  ```py
  bios["died_year"] = bios["died_datetime"].dt.year
  ```

[⬆️ Go to Context](#context)

## **Exporting Data**

- Save DataFrame to CSV without index.

  ```py
  bios.to_csv("data/temp_bios.csv", index=False)
  ```

[⬆️ Go to Context](#context)

## **Row-wise Logic with apply()**

- Define custom classification logic.

  ```py
  def categorize_athlete(row):
      if row['height_cm'] < 175 and row['weight_kg'] < 70:
          return 'Lightweight'
      elif row['height_cm'] < 185 or row['weight_kg'] <= 80:
          return 'Middleweight'
      else:
          return 'Heavyweight'
  ```

- Apply function row-wise.

  ```py
  bios["Category"] = bios.apply(categorize_athlete, axis=1)
  bios
  ```

[⬆️ Go to Context](#context)

## **Merging & Joining DataFrames**

- Load lookup table for merging.

  ```py
  nocs = pd.read_csv('./data/noc_regions.csv')
  ```

- Merge DataFrames using different key names.

  ```py
  bios_new = pd.merge(
      bios,
      nocs,
      left_on="born_country",
      right_on="NOC"
  )
  bios_new.head()
  ```

[⬆️ Go to Context](#context)

## **Handling Missing (NaN) Values**

- Detect missing values per column.

  ```py
  coffee.isnull().sum()
  ```

- Introduce NaN values manually.

  ```py
  coffee.loc[[2,3], 'Units Sold'] = np.nan
  ```

- Fill missing values with column mean.

  ```py
  coffee["Units Sold"].fillna(
      coffee["Units Sold"].mean(),
      inplace=True
  )
  ```

- Drop rows with NaN in specific column.

  ```py
  coffee.dropna(subset=['Units Sold'], inplace=True)
  ```

[⬆️ Go to Context](#context)

## **Aggregation & Grouping**

- Count frequency of values in a column.

  ```py
  bios['born_city'].value_counts()
  ```

- Aggregate using groupby with sum.

  ```py
  coffee.groupby(["Coffee Type"])["Units Sold"].sum()
  ```

- Aggregate using groupby with mean.

  ```py
  coffee.groupby(["Coffee Type"])["Units Sold"].mean()
  ```

[⬆️ Go to Context](#context)

## **Pivot Tables (Reshaping Data)**

- Create pivot table from DataFrame.

  ```py
  pivot = coffee.pivot(
      columns="Coffee Type",
      index="Day",
      values="revenue"
  )
  pivot
  ```

[⬆️ Go to Context](#context)
