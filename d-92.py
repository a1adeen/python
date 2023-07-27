# function caching


# importing functool
import time
# import functools
from functools import lru_cache

@lru_cache(maxsize=None)
def fx(n):
    time.sleep(2)
    return n*2
# these value will be printed in 2sec
print(fx(2))
print(fx(44))
print(fx(9))
# these value value will be printed faster than previous
print(fx(2))
print(fx(44))
print(fx(9))
