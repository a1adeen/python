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