# ek hi function ek hi value ke liye kitna baar run krta h 
# import functools
from functools import lru_cache
import time
@lru_cache(maxsize=None)
def fx(n):
    # if n < 2:
    #     return n
    # return fib(n-1) + fib(n-2)
    time.sleep(5)
    return n*5

print(fx(20))
print("done for 20")
print(fx(6))
print("done for 6")
print(fx(2))
print("done for 2")
#yha tk 5 sec ke baad baad orint hoga but iske baad tutant 
#function alreddy memoize  memoization
print(fx(20))
print("done for 20")
print(fx(6))
print("done for 6")
print(fx(2))
print("done for 2")


 