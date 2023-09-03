import re

# num = int(input("num here"))
# if num >= 1:
#     for i in range(2 , num):
#         if num % i == 0:
#             print("its not prime number")
#             break
#     else:
#         print('its prime number ')
#
# #
#
# def func_1(n):
#     first_half = n[:3]
#     second_half = n[3:]
#     print(first_half.capitalize() + second_half.capitalize())
#
#
# hey = func_1('ishant')
# print(hey)\
LIS = 'hey my name is ishant'
print(LIS.split())

def func(a,b):
    if a % 2 == 0 and b % 2 == 0 :
        if a < b :
            print(a)
        else:
            print(b)
    elif a % 2 == 0 and b % 2 != 0:
        if a < b :
            print(b)
        else:
            print(a)
    elif  a % 2 != 0 and b % 2 != 0:
        if a < b :
            print(b)
        else:
            print(a)


#
# hr = func(10 , 7 )
#
# print(hr)



def lesser_of_two_evens(a,b):

    if a % 2 == 0 and b % 2 == 0:
        return min(a,b)
    else:
        return max(a,b)

hey = lesser_of_two_evens(11 , 19)
print(hey)




def animal(i):
    i.split()
    if i[0][0] == i[1][0]:
        return  True
    else:
        return False

hey_2 = animal('crazy kangroo')
print(hey_2)

def twenty(h , k):
    if h + k == 20:
        return True
    elif h == 20 or k == 20:
        return True
    else:
        return  False


hey_3 = twenty(10 , 20)
print(hey_3)

# def makes_twenty(n1,n2):
#
#     if n1+n2 == 20:
#         return True
#     elif n1 == 20 or n2 == 20:
#         return True
#     else:
#         return False
#
# hey_5 = makes_twenty(20 , 0)
# print(hey_5)


#
# def cap(na):
#    first = na.capitalize()
#    secon
#
# hey_6 = cap("ishant")
# print(hey_6)


def old_macdonald(name):
    first = name[:3]
    second = name[3:]
    return first.capitalize() + second.capitalize()
hey_9 = old_macdonald('macdonald')
print(hey_9)