
# normal function

def double(x):
     return x * 2

print(double(2))




# lambda fucntion:

triple = lambda x: x * 3
print(triple(2))


# cube function using lambda
cube = lambda c : c * c * c
print(cube(2))


# avg calculating function

avg = lambda x, y: (x + y)/2
print(avg(2,2))


# using def function
def avgr( h ,y ):
    return (h + y)/2

print(avgr(5,3))



# adding function in function
four_time = lambda  four: four * 4
def adding(fx, value):
    return 6 + fx(value)


print(adding(four_time,1))


# practice code
# def greeting(name):
#     naam = (input("your name here :"))
#     return  f"your welcome {naam}"
#
#
#
# print(greeting("aladen"))