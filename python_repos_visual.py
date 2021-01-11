import requests#p170からスタート!(p164と同じ)

from plotly.graph_objs import Bar
from plotly import offline

#API呼び出しを作成してそのレスポンスを格納する(p164)
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept':'application/vnd.github.ve+json'}
r = requests.get(url, headers=headers)
print(f"ステータスコード: {r.status_code}")

#結果を処理する(p170)
response_dict = r.json()#o164と同じ
repo_dicts = response_dict['items']#(p166と同じ)

# repo_names, stars, labels = [], [], []#labels追加(p174)
repo_links, stars, labels = [], [], []#repo_namesをrepo_linksに変更(p176)
for repo_dict in repo_dicts:
    # repo_names.append(repo_dict['name'])
    repo_name = repo_dict['name']#p176
    repo_url = repo_dict['html_url']#p176
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"#p176
    repo_links.append(repo_link)#p176

    stars.append(repo_dict['stargazers_count'])

    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}<br />{description}"#p175
    labels.append(label)#p175

#可視化を実行する(p171)
data = [{#p153とp121,122のbar参照
    'type':'bar',
    # 'x': repo_names,
    'x': repo_links,
    'y': stars,
    'hovertext':labels,#追加(p175)
    'marker':{#でグラフ改良のため追加(p172)
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,#不透明度
}]

my_layout = {
    'title': 'GitHubで最も多くのスターがついているPythonプロジェクト',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'リポジトリ',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'スターの数',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')
