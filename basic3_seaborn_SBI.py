import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns

sns.set(style="darkgrid")


ticker = "SBIN.NS"
data = yf.download(ticker, period="1d", interval="1m")


plt.figure(figsize=(12, 8))


plt.plot(data.index, data['Close'], label="SBI Price", color='darkblue', linewidth=2)


plt.scatter(data.index[-1], data['Close'][-1], color='red')
plt.text(data.index[-1], data['Close'][-1], f' {data["Close"][-1]:.2f}', color='red', fontsize=12)


plt.grid(True, linestyle='--', alpha=0.6)


plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
plt.gcf().autofmt_xdate()


plt.xlabel('Time', fontsize=14, color='black')
plt.ylabel('Price (INR)', fontsize=14, color='black')
plt.title('Real-Time Price of SBI', fontsize=16, color='black', weight='bold')


plt.legend(fontsize=12, loc='upper left')

plt.tight_layout()
plt.show()
