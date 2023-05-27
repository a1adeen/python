#for loop
name = "ishant"
for n in name:
    print(n)
    if(n == "i"):
        print("this is special")

# making list
color = ["red","blue","green"]
for colors in color:
    print(colors)
for i in color:
    print(i)    


fame = ["ishant","aladeen"]
for n in fame:
    print(n)    


# 
for r in range(10):
    print(r)

# to count in reverse
for cout in reversed(range(1 , 11)):
    print(cout)

for ji in range(1,11):
    print(ji)



mobileNo = "8287606404"

for no in mobileNo:
    print(no)


# to skip a number 
for my in range(1 , 21):
    if(my == 16):
      continue   
    else:
        print(my)


# to break a loop 
for teri in range(1 , 31):
    if(teri == 26 ):
        break        
    else:
        print(teri)

# age = int(input("your age: "))
# if age > 100: print("This uis can't be real"); age = int(input("your age: "))
# elif age < 0: print("your age can't be -ve"); age = int(input("your age: "))        