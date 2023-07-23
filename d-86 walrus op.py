# walrus operator


# ex
list_1 = [1,2,3,4,5]
while (n := len(list_1)) > 0 :
    print(list_1.pop())



# normal code
foods = list()

while True:
    food =input(f"what food do u like? :")
    if food == "quit":
            break
    foods.append(food)



# walrus method

khaana = list()
while (khana := input("what ur fav food? :")) != "quit":
    khaana.append(khana)




# another example


name = input("whats ur name :")
if name == int():
    print("no integers are allowed here")
else:
    print(name)

naam = input("tell me ur name")
if naam := int() : print("no int ae allowed ")
else : print(naam)