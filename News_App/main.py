import requests
query =input("What type of news are you interested in today?")
api="e56af16b1adc463e80618c7effc8af55"

url= f"https://newsapi.org/v2/everything?q={query}&from=2025-04-30&sortBy=publishedAt&apiKey={api}"

print(url)
r=requests.get(url)

data=r.json()
articles=data["articles"]

for index, article in enumerate( articles):
    print(index + 1,article["title"],article["url"])
    print("\n****************************************\n")
