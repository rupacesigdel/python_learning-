import json
import requests

query = input("what type of news are you interested in? ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2024-04-06&sortBy=publishedAt&apiKey=4984d3711ee34bd8ac5f32717d871ad4"
r = requests.get(url)
news = json.loads(r.text)

# print(news, type(news))

for article in news["articles"]:
  print(article["title"])
  print(article["description"])
  print("---------------------------------------")
