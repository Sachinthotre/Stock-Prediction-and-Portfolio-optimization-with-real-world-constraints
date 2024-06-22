import yfinance as yf
from datetime import datetime
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style
from mplfinance.original_flavor import candlestick_ohlc

# style.use('ggplot')

# Define the time period
start = datetime(2015, 1, 1)
end = datetime(2020, 9, 7)

# Define the ticker
ticker = ['BAC']

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
ax1 = plt.subplot2grid((8, 1), (0, 0), rowspan=3, colspan=1)
ax2 = plt.subplot2grid((6, 1), (4, 0), rowspan=2, colspan=1, sharex=ax1)

# Plot the candlestick chart
candlestick_ohlc(ax1, ohlc[['Date', 'Open', 'High', 'Low', 'Close']].values, colorup='green', colordown='pink')

# Plot the volume
ax2.bar(volume.index, volume, color='blue')

# Set labels
ax1.set_ylabel('OHLC')
ax2.set_ylabel('Volume')
ax2.set_xlabel('Date')

# Adjust layout and display the plot
plt.tight_layout()




