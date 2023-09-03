# import re
# import bs4
# import requests
#
#
# # print("availeble category for quotes:\n"
# #       "love\n"
# #       "inspirational\n"
# #       "life \n"
# #       "humor\n"
# #       "book\n"
# #       "reading\n"
# #       "freindship\n"
# #       "friends\n"
# #       "truth\n"
# #       "simile")
#
# list_bucket = ["love","inspirational","life ","humor","book", "reading","freindship", "friends", "truth","simile"]
# for i in list_bucket:
#       print(i , end=" , ")
#
# # to get the 1st and 2nd page link of the tag
# def fun_1(C):
#     page_1 =  f'http://quotes.toscrape.com/tag/{C}/'
#     page_2 = f'http://quotes.toscrape.com/tag/{C}/page/2/'
#     print(page_1)
#     return page_2
# # function to check the author_name
#
# # def author(tag):
#
#
#     # if f"https://quotes.toscrape.com/tag/{C}/page/2/" :
#     #     return f'https://quotes.toscrape.com/tag/{C}/page/2/'
#     # else:
#     #     print('only one page is there ')
# print(fun_1("humor"))
#
# url = requests.get('http://quotes.toscrape.com/tag/simile/'
#                    '')
# # print(url.text)
# soup = bs4.BeautifulSoup(url.text , 'lxml')
# print(soup.select('.author')[0:])
#
#
# # loop to get the all pages
#
# def lis():
#   for cat in list_bucket:
#     page_num_1 = []
#     # page_num_2 = []
#     links = f'http://quotes.toscrape.com/tag/{cat}\nhttp://quotes.toscrape.com/tag/{cat}/page/2/'
#     return page_num_1.append(links)
# hey = lis()
# print(hey)
# # all_links = bs4.BeautifulSoup(links.text , 'lxml')
# #
# # def to_scrap():
# #     pass



# solution from the course







