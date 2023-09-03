import requests
import bs4


url = requests.get('http://quotes.toscrape.com/')
print(url.text)

soup = bs4.BeautifulSoup(url.text , 'lxml')
print(soup.select('.author'))

# for authors
authors = []
for z in soup.select('.author'):
    authors.append(z.text)
# print(authors)
for author in authors:
    print(author)


# for quotes
quotes = []
for i in soup.select('.text'):
    quotes.append(i.text)
for quote in quotes:
    print(quote)


# tags

for items in soup.select('.tag-item'):
    print(items.text)

authorr = set()
url_2 = 'http://quotes.toscrape.com/page/'
for page in range(11):
    # authorr = set()
    page_url = f'http://quotes.toscrape.com/page/{page}'
    res = requests.get(page_url)
    soup_2 = bs4.BeautifulSoup(res.text , 'lxml')
    for name in soup.select('.author'):
        authorr.add(name.text)

print(authorr)


page_url = 'http://quotes.toscrape.com/page/999'