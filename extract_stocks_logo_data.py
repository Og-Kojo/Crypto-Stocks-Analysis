import yfinance as yf
import pandas as pd
from sqlalchemy import create_engine

# Stock Logo Data
stock_data = [
    {"Name": "Apple", "Symbol": "AAPL", "Logo": "https://logo.clearbit.com/apple.com"},
    {"Name": "Microsoft", "Symbol": "MSFT", "Logo": "https://logo.clearbit.com/microsoft.com"},
    {"Name": "Alphabet", "Symbol": "GOOGL", "Logo": "https://logo.clearbit.com/abc.xyz"},
    {"Name": "Amazon", "Symbol": "AMZN", "Logo": "https://logo.clearbit.com/amazon.com"},
    {"Name": "Nvidia", "Symbol": "NVDA", "Logo": "https://logo.clearbit.com/nvidia.com"},
    {"Name": "Berkshire Hathaway", "Symbol": "BRK-B", "Logo": "https://logo.clearbit.com/berkshirehathaway.com"},
    {"Name": "Meta", "Symbol": "META", "Logo": "https://logo.clearbit.com/meta.com"},
    {"Name": "Tesla", "Symbol": "TSLA", "Logo": "https://logo.clearbit.com/tesla.com"},
    {"Name": "Eli Lilly", "Symbol": "LLY", "Logo": "https://logo.clearbit.com/lilly.com"},
    {"Name": "JPMorgan Chase", "Symbol": "JPM", "Logo": "https://logo.clearbit.com/jpmorganchase.com"},
    {"Name": "Johnson & Johnson", "Symbol": "JNJ", "Logo": "https://logo.clearbit.com/jnj.com"},
    {"Name": "Visa", "Symbol": "V", "Logo": "https://logo.clearbit.com/visa.com"},
    {"Name": "Exxon Mobil", "Symbol": "XOM", "Logo": "https://logo.clearbit.com/exxonmobil.com"},
    {"Name": "UnitedHealth", "Symbol": "UNH", "Logo": "https://logo.clearbit.com/unitedhealthgroup.com"},
    {"Name": "Taiwan Semiconductor", "Symbol": "TSM", "Logo": "https://logo.clearbit.com/tsmc.com"},
    {"Name": "Broadcom", "Symbol": "AVGO", "Logo": "https://logo.clearbit.com/broadcom.com"},
    {"Name": "Walmart", "Symbol": "WMT", "Logo": "https://logo.clearbit.com/walmart.com"},
    {"Name": "Mastercard", "Symbol": "MA", "Logo": "https://logo.clearbit.com/mastercard.com"},
    {"Name": "Procter & Gamble", "Symbol": "PG", "Logo": "https://logo.clearbit.com/pg.com"},
    {"Name": "Home Depot", "Symbol": "HD", "Logo": "https://logo.clearbit.com/homedepot.com"},
]

# Convert to DataFrame
df_stock = pd.DataFrame(stock_data)

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
df_stock.to_sql('stock_logo', con=engine, if_exists='replace', index=False)

print("Stock logo data upload was successful")
