# multilevel inheritance



class Animal:
    def __init__(self , name , species):
        self.name = name
        self.species = species
    def show(self):
        print("ye to kutta hai ")
class Dog(Animal):
    def __init__(self , name , breed):
        Animal.__init__(
            name="bhai" , species="vodafone")
        self.breed = breed
    def show(self):
        print("'barks!")

class voda(Dog):
    def __init__(self, name, breed , color):
        super().__init__(name, breed="golden")
        self.color = color
    def show(self):
        print("its a dog here")
