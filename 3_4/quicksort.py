def swap(l, i, j):  # 可以直接使用 l[i], l[j] = l[j], l[i]
    temp = l[i]
    l[i] = l[j]
    l[j] = temp


def quicksort(l):
    quicksort_helper(l, 0, len(l) - 1)


def quicksort_helper(l, left, right):
    pivot_location = partition(l, left, right)
    quicksort_helper(l, left, pivot_location - 1)
    quicksort_helper(l, pivot_location + 1, right)


def partition(l, left, right):
    # 找到pivot，交换它与最右项
    middle = (left + right) // 2
    pivot = l[middle]
    l[middle] = l[right]
    l[right] = pivot
    # 在最左项前设置边界
    boundary = left
    # 把比基准点小的项移动到边界左边
    for index in range(left, right):
        if l[index] < pivot:
            swap(l, index, boundary)
            boundary += 1
    # 交换基准点和边界
    swap(l, right, boundary)
    return boundary


import random


def main(size=20):
    l = [random.randint(1, size + 1) for _ in range(size)]
    l = []
    for count in range(size):
        l.append(random.randint(1, size + 1))
    print(l)
    quicksort(l)
    print(l)


if __name__ == '__main__':
    import sys

    sys.setrecursionlimit(9000000)  # 这里设置大一些
    main()
