import requests

#API呼び出しを作成してそのレスポンスを格納する
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept':'application/vnd.github.ve+json'}
r = requests.get(url, headers=headers)
print(f"ステータスコード: {r.status_code}")

#APIレスポンスを変巣に格納する
response_dict = r.json()

#結果を処理する
print(response_dict.keys())

