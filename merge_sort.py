# by luffycity.com

def merge(li, low, mid, high):
    i = low
    j = mid + 1
    li_tmp = []
    while i <= mid and j <= high:
        if li[i] < li[j]:
            li_tmp.append(li[i])
            i += 1
        else:
            li_tmp.append(li[j])
            j += 1
    while i <= mid:
        li_tmp.append(li[i])
        i += 1
    while j <= high:
        li_tmp.append(li[j])
        j += 1
    for i in range(low, high+1):
        li[i] = li_tmp[i-low]


def merge_sort(li, low, high):
    if low < high:  # 至少两个元素
        mid = (low + high) // 2
        print(li[low:mid + 1], li[mid + 1:high + 1])
        merge_sort(li, low, mid)
        merge_sort(li, mid+1, high)
        print(li[low:mid+1], li[mid+1:high+1])
        merge(li, low, mid, high)
        print(li[low:high + 1])

li = [10,4,6,3,8,2,5,7]
merge_sort(li, 0, len(li)-1)