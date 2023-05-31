# default functions

# def your_name(a="ishant",b = "aladeen"):
#     print(f"your name is {a} and your last name is {b}")

# your_name("aladeen","don")    

def average(*numbers):
 sum = 0
 for i in numbers:
    sum = sum +1
    return sum / len(numbers)
  
a = average(23,2,342,5,32,32,32,34,23)
print(a)