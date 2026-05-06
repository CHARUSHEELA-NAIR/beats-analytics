import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import os

os.makedirs("charts", exist_ok=True)

# Install vader if needed
try:
    from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
except ImportError:
    import subprocess
    subprocess.run(["pip", "install", "vaderSentiment"])
    from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

df = pd.read_csv("beats_data_cleaned.csv")
analyzer = SentimentIntensityAnalyzer()
BEATS_RED = "#E31837"

# --- Run Sentiment Analysis ---
def get_sentiment(text):
    score = analyzer.polarity_scores(str(text))
    compound = score["compound"]
    if compound >= 0.05:
        return "Positive", compound
    elif compound <= -0.05:
        return "Negative", compound
    else:
        return "Neutral", compound

df[["sentiment", "sentiment_score"]] = df["review"].apply(
    lambda x: pd.Series(get_sentiment(x))
)

print("=== SENTIMENT DISTRIBUTION ===")
print(df["sentiment"].value_counts())
print(f"\nAverage Sentiment Score: {df['sentiment_score'].mean():.3f}")

# --- Chart 7: Sentiment Distribution ---
plt.figure(figsize=(8, 6))
sentiment_counts = df["sentiment"].value_counts()
colors = [BEATS_RED if s == "Positive" else "#555555" if s == "Neutral" else "#222222"
          for s in sentiment_counts.index]
plt.bar(sentiment_counts.index, sentiment_counts.values, color=colors)
plt.title("Customer Sentiment Distribution", fontsize=16, fontweight="bold")
plt.xlabel("Sentiment")
plt.ylabel("Number of Reviews")
plt.tight_layout()
plt.savefig("charts/07_sentiment_distribution.png", dpi=150)
plt.close()
print("✅ Chart 7 saved")

# --- Chart 8: Sentiment by Product ---
plt.figure(figsize=(12, 6))
sentiment_product = df.groupby(["product", "sentiment"]).size().unstack(fill_value=0)
sentiment_product.plot(kind="bar", color=[BEATS_RED, "#222222", "#888888"],
                       figsize=(12, 6))
plt.title("Sentiment by Product", fontsize=16, fontweight="bold")
plt.xlabel("")
plt.ylabel("Number of Reviews")
plt.xticks(rotation=30, ha="right")
plt.legend(title="Sentiment")
plt.tight_layout()
plt.savefig("charts/08_sentiment_by_product.png", dpi=150)
plt.close()
print("✅ Chart 8 saved")

# --- Chart 9: Sentiment Score vs Rating ---
plt.figure(figsize=(8, 6))
avg_score = df.groupby("rating")["sentiment_score"].mean()
plt.plot(avg_score.index, avg_score.values, color=BEATS_RED,
         linewidth=2.5, marker="o", markersize=8)
plt.title("Sentiment Score vs Star Rating", fontsize=16, fontweight="bold")
plt.xlabel("Star Rating")
plt.ylabel("Average Sentiment Score")
plt.tight_layout()
plt.savefig("charts/09_sentiment_vs_rating.png", dpi=150)
plt.close()
print("✅ Chart 9 saved")

# --- Chart 10: Word Cloud ---
all_reviews = " ".join(df["review"].astype(str).tolist())
wordcloud = WordCloud(
    width=1200, height=600,
    background_color="black",
    colormap="Reds",
    max_words=100
).generate(all_reviews)

plt.figure(figsize=(14, 7))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Most Common Words in Reviews", fontsize=16, fontweight="bold", color="white",
          pad=20)
plt.tight_layout()
plt.savefig("charts/10_wordcloud.png", dpi=150, facecolor="black")
plt.close()
print("✅ Chart 10 saved")

# --- Save updated dataset ---
df.to_csv("beats_data_final.csv", index=False)
print("\n✅ Final dataset saved as beats_data_final.csv")
print("\n=== SENTIMENT BY PRODUCT ===")
print(df.groupby(["product", "sentiment"]).size().unstack(fill_value=0))