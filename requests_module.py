import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.instagram.com")
# print(r.text)

soup = BeautifulSoup(r.text,"html.parser")

for heading in soup.find_all("h1"):
    print(heading.text)



# url = "https://jsonplaceholder.typicode.com/posts"

# data = {
#     "title" : 'rajan',
#     "body": 'dost',
#     "user Id": 12,
#     }
# headers = {
#     'Content-tpye':'application/json; charset=UTF-8',
#     }
# response = requests.post(url, headers=headers, json=data)