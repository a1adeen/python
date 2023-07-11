# class method
# changing function in class
class Employee:
    company = "ETA"
    def __init__(self , name):
        print("activated")
        self.name = input("type employee's name here :")
    def show(self):
     print(f"name of employee is {self.name} and he works at {self.company}")
        # to change the function in the class
    def changecom(cls , new_company):
         cls.company = new_company


emp_1 = Employee("aladeen ")
print(emp_1)
emp_1.show()
emp_1.changecom("appple")
emp_1.show()
