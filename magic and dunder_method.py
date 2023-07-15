# magic and dunder method



# magic method


class Employeee:
    def __init__(self , name ):
        self.name = name
    # def __str__(self):
    #     return f"name of the employee is {self.name}"
    # this method will print if the the above method s commented
    def __repr__(self):
        return f"this mehtod is repr'previous mehtod is commented "
    # this method is used when we need to call the class
    def __call__(self):
        print("he how are you")

emo_1 = Employeee("aladeen")
print(emo_1)
# # to call both mehtod at the same time
# print(repr(emo_1))
# emo_1()