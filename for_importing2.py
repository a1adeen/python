# function for welcome
# def welcome(name):
#     hey = (f"{name} your welcome")
#     if(hey == ""):
#         print('enter your name here again ')
#         welcome()
#     else:
#         print(hey)


# welcome()
hi = 3
# using while loop 
def welcome(name):
    hey = (f"{name} your welcome")
    if name == "" or '':
        print("run this function again and use string this time")
    else: 
           try:
             int(name)
             print("no integers are allowed")
           except:
               print(hey)

# print(__name__)               
# if __name__  == "__main__":
welcome("aladeen")     

