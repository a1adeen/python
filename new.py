# player = {
#     -1 : "snake",
#      0 : "water",
#      1 : "gun"
#
# }
# computer = {
#     2 : "snake",
#     3 : "water",
#     4 : "gun"
# }
#
#
#
# rules = ("before starting note that the -1 = snake   0 = water    and 1 = gun ")
# print(rules)
# start = (input("start playing :"))
# if (start == -1):
#     print("you win")
# elif start == 0:
#     print("you lost")
# if start == 1:
#     print("u wins")
#
# else:
#    raise ValueError("no strings are allowed")
#
#

# will continue this
# new solution
import random

def check(user , comp):
    if (user == comp ):
        return 0
    if ( user == 1 and comp == 0 ):
        return -1
    if (user == 1 and comp == 2):
        return -1
    if( user == 0 and comp == 2):
        return -1
    else:
        return 1




user = int(input("0 for snake  , 1 for water , 2 for gun :"))
comp = (random.randint(0 ,2))

score = check(user , comp)
if score == 0 :
 print("its a draw")
elif(score == 1):
    print("you won")
else:
    print("you lose")


print("what you have chosen")
print("you :" , user )
print("computer : " , comp)