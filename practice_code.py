# rock , paper , sciccors game
import random

def check(user , comp):
    if (user == comp):
        return 0
    if (user == 1 and comp == 2):
        return -1
    if (user == 2 and comp == 2):
        return -1
    if (user == 3 and comp == 1 ):
        return -1
    else:
        return 1
user = int(input("0 for rock , 1 for paper ,  2 for sciccors :"))
comp = (random.randint(0 , 2))

print("you chose : " , user )
print("computer choosen :" ,comp)


score = check(user , comp)
if score == -1:
    print("you loose :(")
elif score == 0 :
    print("its draw :0")
else:
    print("you win : D")