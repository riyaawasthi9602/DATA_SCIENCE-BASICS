import pandas as pd

# Load dataset
df = pd.read_csv(
    r"try\tasks\Sample - Superstore.csv",
    encoding="latin1"
)

print("\nFirst 5 Records:\n")
print(df.head())


# -----------------------------------
# Basic Information
# -----------------------------------

print("\nDataset Shape :", df.shape)
print("\nColumns:\n", df.columns.tolist())


# -----------------------------------
# Region-wise Sales Analysis
# -----------------------------------

sales_summary = df.groupby("Region")[["Sales", "Profit"]].sum()

print("\nRegion Wise Sales & Profit:\n")
print(sales_summary)


# -----------------------------------
# Category Analysis
# -----------------------------------

category_report = df.groupby("Category").agg({
    "Sales": "sum",
    "Profit": "mean"
})

print("\nCategory Report:\n")
print(category_report)


# -----------------------------------
# Top Selling Sub-Categories
# -----------------------------------

top_products = (
    df.groupby("Sub-Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

print("\nTop Selling Products:\n")
print(top_products)


# -----------------------------------
# Profit Margin
# -----------------------------------

df["Profit_Percentage"] = (
    df["Profit"] / df["Sales"]
) * 100

print("\nProfit Percentage Added\n")

print(
    df[["Sales", "Profit", "Profit_Percentage"]]
    .head()
)


# -----------------------------------
# Sales Type Classification
# -----------------------------------

df["Sales_Level"] = df["Sales"].apply(
    lambda x: "Good" if x >= 500 else "Average"
)

print("\nSales Classification:\n")

print(
    df[["Sales", "Sales_Level"]]
    .head()
)


# -----------------------------------
# Monthly Profit Analysis
# -----------------------------------

df["Order Date"] = pd.to_datetime(df["Order Date"])

df["Month"] = df["Order Date"].dt.month_name()

monthly_profit = df.groupby("Month")["Profit"].sum()

print("\nMonthly Profit:\n")
print(monthly_profit)


# -----------------------------------
# Pivot Table
# -----------------------------------

pivot_table = pd.pivot_table(
    df,
    values="Sales",
    index="Region",
    columns="Segment",
    aggfunc="sum"
)

print("\nPivot Table:\n")
print(pivot_table)


# -----------------------------------
# Quarterly Sales
# -----------------------------------

df.set_index("Order Date", inplace=True)

quarter_sales = df["Sales"].resample("Q").sum()

print("\nQuarterly Sales:\n")
print(quarter_sales)


print("\nSales Analysis Completed Successfully!")