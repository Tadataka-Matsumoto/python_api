import requests#p164

#API呼び出しを作成してそのレスポンスを格納する(p164)
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept':'application/vnd.github.ve+json'}
r = requests.get(url, headers=headers)
print(f"ステータスコード: {r.status_code}")

#APIレスポンスを変巣に格納する(p164)
response_dict = r.json()

#結果を処理する(p164)
print(response_dict.keys())


print(f"全リポジトリ数: {response_dict['total_count']}")#全リポジトリ数を出力(p165)


#リポジトリに関する情報を調べる(P166)
repo_dicts = response_dict['items']#(p166)
print(f"情報が返されたリポジトリの数:{len(repo_dicts)}")


#一つ目のリポジトリを調査する(p166)
repo_dict = repo_dicts[0]
print(f"\nキーの数: {len(repo_dict)}")#キーの数は74で本と同じ(p166)
# for key in sorted(repo_dict.keys()):
#     print(key)

# #p167のプリント情報
# print("\n1つめのリポジトリの情報抜粋：")
# print(f"名前：{repo_dict['name']}")
# print(f"所有者：{repo_dict['owner']['login']}")
# print(f"スターの数：{repo_dict['stargazers_count']}")
# print(f"リポジトリURL：{repo_dict['html_url']}")
# print(f"作成日時：{repo_dict['created_at']}")
# print(f"最終更新日時：{repo_dict['updated_at']}")
# print(f"説明文：{repo_dict['description']}")


# p168のプリント情報
print("\n各リポジトリの情報抜粋：")
for repo_dict in repo_dicts:
    print(f"\n名前：{repo_dict['name']}")
    print(f"所有者：{repo_dict['owner']['login']}")
    print(f"スターの数：{repo_dict['stargazers_count']}")
    print(f"リポジトリURL：{repo_dict['html_url']}")
    print(f"説明文：{repo_dict['description']}")


