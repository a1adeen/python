import re

st = 'print only the words that start with letter s in this sentence'
for letter in st.split():
    if letter[0] == 's':
        print(letter)
        

