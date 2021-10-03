import numpy as np


# def square(x):
#     return x ** 2
#
#
# a = np.array(list(map(square, [2, 4, 5, 7, 10])))
# a = [i for i in a if i > 23]
# print(a)


def sum_odd(a,b):
    a=int(a)
    b=int(b)
    S:int = 0
    if a<b:
        while a <= b:
            if a % 2 == 1:
                S += a
            a += 1
        return S
...
c = sum_odd(5,34)
print(c)
