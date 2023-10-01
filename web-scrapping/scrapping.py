import bs4
from bs4 import BeautifulSoup
import requests



url = "https://www.codewithharry.com"
content_url = requests.get(url)
htmlcontent = content_url.content

# print(htmlcontent

# to parse the html content
# in order
soup = BeautifulSoup(htmlcontent , 'html.parser')
# print(soup.prettify())

# to get the tag
#
title= soup.li
print(type(title))


# to get all the elements for the tag


