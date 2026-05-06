import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.patches import FancyBboxPatch
import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv("beats_data_final.csv")
BEATS_RED = "#E31837"
DARK = "#1a1a1a"
GRAY = "#555555"

fig = plt.figure(figsize=(20, 24), facecolor=DARK)
fig.suptitle("BEATS BY DRE — CUSTOMER ANALYTICS REPORT",
             fontsize=26, fontweight="bold", color="white", y=0.98)

gs = gridspec.GridSpec(4, 2, figure=fig, hspace=0.45, wspace=0.35)

# --- 1. Units Sold by Product ---
ax1 = fig.add_subplot(gs[0, 0])
product_sales = df["product"].value_counts()
ax1.barh(product_sales.index, product_sales.values, color=BEATS_RED)
ax1.set_title("Units Sold by Product", color="white", fontweight="bold", fontsize=13)
ax1.tick_params(colors="white")
ax1.set_facecolor(DARK)
for spine in ax1.spines.values():
    spine.set_edgecolor(GRAY)

# --- 2. Revenue by Product ---
ax2 = fig.add_subplot(gs[0, 1])
revenue = df.groupby("product")["revenue"].sum().sort_values()
ax2.barh(revenue.index, revenue.values, color=BEATS_RED)
ax2.set_title("Total Revenue by Product (USD)", color="white", fontweight="bold", fontsize=13)
ax2.tick_params(colors="white")
ax2.set_facecolor(DARK)
for spine in ax2.spines.values():
    spine.set_edgecolor(GRAY)

# --- 3. Sentiment Distribution ---
ax3 = fig.add_subplot(gs[1, 0])
sentiment = df["sentiment"].value_counts()
colors_s = [BEATS_RED if s == "Positive" else GRAY if s == "Neutral" else "#222222"
            for s in sentiment.index]
ax3.bar(sentiment.index, sentiment.values, color=colors_s)
ax3.set_title("Customer Sentiment Distribution", color="white", fontweight="bold", fontsize=13)
ax3.tick_params(colors="white")
ax3.set_facecolor(DARK)
for spine in ax3.spines.values():
    spine.set_edgecolor(GRAY)

# --- 4. Avg Rating by Product ---
ax4 = fig.add_subplot(gs[1, 1])
avg_rating = df.groupby("product")["rating"].mean().sort_values()
ax4.barh(avg_rating.index, avg_rating.values, color=BEATS_RED)
ax4.set_title("Average Rating by Product", color="white", fontweight="bold", fontsize=13)
ax4.set_xlim(0, 5)
ax4.tick_params(colors="white")
ax4.set_facecolor(DARK)
for spine in ax4.spines.values():
    spine.set_edgecolor(GRAY)

# --- 5. Sales by Region ---
ax5 = fig.add_subplot(gs[2, 0])
region = df["region"].value_counts()
ax5.pie(region.values, labels=region.index, autopct="%1.1f%%",
        colors=[BEATS_RED, GRAY, "#333333", "#777777", "#999999"],
        textprops={"color": "white"})
ax5.set_title("Sales by Region", color="white", fontweight="bold", fontsize=13)
ax5.set_facecolor(DARK)

# --- 6. Monthly Trend ---
ax6 = fig.add_subplot(gs[2, 1])
monthly = df.groupby(["year", "month"]).size().reset_index(name="sales")
monthly["period"] = monthly["year"].astype(str) + "-" + monthly["month"].astype(str).str.zfill(2)
ax6.plot(monthly["period"], monthly["sales"], color=BEATS_RED, linewidth=2.5, marker="o")
ax6.set_title("Monthly Sales Trend", color="white", fontweight="bold", fontsize=13)
ax6.tick_params(colors="white", axis="both")
ax6.set_xticklabels(monthly["period"], rotation=45, ha="right", fontsize=7)
ax6.set_facecolor(DARK)
for spine in ax6.spines.values():
    spine.set_edgecolor(GRAY)

# --- 7. Key Metrics Summary Box ---
ax7 = fig.add_subplot(gs[3, :])
ax7.set_facecolor("#2a2a2a")
ax7.axis("off")
for spine in ax7.spines.values():
    spine.set_edgecolor(BEATS_RED)

total_revenue = df["revenue"].sum()
avg_rating = df["rating"].mean()
best_product = df["product"].value_counts().idxmax()
top_region = df["region"].value_counts().idxmax()
positive_pct = (df["sentiment"] == "Positive").sum() / len(df) * 100
avg_sentiment = df["sentiment_score"].mean()

metrics = [
    ("💰 Total Revenue", f"${total_revenue:,.0f}"),
    ("📦 Units Sold", f"{len(df):,}"),
    ("⭐ Avg Rating", f"{avg_rating:.2f} / 5"),
    ("🏆 Best Product", best_product.replace("Beats ", "")),
    ("🌍 Top Region", top_region),
    ("😊 Positive Reviews", f"{positive_pct:.1f}%"),
]

for i, (label, value) in enumerate(metrics):
    x = 0.08 + (i % 3) * 0.33
    y = 0.65 if i < 3 else 0.2
    ax7.text(x, y, label, transform=ax7.transAxes,
             fontsize=11, color=GRAY, fontweight="bold")
    ax7.text(x, y - 0.2, value, transform=ax7.transAxes,
             fontsize=14, color="white", fontweight="bold")

ax7.set_title("KEY BUSINESS METRICS", color=BEATS_RED,
              fontweight="bold", fontsize=14, pad=10)

plt.savefig("charts/BEATS_ANALYTICS_REPORT.png", dpi=150,
            facecolor=DARK, bbox_inches="tight")
plt.close()
print("✅ Final report saved as charts/BEATS_ANALYTICS_REPORT.png")