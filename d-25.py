# operaters in tuples


# to make 1 tuple using 2 tuple

tup1 = (23,252,526,7)
tup2 = ("hey","nononon")
tup3 = tup1 + tup2
print(tup3)


# to check how many times a element occurs in an tuple
hey = (342,4,22,2,2,2,2,2,2,434343)
res = hey.count(2)
print(f"its occurs {res} times in a tuple")

# to know at which place an item comes at which position
# !not working
# k = (342,4,22,2,2,2,2,2,2,434343)
# rst = k.index(4 , 0, 5)
# print(f"it comes at {k} in this tuple")