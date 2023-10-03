import bs4
from bs4 import BeautifulSoup
import requests

url = "https://timesofindia.indiatimes.com/"

data = requests.get(url)
print(data.text)

soup = bs4.BeautifulSoup(data.text)
print(soup.prettify())