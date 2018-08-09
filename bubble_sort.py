# by luffycity.com

from cal_time import cal_time

@cal_time
def bubble_sort(li):
    for i in range(0, len(li)-1):
        # i表示第i趟 有序区有i个数
        for j in range(0, len(li)-i-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]

@cal_time
def bubble_sort_2(li):
    for i in range(0, len(li)-1):
        # i表示第i趟 有序区有i个数
        exchange = False
        for j in range(0, len(li)-i-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
                exchange = True
        if not exchange:
            return

import random

li = list(range(10000))
#random.shuffle(li)
bubble_sort_2(li)
print(li)