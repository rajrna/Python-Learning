import requests
import json
import sys

if len(sys.argv)!=2:
    sys.exit("Missing command-line argument")

try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=")
    # print(json.dumps(response.json(), indent= 2))
    o = response.json()
    # print(o)
    price = float(o['data']['priceUsd'])
    print(f"${price*n:,.4f}")

except ValueError:
    pass

