
class My:
    def __init__(self, v):
      print("activated")
      self.value = v
    def how(self):
          print(f"this is the vaLUE OF {self.value}")
    @property
    def ten_value(self):
        return 10 * self.value
    @ten_value.setter
    def ten_value(self,new_value):
        self._value = new_value/10

h =My(1)
h.how()

























class Hey:
    def __init__(self , k ):
        self._kal = k

    def show_me(self):
        print(f"{self._kal} is the value ")

    @property
    def x_show_me(self):
     return 10 * self._kal
    @x_show_me.setter
    def x_show_me(self , new):
        self._new = self._kal / 10



obj = Hey(100)
obj.x_show_me = 10
print(obj.x_show_me)