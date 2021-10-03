# 编写一个程序，他以球体的半径（浮点数）作为输入，并且输出球体的直径、大圆周长、表面积和体积

# 这里采用面向对象编程思想
from math import *


class Ball:
    def __init__(self, radius=None):
        if radius is None:
            radius = 1
        self.radius = radius
        self.diameter = 2 * radius
        self.perimeter = pi * self.diameter
        self.superficial_area = 4 * pi * (radius ** 2)
        self.volume = 4 * pi * (radius ** 3) / 3

    def __str__(self):
        return 'this is a ball,it has {} radius,{} diameter,{} perimeter,{} superficial area,{} volume.'.format(
            self.radius, self.diameter, self.perimeter, self.superficial_area, self.volume)


if __name__ == '__main__':
    a = input('please input a ball\'s radius that you want(but if you input a string,we let radius=1):')
    # 处理字符串
    try:
        a = float(a)
    except ValueError:
        a = None
    ball = Ball(a)
    print(ball)
