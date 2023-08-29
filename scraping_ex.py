import re
import bs4
import requests


# print("availeble category for quotes:\n"
#       "love\n"
#       "inspirational\n"
#       "life \n"
#       "humor\n"
#       "book\n"
#       "reading\n"
#       "freindship\n"
#       "friends\n"
#       "truth\n"
#       "simile")

list_bucket = ["love","inspirational","life ","humor","book", "reading","freindship", "friends", "truth","simile"]
for i in list_bucket:
      print(i , end=" , ")
def fun_1(C):
    return f'http://quotes.toscrape.com/tag/{C}/'
print(fun_1("simile"))

url = requests.get('http://quotes.toscrape.com/tag/simile/')
# print(url.text)
soup = bs4.BeautifulSoup(url.text , 'lxml')
print(soup.select('.author')[0:])