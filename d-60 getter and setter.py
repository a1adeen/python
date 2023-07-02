
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


