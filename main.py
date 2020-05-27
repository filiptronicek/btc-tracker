import requests, json

btc_usd_req = json.loads(requests.get("https://blockchain.info/ticker").text)
usd_czk = (json.loads(requests.get("https://api.exchangeratesapi.io/latest?base=USD").text))


btc_usd_req = btc_usd_req['USD']['sell']
usd_czk = usd_czk['rates']['CZK']

CZK_BTC = btc_usd_req * usd_czk

