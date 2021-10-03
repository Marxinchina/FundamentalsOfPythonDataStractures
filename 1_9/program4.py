# 德国数学家Gottfried Leibniz 为求取Π的近似值开发了如下的方法：
# \pi/4 = 1 - 1/3 + 1/5 - 1/7 + ···
# 编写一个程序，让用户指定在这种近似方法中使用迭代的次数，并且显示最终的结果。

class GetPi:
    def __init__(self,inter_times):
        pi_quarter = 0
        for i in range(inter_times):
            pi_quarter = pi_quarter + ((-1) ** i) * (1/(2 * i + 1))
        self.value = pi_quarter * 4

    def __str__(self):
        return '{}'.format(self.value)


if __name__ == '__main__':
    times = int(input('你想获取迭代多少次的结果：'))
    print(GetPi(times))