import requests, json
from datetime import datetime
import os

btc_usd_req = json.loads(requests.get("https://blockchain.info/ticker").text)
usd_czk = json.loads(
    requests.get("https://api.exchangeratesapi.io/latest?base=USD").text
)

btc_usd_req = btc_usd_req["USD"]["sell"]
usd_czk = usd_czk["rates"]["CZK"]

CZK_BTC = btc_usd_req * usd_czk

now = datetime.now()

filename = "data/data.csv"

if not os.path.isfile(filename) and not os.access(filename, os.R_OK):
    pf = open(filename, "w")
if os.stat(filename).st_size == 0:
    WriteData = open(filename, "a")
    WriteData.write("datetime, usd, czk")
    WriteData.close()

WriteData = open(filename, "a")
WriteData.write(
    "\n" + now.strftime("%Y.%m.%d") + "," + str(btc_usd_req) + "," + str(int(CZK_BTC))
)
WriteData.close()
