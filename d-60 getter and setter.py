
class My:
    def __init__(self, v):
      print("activated")
      self.value = v
    def how(self):
          print(f"this is the vaLUE OF {self.value}")
    @property
    def ten_value(self):
        return 10 * self.value

h =My(1)
h.how()


