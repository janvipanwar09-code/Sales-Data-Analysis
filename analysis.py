import pandas as pd
import matplotlib.pyplot as plt


# Load sales dataset
df = pd.read_csv("data/sales_data.csv")


# Basic information
print("\n--- Dataset Overview ---")
print(df.head())

print("\n--- Dataset Information ---")
print(df.info())

print("\n--- Summary Statistics ---")
print(df.describe())


# Total sales
total_sales = df["Sales"].sum()

print("\nTotal Sales:", total_sales)


# Product-wise sales
product_sales = df.groupby("Product")["Sales"].sum().sort_values(
    ascending=False
)

print("\n--- Product-wise Sales ---")
print(product_sales)


# Category-wise sales
category_sales = df.groupby("Category")["Sales"].sum().sort_values(
    ascending=False
)

print("\n--- Category-wise Sales ---")
print(category_sales)


# Region-wise sales
region_sales = df.groupby("Region")["Sales"].sum().sort_values(
    ascending=False
)

print("\n--- Region-wise Sales ---")
print(region_sales)


# Monthly sales
df["Date"] = pd.to_datetime(df["Date"])

monthly_sales = (
    df.groupby(df["Date"].dt.to_period("M"))["Sales"]
    .sum()
)

print("\n--- Monthly Sales ---")
print(monthly_sales)


# Product sales chart
plt.figure(figsize=(10, 5))

product_sales.plot(kind="bar")

plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")

plt.tight_layout()
plt.show()
