import yfinance as yf
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
from matplotlib import style

style.use('ggplot')

# Define the start and end dates
start = dt.datetime(2015, 1, 1)
end = dt.datetime(2020, 9, 7)

# Define the ticker symbols
tickers = ['AAPL', 'KO', 'MSFT', 'TSLA', 'AMZN']

# Iterate over each ticker symbol
for ticker in tickers:
    # Download stock data
    data = yf.download(ticker, start=start, end=end)
    
    # Calculate Simple Moving Averages (SMA)
    data['SMA20'] = data['Adj Close'].rolling(20).mean()
    data['SMA120'] = data['Adj Close'].rolling(120).mean()
    
    # Calculate Exponential Moving Averages (EWM)
    data['EWM12'] = data['Adj Close'].ewm(span=12, adjust=False).mean()
    data['EWM26'] = data['Adj Close'].ewm(span=26, adjust=False).mean()
    
    # Calculate the daily price change ratio
    data['Change'] = data['Adj Close'] / data['Adj Close'].shift(1)
    data['Change'].fillna(1, inplace=True)
    
    # Determine the investment strategy based on SMA and EWM crossovers
    data['Invested_SMA'] = np.where(data['SMA20'] > data['SMA120'], 1, 0)
    data['Invested_EWM'] = np.where(data['EWM12'] > data['EWM26'], 1, 0)
    
    # Calculate the cumulative return for buy-and-hold strategy
    data['Buy_and_hold'] = np.cumprod(data['Change'])
    
    # Calculate the cumulative return for SMA and EWM strategies
    sma_invested = data[data['Invested_SMA'] == 1]
    sma_invested['Return'] = np.cumprod(sma_invested['Change'])
    
    ewm_invested = data[data['Invested_EWM'] == 1]
    ewm_invested['Return'] = np.cumprod(ewm_invested['Change'])
    
    print(f'Ticker: {ticker}')
    print('Buy and hold strategy return:', data['Buy_and_hold'].iloc[-1])
    print('SMA return:', sma_invested['Return'].iloc[-1] if not sma_invested.empty else "No SMA strategy applied")
    print('EWM return:', ewm_invested['Return'].iloc[-1] if not ewm_invested.empty else "No EWM strategy applied")
    
    '''
    # Uncomment the following lines if you want to visualize the data
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(14, 10), gridspec_kw={'height_ratios': [4, 3, 2]}, sharex=True)

    # Plot Adjusted Close Price and SMAs on the first subplot
    ax1.plot(data.index, data['Adj Close'], label='Adjusted Close Price', color='blue', alpha=0.5)
    ax1.plot(data.index, data['SMA20'], label='20-Day SMA', color='orange', linewidth=2)
    ax1.plot(data.index, data['SMA120'], label='120-Day SMA', color='green', linewidth=2)
    ax1.plot(data.index, data['EWM12'], label='EWM 12', color='Purple', linewidth=2)
    ax1.plot(data.index, data['EWM26'], label='EWM 26', color='Pink', linewidth=2)
    ax1.set_title(f'{ticker} Stock Prices (2015-2020)')
    ax1.set_ylabel('Price (USD)')
    ax1.legend()

    # Plot Volume on the second subplot
    ax2.bar(data.index, data['Volume'], label='Volume', color='grey', alpha=0.3)
    ax2.set_ylabel('Volume')
    ax2.legend()

    # Plot strategy performance on the third subplot
    ax3.plot(data.index, data['Buy_and_hold'], label='Buy and Hold', color='blue')
    ax3.plot(sma_invested.index, sma_invested['Return'], label='SMA20 > SMA120', color='orange')
    ax3.plot(ewm_invested.index, ewm_invested['Return'], label='EWM12 > EWM26', color='green')
    ax3.set_xlabel('Date (Year-Month)')
    ax3.set_ylabel('Cumulative Return')
    ax3.legend()

    # Set x-axis date format
    ax3.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

    # Rotate x-axis labels for better readability
    plt.setp(ax3.xaxis.get_majorticklabels(), rotation=45)

    # Adjust layout for better fit
    plt.tight_layout()

    # Show plot
    plt.show()

    # Save the plot as an image (optional)
    # plt.savefig(f'{ticker}_2015_to_2020.png')
    '''
