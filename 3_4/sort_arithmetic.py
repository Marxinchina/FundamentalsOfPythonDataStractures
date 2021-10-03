class Sort:
    @staticmethod
    def swap(l, i, j):  # 可以直接使用 l[i], l[j] = l[j], l[i]
        temp = l[i]
        l[i] = l[j]
        l[j] = temp

    def selection_sort(self, l):  # 选择排序，复杂度为O(n ** 2)
        point = 0  # 设定定位点
        while point < len(l) - 1:  # 最后一个元素不用排序
            min_index = point  # 假设定位点的值恰好足够小
            move_index = point + 1  # 设置探索点，遍历定位点的后面所有点
            while move_index < len(l):  # 最后一个元素也要参与比较
                if l[move_index] < l[min_index]:
                    min_index = move_index  # 如果找到更小的点，更新索引
                move_index += 1  # 没有就往下遍历
            if move_index != point:
                self.swap(l, min_index, point)  # 定位点不是最小的，就把最小的点与点位点交换
            point += 1  # 继续往下定位
        return l

    def bubble_sort(self, l):  # 冒泡排序
        n = len(l)
        while n > 1:
            swapped = False  # 没发生交换
            i = 1
            while i < n:
                if l[i] < l[i - 1]:  # 后面的数小，将两者交换
                    self.swap(l, i, i - 1)  # 发生交换
                    swapped = True
                i += 1  # 移动指针
            if not swapped:  # 没有发生交换，表明列表已排序，退出循环
                break
            n -= 1  # 移动指针
        return l

    @staticmethod
    def insert_sort(l):
        point = 1  # 这里是列表未排序部分第二项的索引
        while point < len(l):  # 从第二项到最后一项都要插入一次
            item_insert = l[point]  # 保存插入项的值
            compare_point = point - 1  # 初始比较项的索引
            while compare_point >= 0:  # 每比较一次就把指针往前挪，直到为负
                if item_insert < l[compare_point]:  # 如果插入项小，就交换两者的值
                    l[compare_point + 1] = l[compare_point]
                    compare_point -= 1  # 然后指针前移
                else:
                    break  # 因为前面都排好序，所以插入项比指针处的值大，不用往前比了
            l[compare_point + 1] = item_insert  # 指针前移前的值后移一位，空出来的位置填上插入值
            point += 1  # 下一个插入点
        return l

    def quick_sort(self, l):
        if len(l) > 1:
            pivot = l[0]
            left = [i for i in l[1:] if i <= pivot]
            right = [i for i in l[1:] if i > pivot]
            return self.quick_sort(left) + [pivot] + self.quick_sort(right)
        else:
            return l

    def merge_sort(self,l):
        pass


if __name__ == '__main__':
    l = [5, 4, 3, 2, 1]
    s = Sort()
    print(s.quick_sort(l))

