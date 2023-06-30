


# constructor
class Emp:
  def __init__(self, n, o):
    print("activated")
    self.name= n
    self.post = o
  def info(self):
    print(f"{self.name} is {self.post} in the company")

emp = Emp("aladeen", "ceo")
emp.info()


emp_1 = Emp("ishant" , "ceo")
emp_1.info()


class Studen:
  def __init__(self , name , sec):
    print("activated")
    self.n = name
    self.s = sec
  def info(self):
      print(f"{self.n} is the student of {self.s} ")

aladeen = Studen("aladeen" , "12th B")
aladeen.info()