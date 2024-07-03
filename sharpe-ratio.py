import yfinance as yf
import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt

# Define the tickers of interest
tickers = ['AMZN', 'GOOGL', 'AAPL', 'MSFT']

# Fetch data from Yahoo Finance
stock_data = yf.download(tickers, start='2020-01-01', end='2023-01-01')['Adj Close']

# Calculate daily returns
daily_returns = stock_data.pct_change().dropna()

# Define the risk-free rate (example: 3% annualized)
rf_rate = 0.03

# Generate random portfolio weights
n_assets = len(tickers)
weights = np.random.random(n_assets)
weights /= np.sum(weights)  # Ensure weights sum up to 1

# Calculate portfolio returns
portfolio_returns = np.dot(daily_returns.mean(), weights) * 252

# Calculate portfolio volatility (standard deviation)
portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(daily_returns.cov() * 252, weights)))

# Calculate Sharpe ratio
sharpe_ratio = (portfolio_returns - rf_rate) / portfolio_volatility

# Plot historical stock prices
plt.figure(figsize=(14, 7))
for ticker in tickers:
    plt.plot(stock_data.index, stock_data[ticker], label=ticker)

plt.title('Historical Stock Prices')
plt.xlabel('Date')
plt.ylabel('Adj Close Price ($)')
plt.legend()
plt.grid(True)
plt.show()

# Plot cumulative portfolio value over time
initial_investment = 1000000
cumulative_returns = (daily_returns.dot(weights) + 1).cumprod() * initial_investment

plt.figure(figsize=(14, 7))
plt.plot(cumulative_returns.index, cumulative_returns, label='Portfolio Value')
plt.title('Cumulative Portfolio Value')
plt.xlabel('Date')
plt.ylabel('Portfolio Value ($)')
plt.legend()
plt.grid(True)
plt.show()

# Print results
print(f'Portfolio Returns: {portfolio_returns:.2%}')
print(f'Portfolio Volatility: {portfolio_volatility:.2%}')
print(f'Sharpe Ratio: {sharpe_ratio:.2f}')
