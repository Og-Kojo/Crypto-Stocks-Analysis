import yfinance as yf
import pandas as pd
import time
from sqlalchemy import create_engine

# Top 20 stocks by market cap (as of 2025)
stock_mapping = {
    'apple': 'AAPL',
    'microsoft': 'MSFT',
    'alphabet': 'GOOGL',
    'amazon': 'AMZN',
    'nvidia': 'NVDA',
    'berkshire_hathaway': 'BRK-B',
    'meta': 'META',
    'tesla': 'TSLA',
    'eli_lilly': 'LLY',
    'jpmorgan': 'JPM',
    'johnson_and_johnson': 'JNJ',
    'visa': 'V',
    'exxon_mobil': 'XOM',
    'unitedhealth': 'UNH',
    'taiwan_semiconductor': 'TSM',
    'broadcom': 'AVGO',
    'walmart': 'WMT',
    'mastercard': 'MA',
    'procter_and_gamble': 'PG',
    'home_depot': 'HD'
}

# Define date range from 2020 to 2025
start_date = '2020-01-01'
end_date = '2025-12-31'

all_data = []

for stock_id, ticker in stock_mapping.items():
    try:
        df = yf.download(
            ticker,
            start=start_date,
            end=end_date,
            interval='1d',
            progress=False
        )

        df = df.reset_index()
        df['stock_id'] = stock_id
        df['ticker'] = ticker

        df = df[['stock_id', 'ticker', 'Date', 'Open', 'High', 'Low', 'Close', 'Volume']]

        all_data.append(df)

        print(f"Fetched data for {stock_id}")

        time.sleep(1.5)  # Pause to avoid rate limits
    except Exception as e:
        print(f"Error fetching {stock_id}: {e}")

# Combine all data
finals_df = pd.concat(all_data, ignore_index=True)



# Display sample data
print(final_df.head())

# SQL Connection parameters
server = 'localhost'
database = 'Crypto_DB'
username = 'SA'
password = 'Godkidpius.1s'
driver = 'ODBC Driver 17 for SQL Server'

# Connection string
conn_str = f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver.replace(' ', '+')}"
engine = create_engine(conn_str)

# Upload to SQL
finals_df.to_sql('Stocks_prices_history', con=engine, if_exists='replace', index=False)

print("Stock price data upload was successful")
