# # file handling





# reading file 

file = open('hey.txt', 'r')
text = file.read()
print(text)
file.close()


# to write a content in the file

write = open('new.txt',  'w')
write.write("hey it starts from here")
write.close()



# appending new txt in the file
file = open('append.txt' , 'a')
file.write("hey bhai hai")
file.close()



# ex of reading 

# hi = open('append.txt' , 'r')
# read = hi.read()
# hi.close()
# print(read)

#
# apppending = open('new.txt,'a')
# apppending.write("   : its the new text here")
# apppending.close()


new = open('nex.txt', 'w')
new.write("hey how are uits new line added here")
new.close()
