from fastapi import FastAPI, Query
import requests

app = FastAPI(title="MCP Crypto API", version="1.0")

@app.get("/")
def read_root():
    return {"message": "MCP Crypto API aktif."}

@app.get("/price")
def get_price(
    coin: str = Query("bitcoin", description="Fiyatı alınacak coin ismi"),
    currency: str = Query("usd", description="Karşılık birimi (örn: usd, eur, try)")
):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": coin, "vs_currencies": currency}
    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        price_data = response.json()
        if not price_data:
            return {"error": "Veri bulunamadı. Coin veya para birimi geçersiz olabilir."}
        return price_data
    except requests.exceptions.RequestException as e:
        return {"error": f"API hatası: {str(e)}"}
