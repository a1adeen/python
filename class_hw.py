

class Line():
    def __init__(self , x_1 ,y_1 ,x_2 , y_2):
        self.x_1 = x_1
        self.y_1 = y_1
        self.x_2 = x_2
        self.y_2 = y_2


    # def distance(self):
    #     return ((self.x_2 - self.x_1)**2 + (self.y_2 - self.y_1)**2)**1/2

    def slope(self):
        return (self.y_2 - self.y_1) / (self.x_2 - self.x_1)


cords = Line(3 , 2,8, 10)
print(cords.slope())




class Cylinder():
    def __init__(self , h , r):
        self.h = h
        self.r = r
    def volumn(self):
        pass
    def surfcae_area(self):
        pass