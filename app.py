from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "MCP Crypto API aktif."}

@app.get("/price")
def get_price(coin: str = "bitcoin", currency: str = "usd"):
    url = f"https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": coin, "vs_currencies": currency}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "API isteği başarısız"}
