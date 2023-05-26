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