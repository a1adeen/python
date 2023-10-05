
list1 = []
list2 = [0]

def func(x , y ):
    x.extend(y)
    new = x
    new.sort()
    return new

hey = func(list1 , list2)
print(hey)