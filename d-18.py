# while loops

i = 0 
while (i < 10):
    print(i) 
    i = i + 3


name = input("your name :  ")  
while name == "":
    print("you did'nt entered your name")  
    name = input("enter your name :")  
print("hello",name )  


age = int(input("your age: "))
while age < 0:
    print("your age can't be -ve")
    age = int(input("enter your age : "))

print(f"your age is {age}")



# brocode 4.42 

age = int(input("your age: "))
if age > 100:
     print("This is can't be real"); 
     age = int(input("your age: "))
elif age < 0: 
    print("your age can't be -ve"); 
    age = int(input("your age: "))
else:
    print(f"your age is{age}")    


# !to give an unstopable error
# count = 5 
# while (count > 0):
#     print(count)
#     count = count +1

