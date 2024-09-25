import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

 
ticker = "SBIN.NS"
data = yf.download(ticker, period="1d", interval="1m")
 
plt.figure(figsize=(10, 6))
plt.plot(data.index, data['Close'], label="SBI Price", color='blue')

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
plt.gcf().autofmt_xdate()

 
plt.xlabel('Time')
plt.ylabel('Price (INR)')
plt.title('Real-Time Price of SBI')
plt.legend()

plt.show()
