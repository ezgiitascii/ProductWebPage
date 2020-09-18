import requests
import pandas as pd
import datetime
from datetime import  date, timedelta
from matplotlib import pyplot as plt

#get yesterday date
yesterday = date.today() - datetime.timedelta(days=1)
dateStr = yesterday.strftime("%Y") + "-" + yesterday.strftime("%m") + "-" + yesterday.strftime("%d")
print(dateStr)

#request and response
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
}
response = requests.get("https://api.turib.com.tr/api/getbulletinsummary/"+ dateStr, headers=headers)
jsonData = response.json()

#save in dataframe
df = pd.DataFrame.from_dict(jsonData["InstantlyList"])
df = df.set_index("Product")

#virtualization
#df1 = df.drop(["Id","Type", "PrevClose", "TradeDate", "ISIN", "ProductCode", "ProductClass", "Low", "High", "NumberOfTrades", "TradedVolume", "TradedValue"], axis = 1)
df1 = df.drop(["TradeDate", "ProductType", "ProductGroup", "NumberOfTrades", "TradedVolume", "TradedValue", "Anlasmali"], axis = 1)
df1.plot( subplots = True )

plt.legend()
plt.xlabel("Products")
#plt.title("Günlük Bülten")
plt.show()
