from email import header
from urllib import request, response
from wsgiref import headers
import requests
import pandas as pd

url = 'https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY'
headers ={
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Mobile Safari/537.36",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9,hi;q=0.8"
}

session = requests.Session()

request = session.get(url, headers=headers)
cookies = dict(request.cookies)
response = session.get(url,headers=headers,cookies=cookies).json()

rawdata = pd.DataFrame(response)
rawOp = pd.DataFrame(rawdata['filtered']["data"]).fillna(0)

print(rawOp)