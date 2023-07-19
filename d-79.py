# multiple inheritance
class Gamer:
    def __init__(self , name ):
        self.name = name 
    def show(self):
        print(f"name of the gamer is {self.name}")    



class programmer:
    def __init__(self , naam):
        self.naam = naam

    def show(self):
        print(f"name of the programmer is {self.naam}")    
          

# this will give most priority to tha most preciding class
# if will place programmer in place of gamer  then it will print "name of the programmer"
class Gameboy(Gamer , programmer):
     def __init__(self, name , naam):
         self.name = name 
         self.naam = naam 



hey =   Gameboy("aladeen" ,"a1adeen")      
hey.show()   

# MRO
# method resolution order 
# this will show the order of inherited classes 
print(Gameboy.mro())