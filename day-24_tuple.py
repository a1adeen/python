# def calculate_mean(a ,b):
#     mean = ((a*b)/(a +b))
#     if(mean == 0):
#         print("numbers are invalid")
#     elif(mean<10):
#         print("mean is under 10")
#     else:
#         print(f"your mean is {mean}")
#     print(mean)
# calculate_mean(8, 20)


# # invoice_function 

# def invoice_function(name , due, date):
#     print(f"{name} your due of {due}will expire on {date}")

# invoice_function("ishnat", 900, 1092091)    





# !tuples starts from here

tup = (1,4,"hey")
print(type(tup))
print(tup)

# tuples can't be edited with indexing == it will throw an error
# example

# lup = (34,3,66,36)
# lup[0]= 90
# print(lup)

# tuple can be indexed only for printing single Value
ney = (23,5,23563,46346)
print(ney[0])
print(ney[-1])
if 122 in ney:
    print("yes ney consist 122")