
# # here i'm importing modules and trying them'
#
#
#
#
#
# import collections
# from collections import Counter
#
#
# list_1 = [1,1,1,1,1,1,3,3,3,3]
# print(Counter(list_1))
# list_2 = ["hhe" , "hhe" , "hhe"  ,9,9,99]
# print(Counter(list_2))


n = int(input("Enter an integer: "))
print(n)

if n % 2 != 0:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")

