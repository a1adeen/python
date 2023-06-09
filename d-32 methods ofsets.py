# method in sets
set1 = { 1,2,3,4,3}
set2 = {5,6,4,6,9}
# union of sat 1 and 2 
print(set1.union(set2))


# to add value from other set
set1.update(set2)
print(set1)



# to print seperatly 
print(set1,set2)



# intersection in 2 sets
set_1 = {"delhi", "haryana","kanpur"}
set_2 = {"banglore" , "delhi", "bengal"}
set_3 = set_1.intersection(set_2)
print(set_3)


# to take diffrence
set_4 =   set_1.symmetric_difference(set_2)
print(set_4)



# isdisjoitn sets 
# 2 sets which do not have any same element 
# to check if sets are dijoint or not  


set_1 = {"delhi1", "haryana","kanpur"}
set_2 = {"banglore" , "delhi", "bengal"}
set_5 = set_1.isdisjoint(set_2)
print(set_5)
# yes this set id dijoint


# superset in sets
# super_set is set which is the part of the other like it has the all elements which are already included in the other set
# ex = set_1 = {1,2,3,4,5,6,7,8}
#      set_2 = { 2,3,4,6}
# see there set_2 is the subset of set_1


set_12 = {"delhi1", "haryana","kanpur","delhi","banglore","bengal"}
set_22 = {"banglore" , "delhi", "bengal"}

set_34 = set_12.issuperset(set_22)
print(set_34)

# to whether the set is the subset or not 
set_35 = set_22.issubset(set_12)
print(set_35)



# to add an items in a set 
add_set = {1,2,3}
add_set.add(5)
print(add_set)
   

#    or 
added_set = {12,34}
add_set.update(added_set)
print(add_set)


# to remove an item from the set 

add_set.remove(34)
print(add_set)


    #  or  
    # here we can use discard instead of remove because it will not throw an error even if we appeal to remove an item which is not even in a set 
# ex:
add_set.discard(99)    
print(add_set)
# this will not throw an error


# to pop an element
# it is use to pick up an random element form the set

pop_set = {"delhi1", "haryana","kanpur","delhi","banglore","bengal"}
item = pop_set.pop()
print(item)

# to delete an entire set 
del_set = {1,2,2,4,54,5,5656}
del del_set
# now del_set is deleted now if we try to prin tit it will throw an error
# print(del_set)
# # !this is throwing an error


# to check wheter the set contain an element or not 

checking = {1,13,345,7}
if 13 in checking:
    print("yes it is included in an set ") 
else:
    print("this set doesn't contains that element that u wants")    