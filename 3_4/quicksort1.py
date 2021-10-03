def partition(arr, low, high):
    i = (low - 1)  # 最小元素索引
    pivot = arr[high]

    for j in range(low, high):

        # 当前元素小于或等于 pivot
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# arr[] --> 排序数组
# low  --> 起始索引
# high  --> 结束索引

# 快速排序函数
def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

import random


def main(size=20):
    # l = [random.randint(1, size + 1) for _ in range(size)]
    l = []
    for count in range(size):
        l.append(random.randint(1, size + 1))
    print(l)
    quicksort(l,0, size - 1)
    print(l)


if __name__ == '__main__':
    import sys

    sys.setrecursionlimit(9000000)  # 这里设置大一些
    main()
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    quicksort(arr, 0, n - 1)
    print("排序后的数组:")

    print(arr)
