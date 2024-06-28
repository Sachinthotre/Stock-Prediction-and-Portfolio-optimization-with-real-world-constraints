'''
import yfinance as yf
import datetime as dt
import pandas as pd
import numpy as np
import matplotlib.ticker as mtick
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style
from mplfinance.original_flavor import candlestick_ohlc
style.use('ggplot')

tickers = ['AAPL','TSLA','AMZN','GS','C','BAC','MS','ATVI','EA','BTC-USD','ETH-USD']

start = dt.datetime(2019, 1, 1)
end = dt.datetime(2020, 11, 7)


returns = pd.DataFrame()

for ticker in tickers:
    data = yf.download(ticker, start=start, end=end)
    data = pd.DataFrame(data)
    data[ticker] = data['Adj Close'].pct_change()
    missing_data = data.isnull().sum()

    if returns.empty:
        returns = data[[ticker]]
    else: 
        returns = returns.join(data[[ticker]], how = 'outer')

returns = returns.dropna()
Correlation = returns.corr()

#print(Correlation.index)
#print(Correlation)

fig =plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_xticks(np.arrange(Correlation.shape[0] + 0.5,minor  = False))
ax.set_yticks(np.arrange(Correlation.shape[1] + 0.5,minor  = False))
heatmap  =ax.pcolor(Correlation, cmap = plt.cm.RdYlGn)
fig.colorbar(heatmap)

#row_labels = Correlation.index
#column_labels = Correlation.columns
ax.set_yticklabels(Correlation.index)
ax.set_yticklabels(Correlation.columns)
plt.show()

'''
import yfinance as yf
import datetime as dt
import pandas as pd
import numpy as np
import matplotlib.ticker as mtick
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style
from mplfinance.original_flavor import candlestick_ohlc
style.use('ggplot')

tickers = ['AAPL', 'TSLA', 'AMZN', 'GS', 'C', 'BAC', 'MS']

start = dt.datetime(2021, 1, 1)
end = dt.datetime(2022, 11, 7)

returns = pd.DataFrame()

for ticker in tickers:
    data = yf.download(ticker, start=start, end=end)
    data = pd.DataFrame(data)
    data[ticker] = data['Adj Close'].pct_change()
    missing_data = data.isnull().sum()
    
    if returns.empty:
        returns = data[[ticker]]
    else:
        returns = returns.join(data[[ticker]], how='outer')

returns = returns.dropna()
Correlation = returns.corr()

# Print correlation matrix (optional)
#print(Correlation.index)
#print(Correlation)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# Set ticks for the heatmap
ax.set_xticks(np.arange(Correlation.shape[0]) +0.5 , minor=False)
ax.set_yticks(np.arange(Correlation.shape[1]) +0.5, minor=False)
ax.invert_yaxis()
ax.xaxis.tick_top()
heatmap = ax.pcolor(Correlation, cmap=plt.cm.RdYlGn)
fig.colorbar(heatmap)
ax.set_xticklabels(Correlation.index)
ax.set_yticklabels(Correlation.columns)
plt.xticks(rotation = 90)
heatmap.set_clim(-1,1)

plt.show()

