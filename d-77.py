# # operater overloading
# class   Vector:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#     def __str__(self):
#         return f"{self.a}a + {self.b}b + {self.c}c"
#     def __add__(self , x):
#         return Vector(f"{self.a + self.a}a + {self.b + self.b}b + {self.c + self.c}c")
#
#
# sum_1 = Vector(1 ,2,3)
# sum_2 = Vector(4,4,5)
# print(sum_1)
# print(sum_2)
# print(sum_1 + sum_2)


# for addtion only
class Vector:

    def input_1(self ,a , b, c):

        self.a = a
        self.b = b
        self.c = c

    def show1(self):
        print("this is equation 1")


    def input_2( self ,i , j, k):
        self.i = i
        self.j = j
        self.k = k
    def show2(self):
        print("this is equation 2")

    def add(self):
        return f"{self.a + self.i}x {self.b + self.j}y {self.c + self.k}z "

# vol_1 = Vector.__init_subclass__(1 , 3, 5)
# vol_2 = Vector.input_1(1 , 4, 9)
vol_1 = Vector.input_2(3, 9 ,5)
vol_1.show2