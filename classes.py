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
# print(hey)

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

# using inheritance

class Animal():
    def __init__(self):
        print('animal created')

    def who_am_i(self):
        print('i am an animal')

    def eat(self):
        print('i am eating')



# print(hey_1)


# POLYMORPHISM


# in this thsi the 2 diffrent class uses the same function name
class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self)
        self.name = name
        print('Dog created')

    def speak(self):
        return f'{self.name} says woof'


beti_dog = Dog(name="huuihiui")

class Cat():
    def __init__(self , name ):
        Animal.__init__(self)
        self.name = name
        print('cat created')

    def speak(self):
        return f'{self.name} says moew'
# naming the cat
niko_the_cat = Cat(name = "sui")
print(niko_the_cat)

# function to for speaking of the animal
def spk(nam):
    print(nam.speak())



class ANimal_2():
    def __init__(self , naam):
        self.naam = naam

    def says(self):
        raise NotImplementedError('subclass is need ')


class Kuuta(ANimal_2):
    def says(self):
        return f'{self.naam} says woof!'

class Billi(ANimal_2):
    def says(self):
        return f'{self.naam} says meow!!'


kutt = Kuuta(naam='hey')
print(kutt.says())
hii = Billi(naam='skslc')
print(hii)




# magic and dunder method
class Book():

    def __init__(self , tittle, author , page):
        self.tittle = tittle
        self.author = author
        self.page = page

    def __str__(self):
        return f'{self.tittle} of {self.author}'

    def __del__(self):
        return "this object has been deleted"



hey_4 = Book('intelligent investor' , 'benjamin grahmin' , 664)
print(hey_4)
