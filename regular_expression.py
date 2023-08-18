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