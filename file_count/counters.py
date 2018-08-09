# from collections import Counter
#
# c=Counter()
# with open("a.txt","r",encoding="utf-8") as f:
#     for i in f.readlines():
#         word = i.split()
#         c1 = Counter(word)
#         c.update(c1)
# print(c.most_common(10))
# print(__file__)
# print(__name__)

# class Parent(object):
#     x=222
#     pass
#
# if hasattr(Parent,'x'):
#     print(getattr(Parent,'x'))
#     setattr(Parent,'x',3)
#     print(getattr(Parent,'x'))

# d=dict(a=3,b=4,mm=33)
# def reverse_lookup(d,v):
#     for k in d:
#         if d[k]== v:
#             return k
#     raise LookupError()
# reverse_lookup(d,333)

import functools
def cal_time(fn):
    @ functools.wraps()
    def inner(*args,**kwargs):
        import time
        start = time.time()
        fn(*args,**kwargs)
        end = time.time()
        use_time = end - start
        return f"run {fn.__name__} use time {use_time}s"
    return inner

@cal_time
def buble_sort(li):
    for i in range(len(li)-1):
        for j in range(len(li)-1-i):
            if li[j]>li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]
    return li

import random
li1 = list(range(1000))
random.shuffle(li1)

res=buble_sort(li1)
print(res)



