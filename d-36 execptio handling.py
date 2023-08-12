# execption handling
# a = int(input("enter the number here for multiplication : "))
# print(f"multiplication of {a}")


# for i in range (11):
#     print(f"{a} X {i} = {a*i}")


# try and except 
# e = error

# hey = (input("enter number : "))
# print("multiplication table is here ")
# try :
#     for y in range(11):
#      print(f"{int(hey)} X {y} = {int(hey * y)}")
#
# except Exception as e:
#     print(e)
#
#     # here we can alse type any line in except e in execption
#     # ex  = print("sorry an error occured") or ("invalid input ") this will me more effective
#
# print("some imp line of coeds")
#

# to avoid this we can use 
# hey = int(input("enter number:")) in input 
     

     
# practicing
# try:
# #     f = open("heym" , 'w')
# #     f.write("bhai hai ")
# # except:
# #     print("bhai kya krra hai ")
# #
# # finally:
# #     print("i always run")
def as_num():
    while True:

        try:
           print(input(int("enter the integer here :")))
        except:
            return "enter the integer!!!!"

        else:
            print("yup now u ca nmove over ")
            break
        finally:
            print("ended the exception part ")
as_num()