import numpy as np

def calculate_rsi(closes, period=14):
    deltas = np.diff(closes)
    gain = np.maximum(deltas, 0)
    loss = -np.minimum(deltas, 0)

    avg_gain = np.mean(gain[-period:])
    avg_loss = np.mean(loss[-period:])

    rs = avg_gain / (avg_loss + 1e-10)
    return 100 - (100 / (1 + rs))

def generate_signal(data):
    closes = data["closes"]
    volumes = data["volumes"]

    rsi = calculate_rsi(closes)
    ma = np.mean(closes[-20:])
    price = closes[-1]

    volume_now = volumes[-1]
    volume_avg = np.mean(volumes)

    score = 0

    if rsi < 30: score += 30
    if rsi > 70: score += 30
    if volume_now > volume_avg * 1.5: score += 30
    if price < ma: score += 20
    if price > ma: score += 20

    if score >= 70:
        signal = "BUY" if price < ma else "SELL"
    else:
        signal = "WAIT"

    return {"signal": signal, "confidence": f"{score}%"}
