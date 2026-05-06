import pandas as pd

# Load the dataset
df = pd.read_csv("beats_data.csv")

print("=== BEFORE CLEANING ===")
print(f"Shape: {df.shape}")
print(f"\nMissing values:\n{df.isnull().sum()}")
print(f"\nDuplicate rows: {df.duplicated().sum()}")

# Fix date column to proper datetime format
df["purchase_date"] = pd.to_datetime(df["purchase_date"])

# Add helper columns
df["year"] = df["purchase_date"].dt.year
df["month"] = df["purchase_date"].dt.month
df["month_name"] = df["purchase_date"].dt.strftime("%B")

# Standardize text columns
df["gender"] = df["gender"].str.strip().str.title()
df["region"] = df["region"].str.strip().str.title()
df["purchase_channel"] = df["purchase_channel"].str.strip().str.title()

# Add revenue column
df["revenue"] = df["price_usd"]

# Add rating label
def label_rating(r):
    if r >= 4:
        return "Positive"
    elif r == 3:
        return "Neutral"
    else:
        return "Negative"

df["rating_label"] = df["rating"].apply(label_rating)

print("\n=== AFTER CLEANING ===")
print(f"Shape: {df.shape}")
print(f"\nData types:\n{df.dtypes}")
print(f"\nRating distribution:\n{df['rating_label'].value_counts()}")

# Save cleaned dataset
df.to_csv("beats_data_cleaned.csv", index=False)
print("\n✅ Cleaned dataset saved as beats_data_cleaned.csv")