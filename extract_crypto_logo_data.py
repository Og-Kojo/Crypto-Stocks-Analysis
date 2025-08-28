import pandas as pd
from sqlalchemy import create_engine

# Coin Logo Data
data = [
    {"Name": "Bitcoin", "Symbol": "BTC", "Coin ID": "bitcoin", "Logo": "https://assets.coingecko.com/coins/images/1/large/bitcoin.png"},
    {"Name": "Ethereum", "Symbol": "ETH", "Coin ID": "ethereum", "Logo": "https://assets.coingecko.com/coins/images/279/large/ethereum.png"},
    {"Name": "Tether", "Symbol": "USDT", "Coin ID": "tether", "Logo": "https://assets.coingecko.com/coins/images/325/large/Tether-logo.png"},
    {"Name": "Binance Coin", "Symbol": "BNB", "Coin ID": "binancecoin", "Logo": "https://assets.coingecko.com/coins/images/825/large/binance-coin-logo.png"},
    {"Name": "Cardano", "Symbol": "ADA", "Coin ID": "cardano", "Logo": "https://assets.coingecko.com/coins/images/975/large/cardano.png"},
    {"Name": "Ripple", "Symbol": "XRP", "Coin ID": "ripple", "Logo": "https://assets.coingecko.com/coins/images/44/large/xrp-symbol-white-128.png"},
    {"Name": "Dogecoin", "Symbol": "DOGE", "Coin ID": "dogecoin", "Logo": "https://assets.coingecko.com/coins/images/5/large/dogecoin.png"},
    {"Name": "Solana", "Symbol": "SOL", "Coin ID": "solana", "Logo": "https://assets.coingecko.com/coins/images/4128/large/solana.png"},
    {"Name": "Polkadot", "Symbol": "DOT", "Coin ID": "polkadot", "Logo": "https://assets.coingecko.com/coins/images/12171/large/polkadot.png"},
    {"Name": "TRON", "Symbol": "TRX", "Coin ID": "tron", "Logo": "https://assets.coingecko.com/coins/images/1094/large/tron-logo.png"},
    {"Name": "Litecoin", "Symbol": "LTC", "Coin ID": "litecoin", "Logo": "https://assets.coingecko.com/coins/images/2/large/litecoin.png"},
    {"Name": "Chainlink", "Symbol": "LINK", "Coin ID": "chainlink", "Logo": "https://assets.coingecko.com/coins/images/877/large/chainlink-new-logo.png"},
    {"Name": "Polygon", "Symbol": "MATIC", "Coin ID": "polygon", "Logo": "https://assets.coingecko.com/coins/images/4713/large/polygon.png"},
    {"Name": "Avalanche", "Symbol": "AVAX", "Coin ID": "avalanche-2", "Logo": "https://assets.coingecko.com/coins/images/12559/large/coin-round-red.png"},
    {"Name": "Uniswap", "Symbol": "UNI", "Coin ID": "uniswap", "Logo": "https://assets.coingecko.com/coins/images/12504/large/uniswap-uni.png"},
    {"Name": "Stellar", "Symbol": "XLM", "Coin ID": "stellar", "Logo": "https://assets.coingecko.com/coins/images/100/large/stellar.png"},
    {"Name": "Cosmos", "Symbol": "ATOM", "Coin ID": "cosmos", "Logo": "https://assets.coingecko.com/coins/images/1481/large/cosmos_hub.png"},
    {"Name": "Monero", "Symbol": "XMR", "Coin ID": "monero", "Logo": "https://assets.coingecko.com/coins/images/69/large/monero_logo.png"},
    {"Name": "Bitcoin Cash", "Symbol": "BCH", "Coin ID": "bitcoin-cash", "Logo": "https://assets.coingecko.com/coins/images/780/large/bitcoin-cash-circle.png"},
    {"Name": "VeChain", "Symbol": "VET", "Coin ID": "vechain", "Logo": "https://assets.coingecko.com/coins/images/2075/large/Vechain_logo.png"}
]

df_logo = pd.DataFrame(data)

# Display DataFrame
print(df_logo)

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
df_logo.to_sql('coin_logo', con=engine, if_exists='replace', index=False)

print("Coin logo data upload was successful")
