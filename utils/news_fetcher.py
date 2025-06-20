# utils/news_fetcher.py

import requests

def fetch_news(stock_name, api_key, max_articles=10):
    """
    Fetch recent stock-related news headlines using NewsAPI (filtered by title).
    
    :param stock_name: Company name (e.g., 'Apple', 'Tata Steel')
    :param api_key: Your NewsAPI key
    :param max_articles: Max number of articles to fetch (default 10)
    :return: List of dictionaries with title, source, publish time, and URL
    """
    try:
        # Search only headlines with stock-related terms
        query = f"{stock_name} stock OR {stock_name} share OR {stock_name} market OR {stock_name} price"

        url = (
    f"https://newsapi.org/v2/everything?"
    f"qInTitle={stock_name} stock&"
    f"language=en&"
    f"sortBy=publishedAt&"
    f"pageSize={max_articles}&"
    f"apiKey={api_key}"
    )


        response = requests.get(url)

        if response.status_code != 200:
            raise ValueError(f"NewsAPI Error: {response.status_code} - {response.text}")

        articles = response.json().get("articles", [])

        headlines = []
        for article in articles:
            headlines.append({
                "title": article.get("title"),
                "url": article.get("url"),
                "source": article["source"]["name"],
                "publishedAt": article.get("publishedAt")
            })

        return headlines

    except Exception as e:
        print(f"[Error] Could not fetch news for '{stock_name}': {e}")
        return None
