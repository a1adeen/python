# web scrapping
import requests
import bs4
import re

#
# result = requests.get('https://riyabanik.github.io/weather-react-app/')
# print(type(result))
# # print(result.text)
#
# soup = bs4.BeautifulSoup(result.text ,"lxml")
# print(soup)
# # by using this we can hop to any tag  of html
# print(soup.select('title')[0].getText())



#
# test

result_2 = requests.get('https://jnsougata.neobrains.dev/')
print(result_2.text)

sp_2 = bs4.BeautifulSoup(result_2.text , 'lxml')
# print(sp_2)
print(sp_2.select('p')[0].getText())

# hunt = re.findall('https' , sp_2)


# to grab the elements form the class and id
#<name> is used for id
print((sp_2.select('#go')))
# .<name> is used for classes
hunt = sp_2.select('.name')
for item in hunt:
    print(item)





# how to grab a image from the website

