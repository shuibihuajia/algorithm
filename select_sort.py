# by luffycity.com

from cal_time import cal_time

@cal_time
def select_sort(li):
    for i in range(len(li)-1):
        # 第i趟：有序区li[0:i] 无序区li[i:n]
        min_loc = i
        for j in range(i+1, len(li)):
            if li[min_loc] > li[j]:
                min_loc = j
        li[min_loc], li[i] = li[i], li[min_loc]

import random
li=[2,3,4,1,6,77,23,8]
# li = list(range(10000))
random.shuffle(li)
select_sort(li)
print(li)