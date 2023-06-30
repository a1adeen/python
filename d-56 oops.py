# object orianted programming
# classes and object







# class
class Student():
    name ="ishant"
    section = 12
    performance = "jod lvl"
    def info(self):
     print(f"{self.name} is a {self.performance} in performance")

aladeen = Student()
aladeen.info()




# for student_2
spouk = Student()
spouk.name = "harshit"
spouk.performance = "noob"
spouk.info()



# for car
class Car():
    company = "mercedes"
    model = "s class "
    color = "black"
    def about(self):
     print(f"{Car.model} of {Car.company} in {Car.color} color")


car_1 = Car()
car_1.about()