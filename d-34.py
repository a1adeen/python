# dicctionary methods 
# to add items of 1 dictionary to another
ep_1 = {
    1 : "aladeen_1",
    2 : "aladeen_2",
    3 : "aladeen_3"
}
ep_2 = {
    4 : "aladeen_4",
    5 : "aladeen_5"
}
ep_1.update(ep_2)
print(ep_1)

# to clear a whole dictionary 
clear = {
    1 : 'jfs',
    2 : 'fasfasfd'
}

clear.clear()
print(clear)

# to remove the last item from the dicitonary 

dic = {
    4 : 'hey',
    1 : "aladeen_1",
    2 : "aladeen_2",
    3 : "aladeen_3"
}

dic.popitem()
print(dic)

# to delte the specific item form the dictionary 
del_dic = {
    11 : "new",
    12 : "old",
    13 : "ggs"
 }
del del_dic[12]
print(del_dic)


# to merge 2 dictionary 


# fuction that merges two dictionaries
def merge_dif( x , y):
    z = x.copy()
    z.update(y)
    return z




# to merge two dictionaries 

a = {
    "a" : 'hey'
}
b = {
    "b" : "hey _2 "
}

i = merge_dif(a , b)
print(i)
