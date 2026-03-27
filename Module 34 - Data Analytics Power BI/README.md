# **Context**

- [**Context**](#context)
- [**Day 57 - Introduction to Power BI**](#day-57---introduction-to-power-bi)
  - [**Why Power BI? Why not Excel or Google Sheets?**](#why-power-bi-why-not-excel-or-google-sheets)
  - [**Power BI Architecture**](#power-bi-architecture)
  - [**What is ETL, and why is it needed?**](#what-is-etl-and-why-is-it-needed)
  - [**Relationships In Power BI**](#relationships-in-power-bi)
  - [**Drill Down vs Drill Up**](#drill-down-vs-drill-up)
    - [1. Drill Down](#1-drill-down)
    - [2. Drill Up](#2-drill-up)
    - [The 4 Drill Buttons](#the-4-drill-buttons)
  - [**4 Types of Relationships in Power BI (Model View)**](#4-types-of-relationships-in-power-bi-model-view)
    - [1. One-to-One (1:1)](#1-one-to-one-11)
    - [2. One-to-Many (1:\*)](#2-one-to-many-1)
    - [3. Many-to-One (\*:1)](#3-many-to-one-1)
    - [4. Many-to-Many (*:*)](#4-many-to-many-)
  - [**For Data Modeling**](#for-data-modeling)
- [**Day 58 - Power BI Part 02**](#day-58---power-bi-part-02)
  - [**1. Matrix (Visual)**](#1-matrix-visual)
  - [**2. Filter Button / Slicer**](#2-filter-button--slicer)
  - [**3. Bookmark**](#3-bookmark)
  - [**4. Navigation**](#4-navigation)
  - [**5. Map (Visual)**](#5-map-visual)
- [**Day 59 - Power BI Part 03**](#day-59---power-bi-part-03)
  - [**1. Drill Through**](#1-drill-through)
  - [**2. Fiscal Calendar**](#2-fiscal-calendar)
  - [**3. DAX Formula (Data Analysis Expressions - DAX)**](#3-dax-formula-data-analysis-expressions---dax)
  - [**4. DAX Key Concepts**](#4-dax-key-concepts)

# **Day 57 - Introduction to Power BI**

## **Why Power BI? Why not Excel or Google Sheets?**

1. **Visualization Power:**

   - Excel charts are often limited and manual.
   - Power BI is designed specifically for visualization, allowing you to create professional, interactive, and dynamic dashboards with just a few clicks.

2. **Large Data Handling:**

   - Excel slows down significantly with large datasets.
   - Power BI can handle millions of rows efficiently using a columnar storage model and compression.

3. **Data Modeling & Relationship:**

   - Instead of complex VLOOKUP or INDEX-MATCH formulas, Power BI allows you to build data models by dragging and dropping relationships between multiple tables.

4. **Automation & Refresh**

   - Power BI allows for scheduled auto-refresh, eliminating manual data entry.
   - You can use a gateway to connect to live data.

5. **DAX (Data Analysis Expressions)**

   - A formula language more powerful than Excel formulas.
   - Used for complex calculations like Year-Over-Year (YOY) growth, running totals, and time intelligence.

6. **Security & Sharing**

   - Offers Row-Level Security (RLS) to control who sees what data.
   - Dashboards are easily published to the web or mobile apps, whereas Excel sharing is often file-based and less secure.

[⬆️ Go to Context](#context)

## **Power BI Architecture**

  ```mermaid
  graph LR
      %% Data Sources
      subgraph Sources [Data Sources]
          DB[(MySQL)]
          XLS[Excel / Files]
      end

      %% ETL Process
      Sources -- Extract --> Transform{Transform}
      Transform -- Load --> DW[(Data Warehouse)]

      %% Output
      DW --> Viz[Visualization / Dashboards]
      Viz --> User((User))

      %% Styling
      style Sources fill:#f9f9f9,stroke:#333,stroke-dasharray: 5 5,color:#ffffff
      style DB color:#ffffff
      style XLS color:#ffffff

      style Transform fill:#e1f5fe,stroke:#01579b,color:#000000
      style DW fill:#fff9c4,stroke:#fbc02d,color:#000000
      style Viz fill:#e8f5e9,stroke:#2e7d32,color:#000000
      style User fill:#f3e5f5,stroke:#7b1fa2,color:#000000
  ```

- **Extract:** Data is pulled from various sources like MySQL databases and flat files (Excel/CSV).
- **Transform:** Data is cleaned and modeled (this is where Power Query and DAX usually sit).
- **Load:** The processed data is stored in the Data Warehouse/Model.
- **Visualization:** The final output is created as interactive charts and dashboards.
- **User:** The stakeholder interacts with the insights.

[⬆️ Go to Context](#context)

## **What is ETL, and why is it needed?**

- **ETL—Extract, Transform, Load**

  1. **Extract (Data Import):** Bringing data in from various sources (Excel, SQL, and web).
  2. **Transform (Cleaning & Changing)**

     - Raw data is usually messy.
     - You use **Power Query Editor** to clean (remove nulls, fix spelling), format (change text to dates/numbers), split columns, or merge tables.
     - This makes the data analysis ready.

  3. **Load:** Once transformed, the data is loaded into the main Power BI model to be used for visuals and DAX measures.

[⬆️ Go to Context](#context)

## **Relationships In Power BI**

- Fact table and Dimension table

   ```mermaid
   erDiagram
      FACT_EMPLOYEE_METRICS {
         int EmployeeID
         int DepartmentID
         int StatusID
         decimal BasicSalary
      }

      DIM_EMPLOYEE {
         int EmployeeID
         string Name
         string Gender
         string DistanceFromOffice
         string EmployeeCategory
      }

      DIM_DEPARTMENT {
         int DepartmentID
         string DepartmentName
      }

      DIM_STATUS {
         int StatusID
         string WorkingStatus
      }

      DIM_EMPLOYEE ||--o{ FACT_EMPLOYEE_METRICS : EmployeeID
      DIM_DEPARTMENT ||--o{ FACT_EMPLOYEE_METRICS : DepartmentID
      DIM_STATUS ||--o{ FACT_EMPLOYEE_METRICS : StatusID
   ```

[⬆️ Go to Context](#context)

## **Drill Down vs Drill Up**

### 1. Drill Down

**Drill Down = Go from higher level → lower level (more detail).**

Example hierarchy:

- Year
- Quarter
- Month
- Day

If a chart shows **Sales by Year**, drilling down lets you see:

- 2024 → Q1, Q2, Q3, Q4
- Then → Months inside Q1

Example

Suppose a chart shows:

  | Department  | Employees |
  | ----------- | --------- |
  | Engineering | 120       |
  | HR          | 20        |

[⬆️ Go to Context](#context)

### 2. Drill Up

**Drill Up = Go from lower level → higher level (summary).**

Example:

You drilled into:

- Year → Quarter → Month

Now drill up returns to:

- Quarter → Year

[⬆️ Go to Context](#context)

### The 4 Drill Buttons

Power BI actually has **4 navigation options**:

- **Drill Down**
  Click a bar to go to the next level for that specific item.

- **Go to Next Level**
  Moves the whole chart down one level.

- **Expand All Down One Level**
  Shows both parent and child levels together.

- **Drill Up**
  Return to previous level.

[⬆️ Go to Context](#context)

## **4 Types of Relationships in Power BI (Model View)**

### 1. One-to-One (1:1)

One record in **Table A** matches **one record in Table B**.

Example:

  | EmployeeID | Name  |
  | ---------- | ----- |
  | 101        | Rahim |

  | EmployeeID | Passport |
  | ---------- | -------- |
  | 101        | A12345   |

Relationship:

  ```xlsx
  Employees.EmployeeID  →  Passport.EmployeeID
  ```

- Each **EmployeeID appears once in both tables**.

Typical use cases:

- Split sensitive data into another table
- Profile tables

---

[⬆️ Go to Context](#context)

### 2. One-to-Many (1:*)

This is the **most common relationship in Power BI**.

One record in **Table A** relates to **many records in Table B**.

Example:

  | DepartmentID | Department  |
  | ------------ | ----------- |
  | D1           | HR          |
  | D2           | Engineering |

  | EmployeeID | DepartmentID |
  | ---------- | ------------ |
  | 1          | D1           |
  | 2          | D2           |
  | 3          | D2           |

Relationship:

  ```xlsx
  Department (1)  →  Employee (*)
  ```

Meaning:

- One **Department**
- Many **Employees**

This is the **typical Fact–Dimension relationship**.

---

[⬆️ Go to Context](#context)

### 3. Many-to-One (*:1)

This is basically the **same relationship but viewed from the opposite side**.

Example:

Employee table connecting to Department table:

  ```xlsx
  Employee (*) → Department (1)
  ```

Meaning:

- Many employees belong to **one department**.

Power BI internally treats **One-to-Many and Many-to-One the same**, just reversed.

---

[⬆️ Go to Context](#context)

### 4. Many-to-Many (*:*)

Many records in **Table A** relate to **many records in Table B**.

Example:

| Student | Course  |
| ------- | ------- |
| A       | Math    |
| A       | Physics |
| B       | Math    |

Here:

- One student can take **many courses**
- One course can have **many students**

Relationship:

  ```xlsx
  Student (*)
    ↕
  Course (*)
  ```

Usually solved with a **bridge table**:

  ```xlsx
  Students
    ↓
  Enrollment (Bridge)
    ↓
  Courses
  ```

---

- Simple Visual Idea

  ```xlsx
  1:1   →  One ↔ One

  1:*   →  One → Many

  *:1   →  Many → One

  *:*   →  Many ↔ Many
  ```

---

[⬆️ Go to Context](#context)

## **For Data Modeling**

In most **Power BI dashboards**, the ideal structure is:

  ```xlsx
  Dimension Table (1)
          ↓
  Fact Table (*)
  ```

Example:

  ```xlsx
  Departments (1)
        ↓
  Employees (*)
  ```

This is called a **Star Schema**, which is the **best practice for Power BI models**.

[⬆️ Go to Context](#context)

# **Day 58 - Power BI Part 02**

## **1. Matrix (Visual)**

- A table-like visual that supports **hierarchical data** (rows + columns + values)

- Similar to Pivot Table in Excel

- **Key Features**

  - Row & Column grouping
  - Drill down / expand-collapse hierarchy
  - Subtotals and grand totals
  - Conditional formatting

- **When to use**

  - When you need **multi-level analysis**

    - Region → Country → City
    - Category → Subcategory → Product

---

[⬆️ Go to Context](#context)

## **2. Filter Button / Slicer**

- Used to **filter data interactively** in reports

- Slicer is the visual version of filters placed on canvas

- **Key Features**

  - Visual-level, Page-level, and Report-level filtering
  - Multiple formats (dropdown, list, date, range slider)
  - Search inside slicer
  - Single-select or multi-select

- **When to use**

  - When users need to **control what data they see**

    - Filter by Region
    - Filter by Date
    - Filter by Category

---

[⬆️ Go to Context](#context)

## **3. Bookmark**

- Saves the **current state of a report**

  - Filters
  - Visual visibility
  - Drill position

- **Key Features**

  - Capture report view (data + display)
  - Toggle between visuals (show/hide)
  - Works with Selection Pane
  - Can control navigation

- **When to use**

  - When creating **interactive reports**

    - Toggle Chart ↔ Table
    - Create storytelling dashboards
    - Build custom UI experience

---

[⬆️ Go to Context](#context)

## **4. Navigation**

- Helps users **move between pages or report states**

- **Key Features**

  - Page Navigator (auto page buttons)
  - Bookmark Navigator
  - Drill-through navigation
  - Custom buttons with actions

- **When to use**

  - When designing **multi-page dashboards**

    - Switch between report pages
    - Navigate using bookmarks
    - Create app-like experience

---

[⬆️ Go to Context](#context)

## **5. Map (Visual)**

- Displays data based on **geographical locations**

- Useful for identifying regional patterns

- **Key Features**

  - Bubble maps (size based on value)
  - Filled maps (color by region)
  - Zoom, pan, and tooltips
  - Supports Latitude & Longitude

- **When to use**

  - When analyzing **location-based data**

    - Sales by country or city
    - Regional performance comparison
    - Geographic trends

[⬆️ Go to Context](#context)

# **Day 59 - Power BI Part 03**

## **1. Drill Through**

- A feature that allows users to **navigate from a summary report to a detailed report page** using a selected data point.

- **Key Features**

  - Passes filters automatically from source visual
  - Works on specific fields (e.g., Product, Customer, Region)
  - Provides deep-level analysis
  - Can include back button for navigation

- **How to Use**

  - Create a new page (Drill Through Page)
  - Add a field to the **Drill-through filters pane**
  - Design visuals for detailed analysis
  - Right-click on a visual → Select Drill Through → Choose page

- **When to Use**

  - When you want **detailed breakdown**

    - Summary: Total Sales by Product
    - Drill Through: Detailed transactions of selected product

---

[⬆️ Go to Context](#context)

## **2. Fiscal Calendar**

- A **custom calendar** where the year does not start in January (e.g., starts in April)

- **Key Features**

  - Supports business-specific reporting periods
  - Enables proper financial analysis (FY, Quarter, Month)
  - Aligns with accounting standards

- **Common Setup (April Start Example)**

  - **Create Calendar Table**

    - `Calendar = CALENDARAUTO(3)`

  - **Add Columns**

    - Month Name

      - `Month = FORMAT('Calendar'[Date], "mmm")`

    - Month Sort (April = 1)

      - `Month Sort = MONTH(EDATE('Calendar'[Date], -3))`

    - Quarter

      - `Qtr = FORMAT(EDATE('Calendar'[Date], -3), "\QQ")`

    - Fiscal Year

      ```dax
      FY = 
      VAR Check = MONTH('Calendar'[Date]) >= 4
      VAR CY = RIGHT(YEAR('Calendar'[Date]), 2)
      VAR NY = RIGHT(YEAR('Calendar'[Date]) + 1, 2)
      VAR PY = RIGHT(YEAR('Calendar'[Date]) - 1, 2)
      RETURN
      IF(Check, CY & "-" & NY, PY & "-" & CY)
      ```

- **When to Use**

  - Financial dashboards
  - Budget vs Actual analysis
  - Year-over-Year comparison based on fiscal periods

---

[⬆️ Go to Context](#context)

## **3. DAX Formula (Data Analysis Expressions - DAX)**

- A formula language used in Power BI for:

  - Calculations
  - Measures
  - Custom columns

---

- **Basic Aggregation Functions**

  - **SUM**

    - Adds values
    - Example: `Total Sales = SUM(Sales[Amount])`

  - **MIN / MAX**

    - Finds smallest / largest value
    - Example: `MAX(Products[Price])`

  - **AVERAGE**

    - Calculates mean
    - Example: `AVERAGE(Sales[Amount])`

---

- **Iterator Functions (Row-by-Row Calculation)**

  - **SUMX**

    - Row calculation + total
    - Example:

      `SUMX(Sales, Sales[Quantity] * Sales[UnitPrice])`

  - **AVERAGEX**

    - Row calculation + average
    - Example:

      `AVERAGEX(Sales, Sales[Price] - Sales[Cost])`

  - **MINX / MAXX**

    - Row-based min/max

  - **COUNTX**

    - Counts non-blank results of expression

---

- **Counting Functions**

  - **COUNTROWS**

    - Counts rows

  - **DISTINCTCOUNT**

    - Counts unique values

  - **COUNTBLANK**

    - Counts empty values

---

- **Logical & Conditional Functions**

  - **IF**

    - Condition check
    - Example:
      `IF([Total Sales] > 10000, "High", "Low")`

  - **SWITCH**

    - Multiple conditions (cleaner than IF)

---

- **Mathematical & Safe Operations**

  - **DIVIDE**

    - Safe division (avoids errors)
    - Example:
      `DIVIDE(SUM(Sales[Profit]), SUM(Sales[Sales]), 0)`

---

- **Filter & Context Functions (Most Important)**

  - **CALCULATE**

    - Changes filter context
    - Example:
      `CALCULATE(SUM(Sales[Amount]), Products[Color] = "Red")`

  - **FILTER**

    - Applies custom filtering logic

  - **ALL**

    - Removes filters (used in % calculations)

---

- **Relationship Functions**

  - **RELATED**

    - Fetch value from related table

---

- **Time Intelligence Functions**

  - **TOTALYTD**

    - Year-to-date calculation

  - **DATEADD**

    - Shift time (last month/year)

---

- **Table Functions**

  - **SUMMARIZE**

    - Creates summary table

  - **VALUES**

    - Returns unique values

---

- **Ranking & Text Functions**

  - **RANKX**

    - Ranking calculation

  - **CONCATENATE / &**

    - Combine text

  - **UPPER / LOWER**

    - Text case formatting

  - **LEFT / RIGHT**

    - Extract characters

---

[⬆️ Go to Context](#context)

## **4. DAX Key Concepts**

- **Row Context**

  - Calculation happens **row by row**
  - Used in calculated columns and iterator functions (SUMX, etc.)

- **Filter Context**

  - Filters applied from:

    - Visuals
    - Slicers
    - CALCULATE

- **Context Transition**

  - When CALCULATE turns row context into filter context

---

[⬆️ Go to Context](#context)

