def greet(fx):
    def mfx():
        print("good morning")
        fx() 
        print("thanks for using this function")
    print(mfx)

def entry():
    name = (input("hey what's your name :"))
    age = (int(input("whats your age :")))
    print(f"your welcome {name}")

entry()    