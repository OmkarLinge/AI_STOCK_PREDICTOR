# test_sentiment.py

from utils.news_fetcher import fetch_news
from utils.sentiment_analyzer import analyze_sentiment
from dotenv import load_dotenv
import os

# Load API key from .env file
load_dotenv()
api_key = os.getenv("NEWS_API_KEY")

# Ask user for input
stock_name = input("🔍 Enter a stock/company name (e.g., Tesla, Tata, Apple): ")

# Ask how many news articles to fetch
try:
    max_articles = int(input("📄 How many news articles to fetch (e.g., 3, 5, 10)? "))
except ValueError:
    max_articles = 5  # fallback
    print("⚠️ Invalid number. Defaulting to 5 articles.")

# Fetch news
news = fetch_news(stock_name, api_key, max_articles=max_articles)

if news:
    print(f"\n🧠 Analyzing latest {len(news)} news articles for '{stock_name}'...\n")

    for i, article in enumerate(news, 1):
        title = article.get("title", "")
        description = article.get("description", "")
        full_text = f"{title}. {description}" if description else title

        sentiment, confidence = analyze_sentiment(full_text)

        print(f"{i}. 📰 {title}")
        print(f"   📝 Description: {description}")
        print(f"   🧠 Sentiment: {sentiment} ({round(confidence * 100, 2)}% confidence)\n")
else:
    print("⚠️ No news found or error occurred.")
