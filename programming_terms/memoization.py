"""
Memoization:
    is an optimization technique used primarily to speed up computer programs by storing the result of expensive function calls and returning the cached result when the same input occurs again.
"""

expensive_func_cache = {}

import time

def expensive_fun(num):
    if num in expensive_func_cache:
        return expensive_func_cache[num]
    
    print("computing...{}".format(num))
    time.sleep(1)
    result = num*num
    expensive_func_cache[num] = result
    return result


result = expensive_fun(4)
print(result)

result = expensive_fun(15)
print(result)

result = expensive_fun(200)
print(result)

result = expensive_fun(110)
print(result)


result = expensive_fun(4)
print(result)

result = expensive_fun(15)
print(result)

result = expensive_fun(200)
print(result)

result = expensive_fun(110)
print(result)