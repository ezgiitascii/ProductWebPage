import requests
import pandas as pd


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
}

response = requests.get("https://api.turib.com.tr/api/getbulletin/2020-09-03",headers=headers)

j = response.json()

df = pd.DataFrame.from_dict(j["DailyList"])

#df = df.set_index("")

print(df)
