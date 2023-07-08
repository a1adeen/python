# static methods
class Maths:
    def __init__(self , num):
     self.num = num
    def adtono(self , n ):
        return self.num + n
# this function can be used anywhere
#     and this function is written inside the class because if the user import this class then user will also be provided with this funcion
    @staticmethod
    def add(a , b):
     return a + b

bey = Maths(9)
# bey.adtono(8)
print(bey.adtono(1))
print(bey.add(1 , 4))
