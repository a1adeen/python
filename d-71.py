# dir  , __dict__ , and help




# dir method help to show all the attribute availeble for an object
hey = "ishant"
print(dir(hey))


# __dict__
# it helps to make a dictionary
class Person:
    def __init__(self , name , salary):
        self.name = name
        self.salary = salary


emp = Person("aladeen" , 12000)
print(emp.__dict__)


# help method
class Paratha:
    def __init__(self , name):
        self.name = name
print(help(Paratha))