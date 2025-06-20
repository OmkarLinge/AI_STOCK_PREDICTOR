from utils.stock_data_fetcher import fetch_stock_data
from utils.name_to_ticker import get_ticker_from_name

# Ask for stock name (e.g., Apple)
stock_name = input("Enter company name (e.g., Apple, Reliance, Tesla): ")

# Convert name to ticker
symbol, fullname, exchange = get_ticker_from_name(stock_name)

if symbol:
    print(f"\n🔎 Found Ticker: {symbol} ({fullname}) on {exchange}")
    data = fetch_stock_data(symbol)
    if data is not None:
        print(f"\n📊 Showing latest 5 entries for {symbol}:\n")
        print(data.tail())
    else:
        print("⚠️ No data returned.")
else:
    print("❌ Could not find ticker for that name. Try a more exact name.")
