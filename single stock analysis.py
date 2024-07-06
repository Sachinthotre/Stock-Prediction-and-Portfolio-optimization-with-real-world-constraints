import yfinance as yf
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style
import numpy as np

# Set the plot style
style.use('ggplot')

# Define the start and end dates
start = dt.datetime(2015, 1, 1)
end = dt.datetime(2020, 9, 7)

# Define the ticker symbol
ticker = 'AAPL'

# Download stock data
data = yf.download(ticker, start=start, end=end)

# Ensure that dropped columns are correct and necessary
data = data.drop(columns=['High', 'Low', 'Open', 'Close'])

# Calculate the 20-day and 120-day Simple Moving Averages
data['SMA20'] = data['Adj Close'].rolling(window=20).mean()
data['SMA120'] = data['Adj Close'].rolling(window=120).mean()

# Calculate the previous day's price
data['Price_yesterday'] = data['Adj Close'].shift(1)

# Calculate daily changes
data['Change'] = data['Adj Close'] / data['Price_yesterday']

# Drop NaN values resulting from moving average calculations
data.dropna(inplace=True)

# Determine if invested based on SMA20 > SMA120
data['Invested_SMA'] = data['SMA20'] > data['SMA120']

# Calculate cumulative returns for buy and hold
data['Buy_and_hold'] = np.cumprod(data['Change'])

# Calculate returns for SMA strategy
sma = data[data['Invested_SMA']]
sma['Return'] = np.cumprod(sma['Change'])

# Create subplots
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(14, 14), gridspec_kw={'height_ratios': [2, 1, 1]})

# Plot Adjusted Close Price and SMAs on the first subplot
ax1.plot(data.index, data['Adj Close'], label='Adjusted Close Price', color='blue', alpha=0.5)
ax1.plot(data.index, data['SMA20'], label='20-Day SMA', color='orange', linewidth=2)
ax1.plot(data.index, data['SMA120'], label='120-Day SMA', color='green', linewidth=2)

# Set title and labels
ax1.set_title('Apple Stock Prices (2015-2020)')
ax1.set_ylabel('Price (USD)')
ax1.legend()

# Plot Volume on the second subplot
ax2.bar(data.index, data['Volume'], label='Volume', color='grey', alpha=0.3)

# Set x-axis labels and format
ax2.set_xlabel('Date (Year-Month)')
ax2.set_ylabel('Volume')
ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
ax2.legend()

# Plot cumulative returns on the third subplot
ax3.plot(data.index, data['Buy_and_hold'], label='Buy and Hold', color='purple')
ax3.plot(sma.index, sma['Return'], label='SMA Strategy', color='red')

# Set x-axis labels and format for the third subplot
ax3.set_xlabel('Date (Year-Month)')
ax3.set_ylabel('Cumulative Return')
ax3.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
ax3.legend()

# Rotate x-axis labels for better readability
plt.setp(ax2.xaxis.get_majorticklabels(), rotation=45)
plt.setp(ax3.xaxis.get_majorticklabels(), rotation=45)

# Show plot
plt.tight_layout()
plt.show()

# Save the plot as an image (optional)
# plt.savefig('Apple_2015_to_2020.png')
# The plt picture is attached in the Readme file.
