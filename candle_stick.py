import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mplfinance.original_flavor import candlestick_ohlc

# Define the time period
start = pd.Timestamp('2015-01-01')
end = pd.Timestamp('2020-09-07')

# Define the ticker
ticker = 'AAPL'

# Download the data
data = yf.download(ticker, start=start, end=end)

# Prepare the data for candlestick plotting
# Resample the full DataFrame to ensure we have OHLC columns
ohlc = data.resample('7D').agg({'Open': 'first',
                                'High': 'max',
                                'Low': 'min',
                                'Close': 'last'})

ohlc.reset_index(inplace=True)

# Ensure the 'Date' column is of type datetime64
ohlc['Date'] = pd.to_datetime(ohlc['Date'])

# Convert 'Date' to numerical format for plotting
ohlc['Date'] = ohlc['Date'].map(mdates.date2num)
volume = data['Volume'].resample('7D').sum()

# Set up the subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# Plot the candlestick chart with broader bars
candlestick_ohlc(ax1, ohlc[['Date', 'Open', 'High', 'Low', 'Close']].values, colorup='green', colordown='red', width=1)

# Plot the volume bars with thicker lines
ax2.bar(volume.index, volume, color='blue', width=3.0)

# Set labels
ax1.set_ylabel('OHLC')
ax2.set_ylabel('Volume')
ax2.set_xlabel('Date')

# Format dates on x-axis
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

# Rotate dates for better readability
plt.xticks(rotation=45)

# Adjust layout and display the plot
plt.tight_layout()
plt.show()
