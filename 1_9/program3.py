# 一个球的弹跳性是0.6，第一次着地前的最高高度和第二次着地前的最高高度之比
# 给定初始下降高度和允许弹跳次数，输出总的运动距离
Degree = 0.6


class BallDistance:
    def __init__(self, initial_hight, times):
        distance = initial_hight * (1 + Degree)
        self.distance = 0
        for i in range(times):
            self.distance = distance + self.distance
            distance = distance * Degree

    def __str__(self):
        return '总距离{}'.format(self.distance)


if __name__ == '__main__':
    h = float(input())
    t = int(input())
    print(BallDistance(h, t))
