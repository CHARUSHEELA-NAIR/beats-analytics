# 🎧 Beats by Dre — Personal Project

A end-to-end data analytics project analyzing customer behavior, sales trends, and sentiment for Beats by Dre products.

## 📊 What This Project Covers
- **Data Preparation** — Created and cleaned a 500-row customer dataset
- **Quantitative Analysis** — Sales, revenue, and rating trends by product and region
- **Sentiment Analysis** — VADER-powered NLP analysis of 500 customer reviews
- **Data Visualization** — 10 charts + a full analytics dashboard

## 🛠️ Tools & Libraries
- Python, Pandas, Matplotlib, Seaborn
- VADER Sentiment Analysis
- WordCloud, OpenPyXL

## 📈 Key Findings
- Total Revenue: $98,795 across 500 transactions
- Average Rating: 3.90 / 5
- 64.8% of reviews were Positive
- Beats Studio Pro generated the highest revenue
- Middle East was the top-performing region

## 📁 Project Structure
beats-analytics/
├── create_dataset.py       # Generates synthetic dataset
├── data_cleaning.py        # Cleans and prepares data
├── quantitative_analysis.py # Sales & revenue charts
├── sentiment_analysis.py   # NLP sentiment analysis
├── generate_report.py      # Final dashboard report
├── beats_data.csv          # Raw dataset
├── beats_data_cleaned.csv  # Cleaned dataset
├── beats_data_final.csv    # Final dataset with sentiment
└── charts/                 # All generated visualizations
## 🚀 How to Run
```bash
pip install pandas matplotlib seaborn vaderSentiment wordcloud openpyxl
python create_dataset.py
python data_cleaning.py
python quantitative_analysis.py
python sentiment_analysis.py
python generate_report.py
```
