# price-discrepancies-amms-cexs


# Arbitrage Bot in Python

## 📈 Overview

This project is a **cryptocurrency arbitrage bot** written in Python. The bot monitors price discrepancies across multiple exchanges and automatically executes profitable trades by buying low on one exchange and selling high on another. It uses real-time market data and API integration to facilitate arbitrage opportunities, leveraging the fast-moving nature of cryptocurrency markets.

## 🚀 Features

- **Multi-Exchange Support**: Monitors and trades across several exchanges (e.g., Binance, Kraken, Coinbase, etc.).
- **Real-Time Data**: Fetches price data and order books using exchange APIs.
- **Automated Trading**: Executes buy and sell orders when profitable arbitrage opportunities arise.
- **Customizable Strategy**: Users can adjust profit thresholds, risk parameters, and supported coins.
- **Logging & Alerts**: Detailed logging of trades and notifications for arbitrage opportunities.

## ⚙️ Requirements

- Python 3.8+
- `requests`, `ccxt`, `pandas`, and other dependencies listed in the `requirements.txt` file.

To install all dependencies, run:

```bash
pip install -r requirements.txt
```

## 📚 Setup
1. Clone the repository:
```bash
git clone https://github.com/yourusername/arbitrage-bot.git
cd arbitrage-bot
```
2. Create a .env file in the root directory with your API keys and configuration:

```bash
API_KEY_BINANCE=your_binance_api_key
API_SECRET_BINANCE=your_binance_api_secret
API_KEY_KRAKEN=your_kraken_api_key
API_SECRET_KRAKEN=your_kraken_api_secret
# Add other exchange API keys as necessary
```
3. Run the bot:
```bash
python main.py
```
## 📊 Configuration
The bot is highly customizable. You can modify parameters such as:
- **Supported exchanges**: Enable or disable exchanges in config.py.
- **Profit thresholds**: Adjust the minimum arbitrage profit percentage in config.py.
- **Risk management**: Set trade limits and stop-loss strategies.

## 🚨 Disclaimer
This bot is for educational purposes only. Cryptocurrency trading involves significant risk, and you should thoroughly test this bot with paper trading or simulations before using real funds.

## 🛠️ Contributing
Contributions are welcome! Please fork this repository and submit a pull request if you'd like to make improvements or add new features.

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.