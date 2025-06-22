from utils.news_fetcher import fetch_news
from utils.sentiment_analyzer import analyze_sentiment

def build_sentiment_report(stock_name, api_key, max_articles=5):
    """
    Build sentiment report for a stock using latest news.
    """
    articles = fetch_news(stock_name, api_key, max_articles)
    report = []

    if not articles:
        return None

    for article in articles:
        title = article.get("title", "")
        description = article.get("description", "")
        full_text = f"{title}. {description}" if description else title

        sentiment, confidence = analyze_sentiment(full_text)

        report.append({
            "title": title,
            "description": description,
            "source": article.get("source", "Unknown"),
            "publishedAt": article.get("publishedAt", ""),
            "url": article.get("url", ""),
            "sentiment": sentiment,
            "confidence": round(confidence * 100, 2)
        })

    return report
