import requests

def get_market_data():
    url = "https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=5m&limit=50"
    data = requests.get(url).json()

    closes = [float(x[4]) for x in data]
    volumes = [float(x[5]) for x in data]

    return {"closes": closes, "volumes": volumes}
