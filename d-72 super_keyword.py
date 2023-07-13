# # super keyword
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











# last practise

class Hieght:
    def __init__(self , h):
        self.h = h

    def show(self):
        print(f"hieght of the person is {self.h}")


class Wieght(Hieght):
    def __init__(self , h , w):
        super().__init__( h)
        self.w = w
    def ic_w(self):
        print(f"wieght of the person is : {self.w}   hieght of the person is :{self.h}")


person_1 =Hieght(190)
person_1.show()


person_2 = Wieght(190 , 90)
person_2.ic_w()
# print(person_2.ic_w.__dict__())







