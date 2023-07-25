# request module
import requests
# from bs4 import BeautifulSoup

# print(dir(requests))

# to get the code of the website
# response = requests.get("https://github.com/a1adeen")
# print(response.text)

# to scrap a website
# scrap = it means to exract the data from the website

# with this we can make file of the required code
url = "https://www.instagram.com/"
r = requests.get(url)
print(r.text)

with open("insta.html" ,"w") as i:
    i.write(r.text)