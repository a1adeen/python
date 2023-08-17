import random

# print(dir(random))


# if we set a seed then we will get same output every time
# random.seed(1)
# random.seed(3)

def random_num():
   rng = random.Random(2)
   for i in range(5):

         listt =  rng.randint(1,100)
         print(listt)

random_num()
def randm_2():
    rnl = random.Random(1)
    for y in range(5):
        print(rnl.randint(1 , 15))
randm_2()

# list with random
mylist = list(range(0, 21))
print((mylist))
# to get the random number from thelist
print(random.choice(mylist))
# to get the multiple numbers from the list

# but in this we can get the same number twice
print(random.choices(population=mylist , k=9))
# to do not get the same number for twince
print(random.sample(population=mylist , k=9))