# keywords in python 
def func_1():
  try:
   list = [1,1,32,3,5]
   i = (input("inter the index here "))
   print(list[i])
  except:
    print("there is some error")
  finally:
    print("this will always be printed")

x = func_1()
print(x)    
