# match case statement

import os

x = int(input("enter the value of x :"))
# if the value of x is 8 
match x:
    case 8:
        print("vaoue of x is 8")
    case 9:
        print("value of x is 9")
    case _:
        print("value of x is " , x)

    # case _ if x >= 10:
    #     print("x is smaller than 10")    
            
