# single inheritance
class Animal():
    def __init__(self , name , species):
     self.name = name
     self.species = species

    def avaj(self):
         print("sound made by animal ")



class Dog(Animal):
    def __init__(self , breed):
        Animal.__init__(self, name="dog" ,  species="dog")
        self.breed = breed
    def mak_sound(self):
        print("bark!")


class Cat(Animal):
    def __init__(self , breed):
        Animal.__init__(self , name="meow" , species="billa")
        self.breed = breed

    def avaj_nikal(self):
        print("meow")


animal = Dog("vodafone")
animal.mak_sound()


animal_2 = Animal("capybara" , "donkey")
animal_2.avaj()


animal_3 = Cat("bilota")
animal_3.avaj_nikal()