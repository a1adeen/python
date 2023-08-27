import requests
import bs4
def func_1(n):
    print(f'http://books.toscrape.com'
          f'/catalogue/page-{n}.html')

url = requests.get('http://books.toscrape.com/catalogue/page-1.html')
# print(url.text)
soup = bs4.BeautifulSoup(url.text , 'lxml')
# print(soup)
hunt = soup.select('.product_pod')
stars = hunt[0]
print(stars.select('.star-rating.Three'))
# here is how u can get the only title from the specific tag
print(stars.select('a')[1]['title'])

two_star_title = []
for n in range(1,51):

    scrap_url = func_1(n)
    res = requests.get(scrap_url)

    soup_2 = bs4.BeautifulSoup(res.text , 'lxml')
    books = soup_2.select('.product_pod')