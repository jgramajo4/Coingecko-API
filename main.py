import json
import requests

response = requests.get('api.coingecko.com/api/v3/coins/list')
print(response)