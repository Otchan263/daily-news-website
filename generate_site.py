import datetime
import requests
import os

# 今日の日付
today = datetime.date.today().strftime("%Y-%m-%d")

# NewsAPIのキー（取得して置き換えてね）
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

# API URL
api_url = f"https://newsapi.org/v2/top-headlines?country=jp&apiKey={NEWS_API_KEY}"
response = requests.get(api_url)
data = response.json()

articles = data.get("articles", [])[:5]  # 上位5件取得

# HTML作成
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
            background-color: rgba(0,0,0,0.5);
            padding: 1em;
            border-radius: 10px;
            margin: 1em 0;
        }}
    </style>
</head>
<body>
    <h1>今日のニュース（{today}）</h1>
"""

for article in articles:
    html_content += f"""
    <div class="news">
        <h2>{article['title']}</h2>
        <p>{article.get('description', '')}</p>
        <a href="{article['url']}" target="_blank" style="color:#ffd;">続きを読む</a>
    </div>
    """

html_content += "</body></html>"

# 保存
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)
