import pandas as pd

# -----------------------------------
# Load Datasets
# -----------------------------------

orders = pd.read_csv(r"try\tasks\olist_orders_dataset.csv")

customers = pd.read_csv(r"try\tasks\olist_customers_dataset.csv")

items = pd.read_csv(r"try\tasks\olist_order_items_dataset.csv")

products = pd.read_csv(r"try\tasks\olist_products_dataset.csv")

payments = pd.read_csv(r"try\tasks\olist_order_payments_dataset.csv")


# -----------------------------------
# Combine DataFrames
# -----------------------------------

data = pd.merge(
    orders,
    customers,
    on="customer_id"
)

data = pd.merge(
    data,
    items,
    on="order_id"
)

data = pd.merge(
    data,
    products,
    on="product_id",
    how="left"
)

data = pd.merge(
    data,
    payments,
    on="order_id",
    how="left"
)


# -----------------------------------
# Dataset Overview
# -----------------------------------

print("\nDataset Shape :", data.shape)

print("\nColumns Available:\n")
print(data.columns.tolist())


# -----------------------------------
# Revenue Analysis
# -----------------------------------

customer_sales = (
    data.groupby("customer_unique_id")["price"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTop Customers by Revenue:\n")
print(customer_sales.head())


# -----------------------------------
# Orders Per Customer
# -----------------------------------

customer_orders = (
    data.groupby("customer_unique_id")["order_id"]
    .nunique()
)

single_order_users = customer_orders[
    customer_orders == 1
]

print("\nCustomers With One Order :")
print(len(single_order_users))


# -----------------------------------
# Date Processing
# -----------------------------------

data["order_purchase_timestamp"] = pd.to_datetime(
    data["order_purchase_timestamp"]
)

data["Year"] = (
    data["order_purchase_timestamp"]
    .dt.year
)

data["Month"] = (
    data["order_purchase_timestamp"]
    .dt.month_name()
)


# -----------------------------------
# Product Category Cleaning
# -----------------------------------

data["product_category_name"] = (
    data["product_category_name"]
    .fillna("Unknown")
    .str.upper()
)

print("\nProduct Categories Updated\n")


# -----------------------------------
# Pivot Table
# -----------------------------------

state_sales = pd.pivot_table(
    data,
    values="price",
    index="Year",
    columns="customer_state",
    aggfunc="sum"
)

print("\nState Wise Sales:\n")
print(state_sales.head())


# -----------------------------------
# Monthly Revenue
# -----------------------------------

monthly_sales = (
    data.groupby(["Year", "Month"])["price"]
    .sum()
)

print("\nMonthly Revenue:\n")
print(monthly_sales.head(10))


# -----------------------------------
# Delivery Time Analysis
# -----------------------------------

data["order_delivered_customer_date"] = pd.to_datetime(
    data["order_delivered_customer_date"]
)

data["Delivery_Time"] = (
    data["order_delivered_customer_date"]
    -
    data["order_purchase_timestamp"]
).dt.days


avg_delivery = data["Delivery_Time"].mean()

print(f"\nAverage Delivery Time : {avg_delivery:.2f} days")


# -----------------------------------
# Slow Delivery Cities
# -----------------------------------

slow_cities = (
    data.groupby("customer_city")["Delivery_Time"]
    .mean()
    .sort_values(ascending=False)
)

print("\nCities With Slow Delivery:\n")
print(slow_cities.head())


# -----------------------------------
# Payment Analysis
# -----------------------------------

payment_modes = (
    data["payment_type"]
    .value_counts()
)

print("\nPayment Methods Used:\n")
print(payment_modes)


# -----------------------------------
# Top Revenue States
# -----------------------------------

top_states = (
    data.groupby("customer_state")["price"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTop Revenue States:\n")
print(top_states.head())


print("\nE-commerce Data Analysis Completed!")