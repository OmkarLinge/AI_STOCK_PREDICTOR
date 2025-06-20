# utils/stock_data_fetcher.py

import yfinance as yf
import pandas as pd

def fetch_stock_data(symbol, start_date="2015-01-01", end_date=None):
    """
    Fetch historical OHLCV data for any stock or forex symbol.
    :param symbol: Ticker symbol like AAPL, RELIANCE.NS, BTC-USD
    :param start_date: Date to start data from (format: YYYY-MM-DD)
    :param end_date: Date to end data (default: today)
    :return: DataFrame with Date, Open, High, Low, Close, Volume
    """
    try:
        ticker = yf.Ticker(symbol)
        data = ticker.history(start=start_date, end=end_date, auto_adjust=True)
        if data.empty:
            raise ValueError("No data found for this symbol.")
        return data
    except Exception as e:
        print(f"[Error] Could not fetch data for {symbol}: {e}")
        return None
