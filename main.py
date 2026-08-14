import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

url = "https://newsapi.org/v2/top-headlines"

params = {
    "country": "us",
    "apiKey": os.getenv("NEWS_API_KEY")
}

response = requests.get(url, params=params)

print(response.status_code)

data = response.json()

articles = data["articles"]

for article in articles:
    print(article["title"])

with open("news.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)

print("News saved successfully!")