from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/signal")
def signal():
    signals = ["BUY", "SELL", "WAIT"]
    return {
        "signal": random.choice(signals),
        "confidence": random.choice(["HIGH", "LOW"])
    }

@app.get("/execute")
def execute():
    print("Executing trade via OpenClaw...")
    return {"status": "success"}
