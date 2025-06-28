import datetime
import requests
import os

# 日付を取得
today = datetime.date.today().strftime("%Y-%m-%d")

# NewsAPIキーを環境変数から取得
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

# NewsAPIエンドポイント
api_url = f"https://newsapi.org/v2/top-headlines?country=jp&apiKey={NEWS_API_KEY}"

# ニュースを取得
response = requests.get(api_url)
data = response.json()
articles = data.get("articles", [])[:5]  # 上位5記事を取得

# HTMLを作成
html_content = f"""<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>Daily News - {today}</title>
    <style>
        body {{
            font-family: sans-serif;
            background-image: url('https://source.unsplash.com/1600x900/?nature,{today}');
            background-size: cover;
            background-position: center;
            color: white;
            padding: 2em;
        }}
        .news {{
            background-color: rgba(0,0,0,0.6);
            padding: 1em;
            margin: 1em 0;
            border-radius: 10px;
        }}
        a {{
            color: #ffd;
        }}
    </style>
</head>
<body>
    <h1>今日のニュース - {today}</h1>
"""

for article in articles:
    html_content += f"""
    <div class="news">
        <h2>{article['title']}</h2>
        <p>{article.get('description', '')}</p>
        <a href="{article['url']}" target="_blank">続きを読む</a>
    </div>
    """

html_content += "</body></html>"

# index.html を保存
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("✅ index.html を生成しました。")
