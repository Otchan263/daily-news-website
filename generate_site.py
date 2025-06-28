import datetime
import requests
import os

today = datetime.date.today().strftime("%Y-%m-%d")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
api_url = f"https://newsapi.org/v2/top-headlines?country=jp&apiKey={NEWS_API_KEY}"
response = requests.get(api_url)
data = response.json()
articles = data.get("articles", [])[:5]

# 背景画像の固定
background_url = "https://source.unsplash.com/1600x900/?nature,landscape"

html_content = f"""<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>Daily News - {today}</title>
    <style>
        body {{
            font-family: sans-serif;
            background-image: url('{background_url}');
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
        a {{ color: #ffd; }}
    </style>
</head>
<body>
    <h1>今日のニュース - {today}</h1>
"""

if not articles:
    html_content += "<p>現在、取得できるニュースがありません。</p>"
else:
    for article in articles:
        title = article.get('title') or 'タイトルなし'
        description = article.get('description') or ''
        url = article.get('url') or '#'

        html_content += f"""
        <div class="news">
            <h2>{title}</h2>
            <p>{description}</p>
            <a href="{url}" target="_blank">続きを読む</a>
        </div>
        """

html_content += "</body></html>"

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("✅ index.html を正常に生成しました。")
