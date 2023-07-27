# generators
def gen():
    for i in range(5):
        yield i

# to run the genetor we have to print(next())
hey = gen()
print(next(hey))
print(next(hey))
# this stores all the value of the function



# ex:
def cube(n):
    result = []
    for i in range(n):
        result.append(i**3)
    return result

num = cube(10)
print(num)


# using yeild
def hey(j):
    for h in range(j):
        yield h ** 2

print(list(hey(8)))



# finonacci number
def fibnaaci(i):
    a = 0
    b = 1
    for ish in range(i):
        yield a
        a,b = b, a+b

for nu in fibnaaci(15):
    print(nu)

# print(len(nu))