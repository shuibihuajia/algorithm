# by luffycity.com
# def func4(n):
#     if n > 0:
#         func4(n-1)
#         print(n)
#
# def text(n):
#     if n > 0:
#         print("抱着",end='')
#         text(n-1)
#         print("的我", end='')
#     else:
#         print("我的小鲤鱼",end='')
#
# text(5)

def hanoi(n, A, B, C):
    if n > 0:
        # n个盘子从A经过B移动到C
        hanoi(n-1, A, C, B)
        print("%s->%s" % (A, C))
        hanoi(n-1, B, A, C)

hanoi(4, "A", "B", "C")