a = "ishant \n"
print(len(a))
print(a.upper())
a += "bhai don"
print(a)

# to remove signs after an strings = rstrip(that sign)
    



    # only signs after a string can be delected 
b = "hey================="
print(b.rstrip("="))
# print(b.strip("^"))

   # not signs before the strings
c = "^^^^hi^^^"
print(c.rstrip("^"))
# print(c.replace("hi","me"))
print(c.replace("hi","me"))


   # to make an list
l = "^^^^^^ supp ^^^^^^^"
print(l.split(" "))

    #to reduce human error and gramatical error of capitalize letter
c = "hey my name is ishant"
print(c.capitalize())

# example there is 1-2 gramatical errors in this sentence
e = "heLLo my name is aladeEN"

# to fix that capitalize letter error capitalize is used
print(e.capitalize())

# to write sentances in middle of the console
m = "its centre"
print(m.center(50))


# to know how many times a specific thing occurs in a string
again = "hey i am here again again again"
print(again.count("again"))

# to check how many a strings come ends with a letter

# ! it is only applicable with signs

end = "hey my name is aladeen :)"
print(end.endswith(":)"))
# print(end.endswith(":)" , 15 , 20))