import datetime
import requests

today = datetime.date.today().strftime("%Y-%m-%d")
api_url = "https://newsapi.org/v2/top-headlines?country=jp&apiKey=あなたのAPIキー"
response = requests.get(api_url)
data = response.json()

articles = data.get("articles", [])[:5]  # 上位5件のニュースを取得

html_content = f"""<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>Daily News - {today}</title>
    <style>
        body {{
            font-family: sans-serif;
            background-image: url('https://source.unsplash.com/random/1600x900?{today}');
            background-size: cover;
            color: white;
            padding: 20px;
        }}
        .news {{
            background-color: rgba(0, 0, 0, 0.5);
            padding: 1em;
            margin: 1em 0;
            border-radius: 10px;
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
        <a href="{article['url']}" target="_blank" style="color: #fff;">続きを読む</a>
    </div>
    """

html_content += "</body></html>"

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)
