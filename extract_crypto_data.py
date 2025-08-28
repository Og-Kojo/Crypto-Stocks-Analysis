pip install pandas
pip install yfinance pandas

import yfinance as yf
import pandas as pd
import time
from sqlalchemy import create_engine

# Top 20 cryptos mapped to Yahoo Finance tickers
coin_mapping = {
    'bitcoin': 'BTC-USD',
    'ethereum': 'ETH-USD',
    'tether': 'USDT-USD',
    'binancecoin': 'BNB-USD',
    'cardano': 'ADA-USD',
    'ripple': 'XRP-USD',
    'dogecoin': 'DOGE-USD',
    'solana': 'SOL-USD',
    'polkadot': 'DOT-USD',
    'tron': 'TRX-USD',
    'litecoin': 'LTC-USD',
    'chainlink': 'LINK-USD',
    'polygon': 'MATIC-USD',
    'avalanche': 'AVAX-USD',
    'uniswap': 'UNI-USD',
    'stellar': 'XLM-USD',
    'cosmos': 'ATOM-USD',
    'monero': 'XMR-USD',
    'bitcoin-cash': 'BCH-USD',
    'vechain': 'VET-USD'
}

# Date range
start_date = '2019-01-01'
end_date = '2025-08-03'

# List to collect data
all_data = []

for coin_id, ticker in coin_mapping.items():
    try:
        df = yf.download(
            ticker,
            start=start_date,
            end=end_date,
            interval='1d',
            progress=False
        )

        df = df.reset_index()
        df['coin_id'] = coin_id
        df['ticker'] = ticker

        df = df[['coin_id', 'ticker', 'Date', 'Open', 'High', 'Low', 'Close', 'Volume']]
        all_data.append(df)

        print(f"Fetched daily data for {coin_id}")
        time.sleep(1.5)  # Avoid hitting API rate limits

    except Exception as e:
        print(f"Error fetching {coin_id}: {e}")

# Combine all crypto data
final_df = pd.concat(all_data, ignore_index=True)



# SQL DB connection parameters
server = 'localhost'
database = 'Crypto_DB'
username = 'SA'
password = 'Godkidpius.1s'
driver = 'ODBC Driver 17 for SQL Server'

# Connection string for SQLAlchemy
conn_str = f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver.replace(' ', '+')}"
engine = create_engine(conn_str)

# Upload to SQL Server (replace table each run)
final_df.to_sql('prices_history', con=engine, if_exists='replace', index=False)
print("Crypto price data uploaded to SQL successfully")
