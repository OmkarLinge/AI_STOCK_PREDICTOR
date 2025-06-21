# utils/news_fetcher.py

import requests

def fetch_news(stock_name, api_key, max_articles=10):
    """
    Fetch recent news headlines and descriptions related to the stock name using NewsAPI.
    :param stock_name: Company name or keyword (e.g., 'Apple', 'Tata Motors')
    :param api_key: Your NewsAPI key
    :param max_articles: Max number of articles to fetch
    :return: List of articles with title, description, source, publishedAt, and URL
    """
    try:
        url = f"https://newsapi.org/v2/everything?q={stock_name}&sortBy=publishedAt&pageSize={max_articles}&apiKey={api_key}"
        response = requests.get(url)

        if response.status_code != 200:
            raise ValueError(f"NewsAPI Error: {response.status_code}")

        articles = response.json().get("articles", [])

        headlines = []
        for article in articles:
            headlines.append({
                "title": article.get("title", ""),
                "description": article.get("description", ""),  # ✅ NEW FIELD ADDED
                "source": article["source"]["name"],
                "publishedAt": article["publishedAt"],
                "url": article["url"]
            })

        return headlines

    except Exception as e:
        print(f"[Error] Could not fetch news for {stock_name}: {e}")
        return None
