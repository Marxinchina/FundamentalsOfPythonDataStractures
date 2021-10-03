# 假设一个列表在索引0到9的位置上，包含了值20、44、48、55、66、74、88、93、99。
# 用二叉搜索法搜索目标值90，记录搜索左边、右边和中间点的值。对于目标值44重复这个过程
D = [20, 44, 48, 55, 66, 74, 88, 93, 99]


class BinarySearch:
    def __init__(self):
        self.left = []
        self.right = []
        self.mid = []

    def search(self, list_sorted, n):
        left_point = 0
        right_point = len(list_sorted) - 1
        while left_point <= right_point:
            mid_point = (left_point + right_point) // 2
            self.mid.append(list_sorted[mid_point])
            self.left.append(list_sorted[left_point])
            self.right.append(list_sorted[right_point])

            if list_sorted[mid_point] > n:
                right_point = mid_point - 1
            elif list_sorted[mid_point] == n:
                return list_sorted[mid_point]
            else:
                left_point = mid_point + 1


if __name__ == '__main__':
    b = BinarySearch()
    print(b.search(D, 90))
    print(b.right)
    print(b.left)
    print(b.mid)
    b1 = BinarySearch()
    print(b1.search(D, 44))
    print(b1.right)
    print(b1.left)
    print(b1.mid)
