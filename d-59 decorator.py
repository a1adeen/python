def greet(fx):
    def mfx():
        print("good morning")
        fx()
        print("thanks for using this function")
    return mfx


@greet
def entry():
    name = (input("hey what's your name :"))
    age = (int(input("whats your age :")))
    print(f"your welcome {name}")

entry()





# practising
def welcome(fx):
    def mkj(*arg , ** kwargs):
        print("good morning")
        fx(*arg , **kwargs)
        print("thanks for using this fuction")
    return mkj


@welcome
def name():
    Name = (input("whats your name :"))
    print(f"{Name} your name has been registered")

name()


@welcome
def avg(a , b):
    avr = (a + b)/2
    print(avr)

avg(3 ,4)





