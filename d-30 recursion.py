# recursion 
# factorial of (0)= 1


# factorial of (n) = n * factorial(n-1)



# factorial function
# ex
def  factorial(n):
    if (n == 0  or n == 1):
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(3))    
print(factorial(5))
print(factorial(0))


# fibonacci sequence
# f0 = 0
# f1  = 1
# f2 = f1 + f0 
# f(n) = f(n-1) + f(n-2)


def fibonacci(f):
    if ( f == 0 ):
        return 0 
    elif(f == 1):
        return 1
    else:
     return

print(fibonacci(4))        