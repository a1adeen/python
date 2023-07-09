# static methods
# class Maths:
#     def __init__(self, num):
#         self.num = num
#
#     def adtono(self, n):
#         return self.num + n
#
#     # this function can be used anywhere
#     #     and this function is written inside the class because if the user import this class then user will also be provided with this funcion
#     @staticmethod
#     def add(a, b):
#         return a + b
#
#
# bey = Maths(9)
# # bey.adtono(8)
# print(bey.adtono(1))
# print(bey.add(1, 4))


# practice code
def math(fx):
    def mk(*arg, **kwargs):
        print("good morning")
        fx(*arg , **kwargs)
        print("thanks for using this funtion")
    return mk

@math
def greet():
    name = (input("hey whats ur name :"))
    age = int(input("whats ur age :"))
    if age <= 20:
        raise ValueError("invalid input")
    else:
        print("ur wwelcome")
@math
def intoto(a):
    print(a *  2)
def triple(i):
    return i * 3
 # greet()
# print(intoto(5))
print(triple(7))