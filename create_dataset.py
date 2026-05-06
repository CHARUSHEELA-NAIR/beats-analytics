import pandas as pd
import random
from datetime import datetime, timedelta

random.seed(42)

products = [
    "Beats Studio Pro", "Beats Fit Pro", "Powerbeats Pro",
    "Beats Solo 4", "Beats Studio Buds+", "Beats Flex"
]
prices = {
    "Beats Studio Pro": 349.99, "Beats Fit Pro": 199.99,
    "Powerbeats Pro": 249.99, "Beats Solo 4": 199.99,
    "Beats Studio Buds+": 169.99, "Beats Flex": 49.99
}
regions = ["North America", "Europe", "Asia Pacific", "Latin America", "Middle East"]
genders = ["Male", "Female", "Non-binary"]
age_groups = ["18-24", "25-34", "35-44", "45-54", "55+"]
purchase_channels = ["Online", "In-Store", "Apple Store", "Third-Party Retailer"]

positive_reviews = [
    "Absolutely love these headphones! The sound quality is incredible.",
    "Best purchase I've made this year. Bass is deep and clear.",
    "Premium feel and amazing noise cancellation. Worth every penny.",
    "Battery life is outstanding. Wore them all day with no issues.",
    "The fit is perfect and they're super comfortable for long sessions.",
    "Incredible sound stage. Music feels alive with these on.",
    "Fast charging is a game changer. 10 mins gave me 3 hours of playback.",
    "Seamless connection with my iPhone. Switching devices is effortless.",
]
neutral_reviews = [
    "Decent headphones for the price. Nothing groundbreaking but solid.",
    "Sound is good but I expected a bit more bass at this price point.",
    "Build quality feels okay. The case could be better designed.",
    "Good for everyday use. Not the best for professional audio work.",
    "Average noise cancellation. Works fine in mild environments.",
    "Comfortable enough but the ear cushions get warm after an hour.",
]
negative_reviews = [
    "Disappointed with the build quality. Feels cheap for the price.",
    "Noise cancellation is underwhelming compared to competitors.",
    "Had connectivity issues from day one. Very frustrating experience.",
    "Returned after a week. The bass is too overpowering for my taste.",
    "Customer support was unhelpful when I had a problem with my order.",
    "Battery drains faster than advertised. Expected better performance.",
]

rows = []
start_date = datetime(2023, 1, 1)

for i in range(500):
    product = random.choice(products)
    rating = random.choices([1, 2, 3, 4, 5], weights=[5, 8, 15, 35, 37])[0]

    if rating >= 4:
        review = random.choice(positive_reviews)
    elif rating == 3:
        review = random.choice(neutral_reviews)
    else:
        review = random.choice(negative_reviews)

    purchase_date = start_date + timedelta(days=random.randint(0, 730))

    rows.append({
        "customer_id": f"CUST{1000 + i}",
        "purchase_date": purchase_date.strftime("%Y-%m-%d"),
        "product": product,
        "price_usd": prices[product],
        "rating": rating,
        "age_group": random.choice(age_groups),
        "gender": random.choice(genders),
        "region": random.choice(regions),
        "purchase_channel": random.choice(purchase_channels),
        "review": review
    })

df = pd.DataFrame(rows)
df.to_csv("beats_data.csv", index=False)
print("✅ Dataset created! beats_data.csv is ready.")
print(df.head())