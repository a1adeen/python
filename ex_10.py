import requests
import json

# print(dir(requests))
query = input("what type of news are you intrested in :")
url = f"https://newsapi.org/v2/everything?q={query}from=2023-06-28&sortBy=publishedAt&apiKey=e7a1362cdcb3470fb7d092c0c1f99465"
r = requests.get(url)
news = json.loads(r.text)
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("----------------------")
# print(news)
# print(r.text)