# hybrid and hiearchical inheritance


# hybrid inheritance
class One:
    pass
class Two(One):
    pass
class Three(One):
    pass
class mixed(Two , Three):
    pass



# hiearchical inheritance
class Parent:
    pass
class Child(Parent):
    pass
class Child_2(Parent):
    pass