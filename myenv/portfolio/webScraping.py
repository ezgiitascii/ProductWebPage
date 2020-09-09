import requests
import pandas as pd
import datetime
from datetime import  date, timedelta
from matplotlib import pyplot as plt


#get yesterday date
today = date.today()
yesterday = today - datetime.timedelta(days=1)
ara= yesterday.strftime("%Y")+"-"+ yesterday.strftime("%m")+"-"+yesterday.strftime("%d")

#request and response
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
}
response = requests.get("https://api.turib.com.tr/api/getbulletin/"+ ara ,headers=headers)
j = response.json()

#save in dataframe
df = pd.DataFrame.from_dict(j["DailyList"])
df = df.set_index("Product")

#virtualization
df1 = df.drop(["Id","Type", "PrevClose", "TradeDate", "ISIN", "ProductCode", "ProductClass", "Low", "High", "NumberOfTrades", "TradedVolume", "TradedValue"], axis = 1)
df1.plot( subplots = True )

plt.legend()
plt.xlabel("Products")
#plt.title("Günlük Bülten")
plt.show()
