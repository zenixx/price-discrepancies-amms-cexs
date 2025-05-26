import time
import logging
import binance
from blinker._utilities import symbol
from kraken import kraken

# Initial fake balances for paper trading
binance_balance = 1000  # USDT
kraken_balance = 1000  # USDT
btc_balance_binance = 0  # BTC
btc_balance_kraken = 0  # BTC

# Set a logging file
logging.basicConfig(filename='paper_arbitrage_bot.log', level=logging.INFO)

# Start paper trading
while True:
    try:
        # Fetch price data
        binance_price = binance.fetch_ticker(symbol)['last']
        kraken_price = kraken.fetch_ticker(symbol)['last']

        # Example: Assume we want to trade 0.001 BTC
        trade_amount = 0.001

        # Simulate arbitrage: Buy on Kraken, Sell on Binance
        if binance_price > kraken_price:
            print(f"Paper trade: Buy on Kraken at {kraken_price}, sell on Binance at {binance_price}")

            # Simulate balance updates
            if kraken_balance >= kraken_price * trade_amount:
                kraken_balance -= kraken_price * trade_amount
                btc_balance_kraken += trade_amount
                binance_balance += binance_price * trade_amount
                btc_balance_binance -= trade_amount

                logging.info(
                    f"Simulated trade: Bought {trade_amount} BTC on Kraken, Sold {trade_amount} BTC on Binance.")
                logging.info(f"Kraken balance: {kraken_balance}, Binance balance: {binance_balance}")
            else:
                print("Not enough USDT on Kraken for this trade.")

        # Simulate arbitrage: Buy on Binance, Sell on Kraken
        elif kraken_price > binance_price:
            print(f"Paper trade: Buy on Binance at {binance_price}, sell on Kraken at {kraken_price}")

            # Simulate balance updates
            if binance_balance >= binance_price * trade_amount:
                binance_balance -= binance_price * trade_amount
                btc_balance_binance += trade_amount
                kraken_balance += kraken_price * trade_amount
                btc_balance_kraken -= trade_amount

                logging.info(
                    f"Simulated trade: Bought {trade_amount} BTC on Binance, Sold {trade_amount} BTC on Kraken.")
                logging.info(f"Binance balance: {binance_balance}, Kraken balance: {kraken_balance}")
            else:
                print("Not enough USDT on Binance for this trade.")

        # Wait before checking again
        time.sleep(5)

    except Exception as e:
        print(f"Error: {e}")
        time.sleep(5)
