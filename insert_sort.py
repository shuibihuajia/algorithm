# by luffycity.com

from cal_time import cal_time

@cal_time
def insert_sort(li):
    for i in range(1, len(li)):
        # i既表示趟数，也表示摸到的牌的下标
        j = i - 1
        tmp = li[i]
        while j >= 0 and li[j] > tmp:
            li[j+1] = li[j]
            j -= 1
        li[j+1] = tmp


import random

li = list(range(10000))
random.shuffle(li)
insert_sort(li)
print(li)