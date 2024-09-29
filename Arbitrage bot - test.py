import requests

class ArbitrageBot:
    def __init__(self, exchanges):
        self.exchanges = exchanges

    def fetch_prices(self):
        prices = {}
        for exchange in self.exchanges:
            try:
                response = requests.get(exchange['url'])
                response.raise_for_status()  # Raise an error for bad responses
                if exchange['name'] == 'Binance':
                    prices[exchange['name']] = response.json()['price']
                elif exchange['name'] == 'Coinbase':
                    prices[exchange['name']] = response.json()['data']['amount']
                print(f'Response from {exchange["name"]}: {response.json()}')  # Debugging line
            except requests.exceptions.RequestException as e:
                print(f'Error fetching price from {exchange["name"]}: {e}')
            except KeyError as e:
                print(f'KeyError: {e} for exchange {exchange["name"]}')
        return prices

    def find_arbitrage_opportunity(self, prices):
        max_price = max(prices.values())
        min_price = min(prices.values())
        if max_price > min_price:
            return max_price, min_price
        return None

    def execute_trade(self, buy_exchange, sell_exchange, amount):
        # Logic to execute trade on the exchanges
        pass

if __name__ == '__main__':
    exchanges = [
        {'name': 'Binance', 'url': 'https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT'},
        {'name': 'Coinbase', 'url': 'https://api.coinbase.com/v2/prices/spot?currency=USD'},
    ]
    bot = ArbitrageBot(exchanges)
    prices = bot.fetch_prices()
    opportunity = bot.find_arbitrage_opportunity(prices)
    if opportunity:
        print(f'Arbitrage opportunity found: Buy at {opportunity[1]} and sell at {opportunity[0]}')
    else:
        print('No arbitrage opportunity found.')