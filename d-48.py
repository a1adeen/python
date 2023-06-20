# global and local variable 

# global variable
x = 9 



def hello(lol):
    # local variable
    x = 8
    print(f"local variable of x ix {x}")
    hey =  (f"hello {lol}")
    print(hey)

hello('aladeen')

print(f"global variable of x is {x}")

print(x)




# changing global variabal 


global_var = 8

def teri(ko):
    global global_var
    global_var = 0
    prin = (f"hello {ko}")
    print(prin)

teri("aladeen")    