# super keyword
# class Parent:
#     def parent_method(self):
#         print("this is parent class ")


# class Child(Parent):
#     def parent_method(self):
#         print("hey")
#         super().parent_method()
#     def child_mehtod(self):
#         print("this  is the child method")
#         # super().parent_mehtod()







# bey = Child()
# bey.child_mehtod()
# # if there will be no parent_class method in the chil class then it wil print from parent
# bey.parent_method()


# # another example

# class Job:
#     def __init__(self , name , id):
#         self.name = name
#         self.id = id
#     def show(self):
#         print(f"{self.name} has {self.id}")
#         # print(f" id of {self.name} is {self.id}")
# class Programmer(Job):
#     def __init__(self ,  lang):
#         self.lang = lang
#         super().__init__()

# man_1 = Job("aladeen" , "hry")
# man_1.show()


# class Employee:
#     def __init__(self , name , id):
#         self.name = name
#         self.id = id

# class Programar(Employee):
#     def __init__(self, name, id , lang):
#         super().__init__(name, id)
#         self.lang = lang


# hey = Employee("aladeeen" , 9090)
# aladeen = Programar("aladeen" , 9090 , "python")
# print(hey.name)
# print(aladeen.lang)




