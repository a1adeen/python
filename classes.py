# OOPs

class Dog:
    reminder = 'name of the dog is provided'
    def __init__(self , breed , name ):
        self.breed = breed
        self.name = name
    def __str__(self):
        return f'breed of the dog is {self.breed} and his name is {self.name}'
    def bark(self , num ):
        for i in range(num):
           print(f'woof my name is {self.name}')
hey = Dog(breed='hiten' , name="hiten ")
print(hey)

class Circle():
    pi = 3.14

    def __init__(self , r):
        self.r = r
    def circumfrence(self):
        return 2 * self.r * Circle.pi
    def area(self):
        return Circle.pi * self.r**2


num = Circle(3)
print(num.area())