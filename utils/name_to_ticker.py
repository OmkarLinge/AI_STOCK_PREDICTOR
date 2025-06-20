import requests

def get_ticker_from_name(stock_name):
    """
    Uses Yahoo Finance's search API to convert company name to ticker symbol.
    """
    try:
        url = f"https://query1.finance.yahoo.com/v1/finance/search?q={stock_name}"

        # Add headers to make the request look like it's from a browser
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
        }

        response = requests.get(url, headers=headers)
        data = response.json()

        if "quotes" in data and len(data["quotes"]) > 0:
            first_result = data["quotes"][0]
            symbol = first_result.get("symbol", None)
            longname = first_result.get("longname", None)
            exch = first_result.get("exchange", "")
            return symbol, longname, exch
        else:
            return None, None, None

    except Exception as e:
        print(f"[Error] Couldn't convert name to ticker: {e}")
        return None, None, None
