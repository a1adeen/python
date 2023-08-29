import requests
import bs4
import re
def func_1(n):
   return  f'http://books.toscrape.com/catalogue/page-{n}.html'

url = requests.get('http://books.toscrape.com/catalogue/page-1.html')
# html = url.text.replace('  ',"").replace("\n" , "")
# found = re.findall("<p class=\"star-rating One\">(.*?)</p>" , html )[0]
# print(found)
# print(found.count("<i"))
# # print(html)

# print(dir(re))
soup = bs4.BeautifulSoup(url.text , 'lxml')
# print(soup)
hunt = soup.select('.product_pod')
stars = hunt[0]
print(stars.select('.star-rating.Three'))
# here is how u can get the only title from the specific tag
print(stars.select('a')[1]['title'])


for n in range(1,51):
    two_star_title = []
    scrap_url = func_1(4)
    res = requests.get(scrap_url)

    soup_2 = bs4.BeautifulSoup(res.text , 'lxml')
    books = soup_2.select('.product_pod')

    for book in books:
        if len(book.select(".star-rating.Two")) != 0:
            book_title = book.select('a')[1]['title']
            two_star_title.append(book_title)
            # print(two_star_title)