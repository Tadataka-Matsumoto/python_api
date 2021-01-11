import requests
import json

#api呼び出しを作成してそのレスポンスを格納する(p178)
url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'
r = requests.get(url)
print(f"ステータスコード： {r.status_code}")
# print(r.json())

#データの構造を調べる(p178)
response_dict = r.json()
readable_file = 'data/readable_hn_data.json'
with open(readable_file, 'w') as f:
    print(json.dump(response_dict, f, indent=4))




