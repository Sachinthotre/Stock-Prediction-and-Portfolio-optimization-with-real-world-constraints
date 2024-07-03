
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


indexes= ['^GSPC','^FCHI','^IBEX','^GDAXI','000001.SS','^N225']

dictionary = {'^GSPC':'US', '^FCHI':"France", '^IBEX':"Spain", '^GDAXI':'Germany', '000001.SS':'China', '^N225':'Japan'}

start = dt.datetime(2007, 8, 1)
end = dt.datetime(2009, 12, 31)

#ticker = ['BAC']

# Download the data

total_returns = pd.DataFrame()

for index in indexes:
    data = yf.download(index, start=start, end=end)
    data = pd.DataFrame(data)
    data['pct'] = data['Adj Close'].pct_change()
    data[index] = (data['pct']+1).cumprod() *100

    if total_returns.empty:
        total_returns = data[[index]]
    else:
        total_returns  = total_returns.join(data[[index]], how = 'outer')


total_returns = total_returns.dropna()


ax1 = plt.subplot2grid((1,1), (0,0), rowspan=1, colspan=1, title = 'Fin shit')

for index in indexes:
    ax1.plot(total_returns[index], label = dictionary[index])

ax1.yaxis.set_major_formatter(mtick.PercentFormatter())

plt.legend()
plt.show()


    
