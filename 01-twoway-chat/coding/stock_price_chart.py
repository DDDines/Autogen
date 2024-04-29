# filename: stock_price_chart.py
import yfinance as yf
import matplotlib.pyplot as plt

# Function to fetch stock price data and plot the chart
def plot_stock_price(symbol, name):
    stock_data = yf.download(symbol, start='2022-01-01', end='2022-12-31')
    stock_data['Close'].plot(label=name)
    
# Fetch stock price data for META and TWITTER
plot_stock_price('META', 'META')
plot_stock_price('TWTR', 'TWITTER')

# Plotting settings
plt.title('Stock Price Change of META and TWITTER in 2022')
plt.xlabel('Date')
plt.ylabel('Stock Price (USD)')
plt.legend()
plt.grid()
plt.show()