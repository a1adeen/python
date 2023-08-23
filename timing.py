import time
import timeit

def func_1(n):
    new_list = []
    for num in range(n):
        new_list.append((num))
    return new_list
#
hey = func_1(10)
print(hey)


def func_2(m):
    return list(map(str, range(m)))

hey_2 = func_2(10)
print(hey_2)


# thats how we can calculate how time is taken by the compilar to give the output
# current_time
start_time = time.time()
# running code
result = func_1(100)
print(result)
# time after the execution of the code
end_time = time.time()
# time taken to execute
eplapsed_time = start_time - end_time
print(eplapsed_time)



# timeit

stm = '''
func_1(100)
'''
setp = '''
def func_1(n):
    new_list = []
    for num in range(n):
        new_list.append((num))
    return new_list
#
'''
print(timeit.timeit(stm , setp , number=1000))

# %%timeit
