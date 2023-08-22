import re


text = "the agent's number is 408-55-1234 the"
# byt using this we can only find the first matxh
f = 'the'
hey = re.search(f , text)
print(hey)

# by this we can find the required word multiple times
fin = "hey my name is aladeen , hey my name is aladeen"
find = 'hey'
hei = re.findall(find , fin)
print(len(hei))

# part 2
my_text = 'my mobile number is 494-343-344777'
hunt = re.findall('\d\d\d-\d\d\d-\d\d\d' , my_text)
print(hunt)


# or

hunt_2 = re.findall('\d{3}-\d{3}-\d{3}' , my_text)
print(hunt_2)


sear = 'hey how can i help u bhai hat sat cat '
# by using | we can use or statment here
hunt_3 = re.search('bhai|bhen' , sear)
# and here we use dot for the strings who have the similar suffix
hunt_4 = re.findall('.at' , sear)
print(hunt_4)
print(hunt_3)
# this only searches the text which have the number at he start
search_1 = '1 is a number'
hunt_5 = re.findall('^\d' , search_1)
print(hunt_5)
# for the number at the end
search_2 = 'the number is 2'
hunt_6 = re.findall('\d$', search_2)
print(hunt_6)






# too exclude the number or text
search_2 = 'there are 3! number?? 34 inside the text'
# byt using the + sign we can get he texts together
hunt_7 = r'[^\d]+'
# to remove the specific words
hunt_8 = r'[^!?]+'
print(re.findall(hunt_8 , search_2))

search_3 = 'hey my-name is ishant hello ala-deen'
pattern = r'[\w]+-[\w]+'
print(re.findall(pattern , search_3))

