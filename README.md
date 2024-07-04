![Screenshot 2024-07-04 235511](https://github.com/Sachinthotre/Stock-Prediction-and-Portfolio-optimization-with-real-world-constraints/assets/46932228/fdf4b977-a805-4647-a74f-68fcf806fb5b)# Stock Prediction and Portfolio optimization with real-world constraints
 Develop a portfolio optimization model that not only finds the efficient frontier through mean-variance optimization but also integrates real-world constraints such as market impact, liquidity and tax considerations. Extend this project by incorporating alternative risk measures (beyond variance) into the optimization process, such as conditional value at risk(VAR) to address the portfolio's tail risk

This repository contains a comprehensive collection of scripts and functions designed for various aspects of stock analysis and portfolio optimization. The content is organized to guide you from basic analysis techniques to sophisticated portfolio management strategies.

---

### 1. **Candlestick Patterns**

   - **Description:** Identify and analyze various candlestick patterns used to predict future price movements in individual stocks.
   - **Code:** `candlestick_patterns.py`
   - [Screenshot 2024-07-04 232615](https://github.com/Sachinthotre/Stock-Prediction-and-Portfolio-optimization-with-real-world-constraints/assets/46932228/8f3c84cf-46c8-40c3-b5c5-946245dea8e6)


### 2. **Relative Strength Index (RSI)**

   - **Description:** Calculate and interpret the RSI to gauge the momentum and identify overbought or oversold conditions in stocks.
   - **Code:** `rsi_analysis.py`
   - [Screenshot 2024-07-04 233900](https://github.com/Sachinthotre/Stock-Prediction-and-Portfolio-optimization-with-real-world-constraints/assets/46932228/8bb8018f-583f-4eba-85f9-5a2a42a48611)


### 3. **Bollinger Bands**

   - **Description:** Use Bollinger Bands to assess volatility and potential price reversals by calculating moving averages and standard deviations.
   - **Code:** `bollinger_bands.py`
   - [Screenshot 2024-07-04 234726](https://github.com/Sachinthotre/Stock-Prediction-and-Portfolio-optimization-with-real-world-constraints/assets/46932228/1a69aa2d-d903-4b2b-bf27-4f310bdec154)


### 4. **Single Stock Analysis**

   - **Description:** Perform in-depth analysis of individual stocks, including trend analysis, moving averages, and basic technical indicators.
   - **Code:** `single_stock_analysis.py`
   - [Screenshot 2024-07-04 235154](https://github.com/Sachinthotre/Stock-Prediction-and-Portfolio-optimization-with-real-world-constraints/assets/46932228/be861bff-693f-4af1-8177-cae11464b217)


### 5. **Multiple Stock Analysis**

   - **Description:** Analyze and compare multiple stocks simultaneously to identify correlations, trends, and potential portfolio candidates.
   - **Code:** `multiple_stock_analysis.py`
   - [Uploading Screenshot 2024-07-04 235511.png…]()


### 6. **Correlation Analysis**

   - **Description:** Calculate and analyze the correlation between different stocks to understand relationships and diversify your portfolio.
   - **Code:** `correlation_analysis.py`
   - ![Correlation Analysis](screenshots/correlation_analysis.png)

### 7. **Event Analysis**

   - **Description:** Analyze the impact of specific events on stock prices and market trends to inform trading strategies.
   - **Code:** `event_analysis.py`
   - ![Event Analysis](screenshots/event_analysis.png)

### 8. **Sharpe Ratio Calculation**

   - **Description:** Evaluate the performance of investment portfolios by calculating the Sharpe ratio, which measures risk-adjusted returns.
   - **Code:** `sharpe_ratio.py`
   - ![Sharpe Ratio](screenshots/sharpe_ratio.png)

### 9. **Monte Carlo Simulations**

   - **Description:** Use Monte Carlo simulations to forecast the potential future performance of stocks and portfolios by modeling various scenarios.
   - **Code:** `monte_carlo_simulation.py`
   - ![Monte Carlo Simulation](screenshots/monte_carlo_simulation.png)

### 10. **Portfolio Optimization**

    - **Description:** Optimize your portfolio using various algorithms and techniques to maximize returns and minimize risk.
    - **Code:** `portfolio_optimization.py`
    - ![Portfolio Optimization](screenshots/portfolio_optimization.png)

---

### How to Use

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/stock-analysis-optimization.git
   ```
2. **Navigate to the Directory:**
   ```bash
   cd stock-analysis-optimization
   ```
3. **Run the Scripts:**
   Follow the instructions in each script's comments to understand its functionality and run it accordingly.

### Dependencies

Make sure to install the necessary Python libraries before running the scripts. You can find a list of required libraries in `requirements.txt`.

```bash
pip install -r requirements.txt
```

### License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---
