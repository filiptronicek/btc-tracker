import requests, json
from datetime import datetime
import os
import time

key = os.environ.get("API_key")

if key is None:
    from key import api as key

btc_usd_req = json.loads(
    requests.get(
        "https://api.nomics.com/v1/currencies/ticker?key=" + key + "&ids=BTC"
    ).text
)
usd_czk = json.loads(
    requests.get("https://api.exchangeratesapi.io/latest?base=USD").text
)


btc_usd_req = btc_usd_req[0]["price"]
usd_czk = usd_czk["rates"]["CZK"]

print(btc_usd_req)

CZK_BTC = int(float(btc_usd_req)) * int(float(usd_czk))


now = datetime.now()

filename = "data/stats/" + now.strftime("%Y.%m") + ".csv"

if not os.path.isfile(filename) and not os.access(filename, os.R_OK):
    pf = open(filename, "w")
if os.stat(filename).st_size == 0:
    WriteData = open(filename, "a")
    WriteData.write("datetime, usd, czk")
    WriteData.close()

WriteData = open(filename, "a")
WriteData.write(
    "\n"
    + time.time()
    + ","
    + str(btc_usd_req)
    + ","
    + str((CZK_BTC))
)
WriteData.close()
