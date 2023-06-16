def exceeding(n):
 num = (n+1)
 if (n == ""):
  raise ValueError("strings are not allowed")
 else:
  return(num)
exceeding(8) 



def mean_calc(a ,b):
 mean = ((a * b)/(a + b))
 if (mean == 0):
  print("value is 0")
 else:
  print(mean)

# mean_calc(1,3)  

def next_num(n):
 num = (n + 3)
 if(num == ""):
  raise ValueError("strings are not allowed")
 else:
  return(num)
 

print(next_num(10) )