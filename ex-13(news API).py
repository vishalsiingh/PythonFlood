# import requests
# query = input("Which type of news do you want: ")
# url=f"https://newsapi.org/v2/everything?q=tesla{query}&from=2024-11-26&sortBy=publishedAt&apiKey=d6e007b3fa4540e9a78bf725fd312916"
# r=requests.get(url) 
# print(r.text)

# import requests
# import json

# query = input("What type of news are you interested in? ")
# url = f"https://newsapi.org/v2/everything?q={query}&from=2023-01-28&sortBy=publishedAt&apiKey=dbe57b028aeb41e285a226a94865f7a7"
# r = requests.get(url)
# news = json.loads(r.text)
# # print(news, type(news))
# for article in news["article"]:
#   print(article["title"])
#   print(article["description"])
#   print("--------------------------------------")
  
import requests
import json


query=input("What type of news are you intested in: ")
url="https://newsapi.org/v2/everything?q={query}&from=2024-11-26&sortBy=publishedAt&apiKey=d6e007b3fa4540e9a78bf725fd312916"
r=requests.get(url)
news=json.loads(r.text)
# print(news,type(news))
for article in news["articles"]:
  print(article["author"])
  print(article["title"])
  print(article["description"])
  print("----------")
  
  
  
