# by luffycity.com

import time

def cal_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print("%s running time: %s secs." % (func.__name__, t2-t1))
        return result
    return wrapper

@cal_time
def binary_search(li, val):
    low = 0
    high = len(li) - 1
    while low <= high:
        mid = (low + high) // 2
        if li[mid] > val:
            high = mid - 1
        elif li[mid] < val:
            low = mid + 1
        else:
            return mid
    else:
        return None

@cal_time
def linear_search(li, val):
    try:
        i = li.index(val)
        return i
    except:
        return None


li = list(range(0, 10000000, 2))
print(binary_search(li, 9000006))
print(linear_search(li, 9000006))
