
# method over riding
class Shape:
    def __init__(self , x, y ):
        self.x = x
        self.y = y
    def area(self):
        return self.x * self.y


obj = Shape(9 , 10)
print(obj.area())


class Circle(Shape):
    def __init__(self , r ):
     self.r = r
     super().__init__(r , r)
    def area(self ):
        return 3.14 * super().area()

c = Circle(9)
print(c.area())