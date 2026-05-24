import requests

url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

response = requests.get(url)

data = response.json()

print("Bitcoin Price in USD:")
print(data["bitcoin"]["usd"])


