# multilevel inheritance



class Animal:
    def __init__(self , name , species):
        self.name = name
        self.species = species
    def show(self):
        print(f"name :{self.name}")
        print(f" species : {self.species}")
class Dog(Animal):
    def __init__(self , name , breed):
        Animal.__init__(self ,  name, species="dog" )
        self.breed = breed
    def show(self):
        Animal.show(self)
        print("'barks!")
        print(f"breed : {self.breed}")

class voda(Dog):
    def __init__(self, name, breed , color):
        super().__init__(name, breed="golden")
        self.color = color
    def show(self):
        Dog.show(self)
        print("its a dog here")
        print(f" color : {self.color}")



kutta = Dog("hiten" , "vodafone")
kutta.show()
