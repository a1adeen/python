player = {
    -1 : "snake",
     0 : "water",
     1 : "gun"

}
computer = {
    2 : "snake",
    3 : "water",
    4 : "gun"
}



rules = ("before starting note that the -1 = snake   0 = water    and 1 = gun ")
print(rules)
start = (input("start playing :"))
if (start == -1):
    print("you win")
elif start == 0:
    print("you lost")
if start == 1:
    print("u wins")
elif(start == ""):
        raise ValueError("no strings are allowed here")
else:
    print("teri mummi")



# will continue this