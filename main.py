import json
import requests

parameters = {
  "ids": 'bitcoin',
  "vs_currencies": 'usd',
  "include_24hr_change": 'true'
}

response = requests.get("https://api.coingecko.com/api/v3/simple/price", params=parameters)
print(response.json())