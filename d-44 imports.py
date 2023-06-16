# working of import in pyhon
# methods of importing 

# 1st case == in this we import as whole 
# ex:
import math
import pandas

result = math.sqrt(9)
print(result)

# 2nd case
# ex:
from math import sqrt
ans = sqrt(10)
print(ans)

# 3rd case
# here we can give a value to a function 
from math import pi as p
pii = 5 * p
print(pii)

print(dir(math))
print(dir(pandas))

# here i imported all the function that i made in for_importing
from for_importing import *
next_num(10)
