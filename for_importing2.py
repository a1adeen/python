# function for welcome
# def welcome(name):
#     hey = (f"{name} your welcome")
#     if(hey == ""):
#         print('enter your name here again ')
#         welcome()
#     else:
#         print(hey)


# welcome()

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
if __name__  == "__main__":
 welcome("hey")     
print(__name__)