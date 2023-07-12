# class method as alternative constructor
class Employee:
    def __init__(self , name , salary):
        self.name = name
        self.salary = salary
        print(f"{self.name} earns {self.salary} from the company")
        # if the info is give in string format
    @classmethod
    def another(cls,string):
            return cls(string.split("-")[0], string.split("-")[1])

        # this will work perfectly
emp = Employee("aladeen", 1000020)
# but if the data is given in string form then we will use alternate class method

string = "aladesen-1202020"
es = Employee.another(string)
print(es.salary)
hey = "ishant-101010"
es_2  = Employee.another(hey)

# class Employee:
#     def __init__(self , name , salary):
#         self.name = name
#         self.salary = salary
#
#     @classmethod
#     def from_str(cls , string):
#         return cls(string.split("-")[0] , string.split("-")[1])
#
# e1 = Employee("aladdeen" , 120202)
# print(e1.name)
#
# strin = "aladeen-12000"
# e2 = Employee.from_str(strin)
# print(e2.name)
# print(e2.salary)
#


# using (,) for spilting
class Player:
    def __init__(self , naam , rank):
        print("player class is activated")
        self.naam = naam
        self.rank = rank
        print(f"{self.naam} is on {self.rank} in valorant")
    @classmethod
    def cust(cls , string):
        return cls(string.split(",")[0] , string.split(",")[1])
he = "aladeen,ace"
es_8 = Player.cust(he)
# print(es_8)
