import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs("charts", exist_ok=True)

df = pd.read_csv("beats_data_cleaned.csv")

sns.set_theme(style="darkgrid")
BEATS_RED = "#E31837"

# --- 1. Sales by Product ---
plt.figure(figsize=(10, 6))
product_sales = df["product"].value_counts()
sns.barplot(x=product_sales.values, y=product_sales.index, color=BEATS_RED)
plt.title("Units Sold by Product", fontsize=16, fontweight="bold")
plt.xlabel("Units Sold")
plt.ylabel("")
plt.tight_layout()
plt.savefig("charts/01_sales_by_product.png", dpi=150)
plt.close()
print("✅ Chart 1 saved")

# --- 2. Revenue by Product ---
plt.figure(figsize=(10, 6))
revenue_by_product = df.groupby("product")["revenue"].sum().sort_values()
sns.barplot(x=revenue_by_product.values, y=revenue_by_product.index, color=BEATS_RED)
plt.title("Total Revenue by Product", fontsize=16, fontweight="bold")
plt.xlabel("Revenue (USD)")
plt.ylabel("")
plt.tight_layout()
plt.savefig("charts/02_revenue_by_product.png", dpi=150)
plt.close()
print("✅ Chart 2 saved")

# --- 3. Average Rating by Product ---
plt.figure(figsize=(10, 6))
avg_rating = df.groupby("product")["rating"].mean().sort_values()
sns.barplot(x=avg_rating.values, y=avg_rating.index, color=BEATS_RED)
plt.title("Average Rating by Product", fontsize=16, fontweight="bold")
plt.xlabel("Average Rating (out of 5)")
plt.ylabel("")
plt.xlim(0, 5)
plt.tight_layout()
plt.savefig("charts/03_avg_rating_by_product.png", dpi=150)
plt.close()
print("✅ Chart 3 saved")

# --- 4. Sales by Region ---
plt.figure(figsize=(8, 6))
region_sales = df["region"].value_counts()
colors = [BEATS_RED if i == 0 else "#555555" for i in range(len(region_sales))]
plt.pie(region_sales.values, labels=region_sales.index, colors=colors,
        autopct="%1.1f%%", startangle=140)
plt.title("Sales Distribution by Region", fontsize=16, fontweight="bold")
plt.tight_layout()
plt.savefig("charts/04_sales_by_region.png", dpi=150)
plt.close()
print("✅ Chart 4 saved")

# --- 5. Sales by Age Group ---
plt.figure(figsize=(8, 6))
age_sales = df["age_group"].value_counts().sort_index()
sns.barplot(x=age_sales.index, y=age_sales.values, color=BEATS_RED)
plt.title("Sales by Age Group", fontsize=16, fontweight="bold")
plt.xlabel("Age Group")
plt.ylabel("Units Sold")
plt.tight_layout()
plt.savefig("charts/05_sales_by_age_group.png", dpi=150)
plt.close()
print("✅ Chart 5 saved")

# --- 6. Monthly Sales Trend ---
plt.figure(figsize=(12, 6))
monthly = df.groupby(["year", "month"]).size().reset_index(name="sales")
monthly["period"] = monthly["year"].astype(str) + "-" + monthly["month"].astype(str).str.zfill(2)
sns.lineplot(data=monthly, x="period", y="sales", color=BEATS_RED, linewidth=2.5, marker="o")
plt.title("Monthly Sales Trend", fontsize=16, fontweight="bold")
plt.xlabel("Month")
plt.ylabel("Units Sold")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("charts/06_monthly_sales_trend.png", dpi=150)
plt.close()
print("✅ Chart 6 saved")

# --- Summary Stats ---
print("\n=== KEY STATS ===")
print(f"Total Revenue: ${df['revenue'].sum():,.2f}")
print(f"Total Units Sold: {len(df)}")
print(f"Average Rating: {df['rating'].mean():.2f} / 5")
print(f"Best Selling Product: {df['product'].value_counts().idxmax()}")
print(f"Top Region: {df['region'].value_counts().idxmax()}")
print("\n✅ All charts saved to /charts folder!")