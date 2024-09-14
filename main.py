import pandas as pd
import requests
from pycoingecko import CoinGeckoAPI

api_key = "CG-xQyHCHHRQX4JJshkZ9hYH1V2"
url = "https://api.coingecko.com/api/v3/simple/price"
params = {
    "ids": "ethereum",
    "vs_currencies": "USD"
}
# Replace 'YOUR_API_KEY' with your actual API key
headers = {'x-cg-demo-api-key': api_key}

response = requests.get(url, params=params)
print(response)

if response.status_code == 200:
    data = response.json()
    Ethereum_price = data["ethereum"]["usd"]
    print(f"The price of Ethereum in USD is ${Ethereum_price}")
else:
    print("Failed to retrieve data from the API")

cg = CoinGeckoAPI()
ohlc = cg.get_coin_ohlc_by_id(id="ethereum", vs_currency="usd", days="30")
print(ohlc)

df = pd.DataFrame(ohlc)
df.columns = ["date", "open", "high", "low", "close"]
df["date"] = pd.to_datetime(df["date"], unit="ms")
df.set_index("date", inplace=True)
