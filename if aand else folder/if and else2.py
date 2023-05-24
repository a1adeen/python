iphone = 1000
budget = 10000

if(iphone<=budget):
    print("you can buy iphone")
else:
    print("you can't buy iphone u are broke")


# another example 

num = int(input("enter the number here :"))
if(num>0):
    print("number is +ve")
elif(num==0):
    print("number is 0")
else:
    print("numberr is -ve")

print("now its good")   

# structure of elif

numb = int(input("enter number here :"))
if(numb < 0):
    print("number is +ve")
elif(numb >= 10):
    if(numb == 10):
        print("number is special")
    elif(numb > 10 and numb <= 20):
        print("number is b/w 10-20")
    else:
        print("number is -ve")           

# its working
        