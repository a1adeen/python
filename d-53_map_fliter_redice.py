def cube(x):
     return x * x * x


# # trying to apply an fucntion in for loop for list
l = [2,4,56,6]
# new_l = []
# for i in l:
#     new_l.append(cube(i))
#     print(new_l)
# # this is an loop fucntion




# now we will use maping
new_l2 = list(map(cube, l))
print(new_l2)



# # another example
#
# def double(d):
#      return d * 2
#
#
# lis = [ 1,4,35,54]
# new_list = list(map(double,lis))
# print(new_list)
# # this is maping mehtod
#
#
#
#
#
# def quadra(q):
#      return q* q * q* q
# list_2 = [ 1122323,245435]
# ne_lis = []
# for i in list_2:
#      ne_lis.append(quadra(i))
#      print(ne_lis)
#



#filter
nai = [1,2,3,3,56,7]

def filter_small(l):
     return l < 10

nai_lis = list(filter(filter_small,nai))
print((nai_lis))



# reduce




from functools import reduce
def sum( x , y ):
     return x + y

he = ["h", "e" , "l", "l", "0"]
helo = reduce(sum , he)

