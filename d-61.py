

# just a practice
#
# import os.path
#
# if (os.path.exists("10days")):
#     print("yes")
# else:
#     print("no")
# os.mkdir("10days")
# for i in range(10):
#     os.mkdir(f"10days/day {i + 1}")


# inheritence of pyhton
class Emp:
    def __init__(self , name , id):
       self.name = name
       self.id = id
    def details(self):
        print(f"{self.name} works on {self.id}")



emp_1 = Emp("aladeen" , "HTML")
emp_1.details()


# to add the new function in a existing class

class Id(Emp):
    def show_lang(self):
        print("default language is pyhton")
emp_3 = Id("aladene" , "html" )
emp_3.show_lang()













# 2nd class
class Animal:

     Alive = True

     def eat(self):
         print("this animal is eating")
     def sleep(self):
         print("this animal is sleeping")

class dog(Animal):
    pass
class cat(Animal):
    pass
Cat = cat()
print(cat.Alive)
Dog = dog()
Dog.eat()


