'''
    测试程序的迭代次数
'''


class Count:
    def __init__(self, p):
        self.problemSize = p
        self.count = 0

    def use(self):
        while self.problemSize > 0:
            self.problemSize //= 2
            self.count += 1


if __name__ == '__main__':
    problemSize = float(input())
    p = Count(problemSize)
    p.use()
    print(p.count)
