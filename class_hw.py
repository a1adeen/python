

class Line():
    def __init__(self , x_1 ,y_1 ,x_2 , y_2):
        self.x_1 = x_1
        self.y_1 = y_1
        self.x_2 = x_2
        self.y_2 = y_2


    def distance(self):
        return ((self.x_2 - self.x_1)**2 + (self.y_2 - self.y_1)**2)**0.5

    def slope(self):
        return (self.y_2 - self.y_1) / (self.x_2 - self.x_1)


cords = Line(3,2,8,10)
print(cords.slope())




class Cylinder():
    pi = 3.14
    def __init__(self , h , r):
        self.h = h
        self.r = r
    def volumn(self):
        return Cylinder.pi * self.r**2 * self.h

    def surfcae_area(self):
        return 2*Cylinder.pi * self.r * self.h + 2 * Cylinder.pi * self.r**2


cyl = Cylinder(2 , 3)
print(cyl.surfcae_area())




