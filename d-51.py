# (seek) and (tell) in file handling
f = open('seek.txt', 'r')
text = f.read()
f.close()
print(text)
#
# hey = open('ggs.txt','r')
# ih = hey.read()
# hey.close()
# print(ih)
# hey.seek(5)
# data = hey.read(9)
#  print((data))
with open('ggs.txt','r') as f:
    f.seek(7)
    data = f.read(9)
    print(data)


# did seek , tell and trunket in file handling


