import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Fetch stock data function
def fetch_stock_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    data = pd.DataFrame(data)
    data[ticker] = data['Adj Close'].pct_change()
    return data[[ticker]].dropna()

# Portfolio optimization functions
def portfolio_statistics(weights, returns):
    weights = np.array(weights)
    portfolio_return = np.sum(returns.mean() * weights) * 252
    portfolio_stddev = np.sqrt(np.dot(weights.T, np.dot(returns.cov() * 252, weights)))
    return np.array([portfolio_return, portfolio_stddev, portfolio_return / portfolio_stddev])

def min_func_sharpe(weights, returns):
    return -portfolio_statistics(weights, returns)[2]

def optimize_portfolio(returns):
    num_assets = len(returns.columns)
    args = (returns,)
    constraints = ({'type': 'eq', 'fun': lambda x: np.sum(np.abs(x)) - 1})
    result = minimize(min_func_sharpe, num_assets * [1. / num_assets,], args=args, method='SLSQP', constraints=constraints)
    return result

# Define tickers and dates
tickers = ['META', 'JPM']
start_date = '2014-01-01'
end_date = '2020-11-20'

# Fetch stock data for each ticker
returns = pd.DataFrame()
for ticker in tickers:
    data = fetch_stock_data(ticker, start_date, end_date)
    if returns.empty:
        returns = data
    else:
        returns = returns.join(data, how='outer')

# Optimize portfolio
opt_result = optimize_portfolio(returns)
opt_weights = opt_result.x

# Print the optimized portfolio weights and statistics
print("Optimized portfolio weights:")
print(opt_weights)
print("Expected annual return, volatility, and Sharpe ratio:")
print(portfolio_statistics(opt_weights, returns))

# Generate random portfolios using Monte Carlo simulation for illustration
def generate_random_portfolios(num_portfolios, returns):
    results = np.zeros((3, num_portfolios))
    weights_record = []
    num_assets = len(returns.columns)
    for i in range(num_portfolios):
        weights = np.random.random(num_assets)
        weights /= np.sum(weights)
        portfolio_return, portfolio_stddev, sharpe_ratio = portfolio_statistics(weights, returns)
        results[0,i] = portfolio_return
        results[1,i] = portfolio_stddev
        results[2,i] = sharpe_ratio
    return results

# Perform Monte Carlo simulation for illustration purposes
num_portfolios = 1000
results = generate_random_portfolios(num_portfolios, returns)

# Find and print lowest risk portfolio
min_risk_idx = np.argmin(results[1])
print("\nLowest risk portfolio:")
print("Return:", results[0, min_risk_idx])
print("Volatility:", results[1, min_risk_idx])
print("Sharpe Ratio:", results[2, min_risk_idx])

# Find and print highest return portfolio
max_return_idx = np.argmax(results[0])
print("\nHighest return portfolio:")
print("Return:", results[0, max_return_idx])
print("Volatility:", results[1, max_return_idx])
print("Sharpe Ratio:", results[2, max_return_idx])

# Find and print highest Sharpe ratio portfolio
max_sharpe_idx = np.argmax(results[2])
print("\nHighest Sharpe ratio portfolio:")
print("Return:", results[0, max_sharpe_idx])
print("Volatility:", results[1, max_sharpe_idx])
print("Sharpe Ratio:", results[2, max_sharpe_idx])

# Plot the results
plt.figure(figsize=(10, 6))

# Scatter plot for Monte Carlo simulated portfolios
plt.scatter(results[1,:], results[0,:], c=results[2,:], cmap='viridis', label='Monte Carlo Portfolios')
plt.colorbar(label='Sharpe Ratio')

# Scatter plot for specific portfolios
plt.scatter(results[1, min_risk_idx], results[0, min_risk_idx], c='yellow', marker='o', s=200,edgecolors='black', label='Lowest Risk')
plt.scatter(results[1, max_return_idx], results[0, max_return_idx], c='green', marker='o', s=200, edgecolors='black', label='Highest Return')
plt.scatter(results[1, max_sharpe_idx], results[0, max_sharpe_idx], c='red', marker='o', s=250, edgecolors='black', label='Highest Sharpe Ratio')

# Yellow dot for optimized portfolio
plt.scatter(portfolio_statistics(opt_weights, returns)[1], 
            portfolio_statistics(opt_weights, returns)[0], 
            c='blue', s=100, edgecolors='black', label='Optimized Portfolio')

plt.title('Portfolio Optimization Curve')
plt.xlabel('Volatility')
plt.ylabel('Return')
plt.legend()
plt.grid(True)
plt.show()

# plt picture is attached in the Readme file
