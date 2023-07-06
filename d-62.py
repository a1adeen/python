# acess modifiers
class Emp:
    def __init__(self):
        self.__name = "ishant"

a = Emp()
# from this way we can't acess the def
# print(a.__name)
print(a._Emp__name)


class Student:
#     def __init__(self):
#         self._hi_3 = 34
    def __init__(self):
        self._game_name = "aladeen"
    def _hey(self):
        return "hey"



obj = Student()
print(obj._game_name)
print(obj._hey())
# print(obj._hi_3)