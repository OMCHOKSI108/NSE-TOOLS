import yfinance as yf

ticker = "SBIN.NS"  
data = yf.download(ticker, period="1d", interval="1m")

if not data.empty:
    print("Data fetched successfully!")
    print(data.head())
else:
    print("No data found for this ticker.")
