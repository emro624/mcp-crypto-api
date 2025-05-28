import requests

url = "http://127.0.0.1:8000/price?coin=bitcoin&currency=usd"
response = requests.get(url)

print(response.json())
