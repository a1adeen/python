import re

num = int(input("num here"))
if num >= 1:
    for i in range(2 , num):
        if num % i == 0:
            print("its not prime number")
            break
    else:
        print('its prime number ')


