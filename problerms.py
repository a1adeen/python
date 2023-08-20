# print(20*5/2**2+75.50-0.25)1st
print(type(8.5))

hey = 'hello'
print(hey[4])
print(hey[-1])

list = [0,0,0]
print(list)
#
for i in range(3):
    creat_list = []
    creat_list.append(0)

# print([0]*3)


list = [5,3,4,6,1]
print(sorted(list))
#
# d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
# print(d['k1'][])

d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2][0])