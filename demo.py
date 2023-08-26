import requests
import bs4

url = requests.get('https://en.wikipedia.org/wiki/Ishant_Sharma')
print(url.text)
soup = bs4.BeautifulSoup(url.text , 'lxml')
print(soup)
# to get the picture that u want
hunt = soup.select('.mw-file-element')[1]
print(hunt['srcset'])

#
get_pic = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/Ishant_Sharma_4.jpg/440px-Ishant_Sharma_4.jpg ')
f = open('get_pi' , 'wb')
f.write(get_pic.content)
print(get_pic)