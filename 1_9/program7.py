# 统计学家想要用一组函数计算一列数字的中位数（median）和众数（mode）。
# 中位数是将一个列表排序后出现在中间位置的数。还要包含一个名为mean的函数，
# 它计算一组数字的平均数。每个函数都接受数字的一个列表作为参数，并且返回一个单个的数字。


class Statistics:
    def __init__(self, num_list):
        self.list = num_list  # 数列
        self.len = len(self.list)  # 数列长度
        self.list_sorted = self.sort_list()  # 排好序的数列
        self.sum = self.summary()  # 数列的和
        self.num_dict = self.amount()  # 数列个数的频数

    def summary(self):
        '''

        :return: 数列的和
        '''
        sum = 0
        for l in self.list:
            sum = sum + l
        return sum

    def sort_list(self):
        '''

        :return: 排好序的数列（由小至大）
        '''
        l = self.list
        for i in range(self.len):
            for j in range(i):
                if l[i] < l[j]:
                    l[i], l[j] = l[j], l[i]
                else:
                    pass
        return l

    def median(self):
        '''

        :return: 数列的中位数
        '''
        if self.len % 2 == 0:
            return 0.5 * (self.list_sorted[int(self.len / 2)] + self.list_sorted[int(self.len / 2 - 1)])
        else:
            return self.list_sorted[int(self.len / 2 - 0.5)]

    def amount(self):
        d = dict()
        # ss = set(self.list)
        # print(ss)
        for l in self.list:
            if l in d.keys():
                d[l] = d[l] + 1
                # print('{}+if'.format(d.keys()))
            else:
                d[l] = 1
                # print('{}+else'.format(d.keys()))
        return d

    def mean(self):
        '''

        :return: 数列的均值
        '''
        return self.sum / self.len

    def mode(self):
        # size = len(self.num_dict)
        record = []
        l = 0
        # count = 0
        for n in self.num_dict:
            if self.num_dict[n] > l:
                l = self.num_dict[n]
                record = [n]
            elif self.num_dict[n] == l:
                record.append(n)
            else:
                pass
        return record


if __name__ == '__main__':
    num = input('请输入一组数字，用逗号隔开即可：').split(',')
    l = []
    for n in num:
        l.append(float(n))
    s = Statistics(l)
    print(s.mean())
    print(s.median())
    print(s.mode())
