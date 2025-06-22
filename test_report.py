from utils.news_sentiment_report import build_sentiment_report
from collections import Counter
import json

# Replace this with your NewsAPI key (we'll .env later)
api_key = "9aff5e4fc1f0455baae0d83a639a3531"

# Get user input
stock = input("🔍 Enter stock/company name: ")
count = input("🔢 How many articles to analyze? (e.g., 3, 5, 10): ")

try:
    count = int(count)
except:
    count = 5

# Generate report
report = build_sentiment_report(stock, api_key, max_articles=count)

if report:
    print(f"\n📊 Sentiment Report for '{stock}' (Top {count} Articles):\n")
    sentiments = []

    for i, item in enumerate(report, 1):
        sentiments.append(item['sentiment'])

        print(f"{i}. 📰 {item['title']}")
        print(f"   📝 Description: {item['description']}")
        print(f"   🧠 Sentiment: {item['sentiment']} ({item['confidence']}%)")
        print(f"   📰 Source: {item['source']}")
        print(f"   📅 Published At: {item['publishedAt']}")
        print(f"   🔗 URL: {item['url']}\n")

    # 🧠 Sentiment Summary
    print("🧠 Overall Sentiment Summary:")
    total = len(sentiments)
    counts = Counter(sentiments)

    for label in ['Positive', 'Neutral', 'Negative']:
        percent = (counts[label] / total) * 100 if label in counts else 0
        print(f"   {label}: {percent:.1f}%")

    # 💾 Save to JSON (optional)
    filename = f"sentiment_report_{stock.lower().replace(' ', '_')}.json"
    with open(filename, "w") as f:
        json.dump(report, f, indent=2)

    print(f"\n💾 Report saved as: {filename}")

else:
    print("⚠️ No news found or failed to fetch.")
