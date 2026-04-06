import requests

def get_whale_activity():
    try:
        url = "https://api.dexscreener.com/latest/dex/pairs/solana"
        data = requests.get(url).json()

        pair = data["pairs"][0]
        volume = float(pair["volume"]["h24"])

        if volume > 1000000:
            return {"type": "ACCUMULATION", "amount": volume}

        return {"type": "NORMAL", "amount": volume}

    except:
        return {"type": "ERROR", "amount": 0}
