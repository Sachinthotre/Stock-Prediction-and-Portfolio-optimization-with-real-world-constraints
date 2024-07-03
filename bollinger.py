import yfinance as yf
import datetime as dt
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
from matplotlib import style

#style.use('ggplot')

# Define the time period
start = dt.datetime(2015, 1, 1)
end = dt.datetime(2020, 9, 7)

# Define tickers
tickers = ['AAPL', 'KO', 'MSFT', 'TSLA', 'AMZN', 'BAC']

# Initialize results DataFrame
results = pd.DataFrame(columns=['Ticker', 'Ratio'])

# Loop through each ticker and calculate the required metrics
for ticker in tickers:
    data = yf.download(ticker, start=start, end=end)

    # Drop unnecessary columns
    data = data.drop(columns=['High', 'Low', 'Open', 'Close'])

    # Calculate the 20-day moving average and standard deviation
    data['20_MA'] = data['Adj Close'].rolling(20).mean()
    data['20_std'] = data['Adj Close'].rolling(20).std()

    # Calculate the Bollinger Bands
    data['Upper_band'] = data['20_MA'] + 2 * data['20_std']
    data['lower_band'] = data['20_MA'] - 2 * data['20_std']

    # Calculate the Ratio of standard deviation to moving average
    data['Ratio'] = data['20_std'] / data['20_MA'] * 100

    # Handle NaN values
    data = data.dropna()

    # Append the latest ratio to the results DataFrame
    if not data.empty:
        last_ratio = data['Ratio'].iloc[-1]
        new_row = pd.DataFrame({'Ticker': [ticker], 'Ratio': [last_ratio]})
        results = pd.concat([results, new_row], ignore_index=True)

# Print the results
print(results)


ax1 = plt.subplot2grid((1,1), (0,0), rowspan = 1, colspan =1, title = ticker)
ax2 = plt.subplot2grid((8,1), (5,0), rowspan=3, colspan=1, sharex = ax1)


ax1.plot(data['Adj Close'], label = 'Price')
ax1.plot(data['Upper_band'],label = 'Upper Band', color = 'green' )
ax1.plot(data['lower_band'],label = 'lower Band', color = 'black' )

ax2.plot(data['Ratio'], label='Ratio', color = 'orange')

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
ax1.set_xlabel('Date (Year-month)')
ax2.set_xlabel('Date (Year-month)')

ax2.legend()
ax1.legend()
plt.show()












