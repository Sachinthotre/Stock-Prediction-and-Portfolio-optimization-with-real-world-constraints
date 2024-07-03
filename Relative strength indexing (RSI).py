import yfinance as yf
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
from matplotlib import style

style.use('ggplot')

start = dt.datetime(2015, 1, 1)
end = dt.datetime(2020, 9, 7)

tickers = ['AAPL', 'KO', 'MSFT', 'TSLA', 'AMZN', 'BAC']
results = pd.DataFrame(columns=['ticker', 'RSI'])

for ticker in tickers:
    data = yf.download(ticker, start=start, end=end)

    # Calculate RSI
    data['abs_Change'] = data['Adj Close'].diff(1)
    data['up'] = np.where(data['abs_Change'] > 0, 1, 0)
    data['down'] = np.where(data['abs_Change'] < 0, 1, 0)

    data['positive_movement'] = data['up'] * data['abs_Change']
    data['negative_movement'] = data['down'] * data['abs_Change'] * -1
    data['avg_gain'] = data['positive_movement'].rolling(14).mean()
    data['avg_loss'] = data['negative_movement'].rolling(14).mean()

    data['RS'] = data['avg_gain'] / data['avg_loss']
    data['RSI'] = 100 - (100 / (1 + data['RS']))

    # Append latest RSI value to results DataFrame
    new_row = pd.DataFrame({'ticker': [ticker], 'RSI': [data['RSI'].iloc[-1]]})
    results = pd.concat([results, new_row], ignore_index=True)

    # Plotting
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

    # Plot Price
    ax1.plot(data.index, data['Adj Close'], label=ticker)
    ax1.set_ylabel('Price')
    ax1.legend()

    # Plot RSI
    ax2.plot(data.index, data['RSI'], label=ticker)
    ax2.axhline(70, color='r', linestyle='--')
    ax2.axhline(30, color='g', linestyle='--')
    ax2.set_ylabel('RSI')
    ax2.set_xlabel('Date')

    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    plt.tight_layout()
    plt.legend()
    plt.show()

# Display RSI results
print("RSI Results:")
print(results)
