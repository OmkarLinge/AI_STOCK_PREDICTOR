# test_news.py

from utils.news_fetcher import fetch_news

api_key = "9aff5e4fc1f0455baae0d83a639a3531"

stock_name = input("Enter company name (e.g., Tesla, Apple, Tata Steel): ")
max_articles = input("How many headlines do you want to fetch? (1–100): ")

try:
    max_articles = int(max_articles)
except:
    max_articles = 10  # fallback to 10

news = fetch_news(stock_name, api_key, max_articles)

if news:
    print(f"\n🗞️ Top {len(news)} stock-related headlines for {stock_name}:\n")
    for i, article in enumerate(news, 1):
        print(f"{i}. {article['title']} ({article['source']})")
        print(f"   Published: {article['publishedAt']}")
        print(f"   Link: {article['url']}\n")
else:
    print("⚠️ No news found or an error occurred.")

