# Other libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
from urllib.request import urlopen
piford_key = '4697a70d83f61dd8f9d8631205844732'
#https://financialmodelingprep.com/api/v3/profile/AAPL?apikey=e0c8820624abede12b92380ba5147ace

sym='AAPL'
#sym=['TWTR','FB','MSFT','NVDA','AAPL','CRM']
#url = "https://financialmodelingprep.com/api/v3/company/profile/"+str(sym)+'?apikey='+piford_key
#response = urlopen(url)
#data = response.read().decode("utf-8")
#profile = json.loads(data)
#profile

url = "https://financialmodelingprep.com/api/v3/company/profile/AAPL,CRM,NVDA"+'?apikey='+piford_key
response = urlopen(url)
data = response.read().decode("utf-8")
profile = json.loads(data)
print(profile)

# plt.figure(figsize=(10,4))
# plt.title("Book Value per Share",fontsize=18)
# plt.bar(x=df1['companyName'],height=df1['price'],color='orange',edgecolor='k')
# plt.xticks(fontsize=14,rotation=45)
# plt.yticks(fontsize=14)
# plt.ylabel('Price',fontsize=16)
# plt.show()

# plt.figure(figsize=(10,4))
# plt.title("debtEquityRatio",fontsize=18)
# plt.bar(x=df1['companyName'],height=df1['debtEquityRatio'])
# plt.xticks(fontsize=14,rotation=45)
# plt.yticks(fontsize=14)
# plt.ylabel("debtEquityRatio",fontsize=16)
# plt.show()

# # Only companies with market cap > 200 billion USD
# df_large_cap = df1[df1['Market Cap']>200e9]
# df_large_cap[['companyName','Market Cap']]