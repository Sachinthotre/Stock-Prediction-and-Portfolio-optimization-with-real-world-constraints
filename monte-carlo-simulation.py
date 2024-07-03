import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import cufflinks as cf
from datetime import datetime
import yfinance as yf

# Function to fetch stock data using Yahoo Finance
def fetch_stock_data(tickers, start_date, end_date):
    data = yf.download(tickers, start=start_date, end=end_date)['Adj Close']
    return data

# Function to calculate daily returns from stock data
def calculate_daily_returns(stock_data):
    daily_returns = stock_data.pct_change().dropna()
    return daily_returns

# Function to perform Monte Carlo simulation
def monte_carlo_simulation(stock_data, num_simulations, initial_investment):
    daily_returns = calculate_daily_returns(stock_data)
    n_assets = len(daily_returns.columns)
    
    # Placeholder arrays for results
    portfolio_values = np.zeros(num_simulations)
    
    # Simulate portfolio values for each simulation
    for i in range(num_simulations):
        weights = np.random.random(n_assets)
        weights /= np.sum(weights)  # Normalize weights to sum up to 1
        
        # Calculate portfolio value
        portfolio_value = initial_investment * (1 + np.dot(weights, daily_returns.mean()))
        portfolio_values[i] = portfolio_value
    
    return portfolio_values

# Define the tickers and date range
tickers = ['AMZN', 'JPM', 'META', 'PG', 'GOOG', 'CAT', 'PFE', 'EXC', 'DE', 'JNJ']
start_date = '2022-01-01'
end_date = '2024-01-01'

# Fetch stock data using Yahoo Finance
stock_data = fetch_stock_data(tickers, start_date, end_date)

# Perform Monte Carlo simulation
num_simulations = 1000
initial_investment = 1000000
simulation_results = monte_carlo_simulation(stock_data, num_simulations, initial_investment)

# Plot the results of the Monte Carlo simulation
plt.figure(figsize=(10, 6))
sns.histplot(simulation_results, bins=30, kde=True)
plt.title('Monte Carlo Simulation: Distribution of Portfolio Values')
plt.xlabel('Portfolio Value ($)')
plt.ylabel('Frequency')
plt.show()