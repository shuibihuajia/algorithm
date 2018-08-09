# by luffycity.com

from cal_time import cal_time

def sift(li, low, high):
    tmp = li[low] # 原省长
    i = low
    j = 2 * i + 1
    while j <= high:    # 第二种跳出条件： j > high
        if j < high and li[j+1] > li[j]: # 如果右孩子存在并且大于左孩子
            j += 1
        if tmp < li[j]:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:   # 第一种跳出条件：li[j] <= tmp
            break
    li[i] = tmp

@cal_time
def heap_sort(li):
    n = len(li)
    # 1. 建堆
    for i in range(n // 2 - 1, -1, -1): # 最后一个非叶子节点的位置是n//2-1
        sift(li, i, n-1)
    # 2. 挨个出数
    for i in range(n-1, -1, -1): # i 表示此时堆的high位置
        li[0], li[i] = li[i], li[0] # 退休+棋子
        sift(li, 0, i-1)

import random


li = list(range(100000))
random.shuffle(li)
heap_sort(li)
print(li)
