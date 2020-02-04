import requests
import hmac
import time
import threading
import calendar
import json
from rest_api import Account

if __name__ == "__main__":
    with open('config.json') as json_file:
        data = json.load(json_file)
    ac = Account(data["api_key"], data["secret"], data["leverage"])
    auth = ac.auth()
    while(True):
        tick = ac.ticker()
        result = tick["result"]
        resinner = result[0]
        bid = resinner["bid_price"]
        ask = resinner["ask_price"]
        symbol = resinner["symbol"]
        print(symbol + " Ask:"+ask + "  Bid:"+bid)
        time.sleep(1)