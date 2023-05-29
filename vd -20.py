#functions = a reusable code


# # mean fn
# a = 4
# b= 10
# mean = ((a*b)/(a +b))
# print(mean)


# mean funct
# !few funcs
def calculatemean(a ,b):
    mean = ((a*b)/(a + b))
    print(mean)

def isgreater( a ,b ):
    if(a > b):
        print("first no. is greater")    
    else:
        print("2nd no. is greater")    
def islesser( a , b):
    if(a < b):
        print("A is samaller then B")
    else:
        print("B is samaller than A") 
# !   
def equalto(a ,b):
    pass

d = 3
h = 8   
equalto( d, h )
islesser( d ,h)
isgreater( d, h)
calculatemean( d , h)



# from brocode


def happy_birthday(name):
    print(f"hayyp birthday to {name} ; D")
    print(f"hayyp birthday to {name} ; D")
    print(f"hayyp birthday to {name} ; D")


happy_birthday("aladeen")    

# another example

def happy_bday(naam , age):
    print(f"happy birthday to {naam}")
    print(f"your are {age} old")
    print(f"haoppy birhtday to {naam}")

happy_bday("ishant" , "9")    


# example of invoice

def invoice( username , amount , dueDate):
    print(f"hey {username}")
    print(f"your amount of ${amount} is due on :{dueDate}")


invoice("aladeen" , 90900909, "01/12/2024")   



# return function

def add( c, v):
    z = c + v
    return z

print(add( 2, 8))


# first and last name function
def your_name(first , last):
    first = first.capitalize()
    last = last.capitalize()
    return first + last

fullName = your_name("aladeen", "man")

print(fullName)