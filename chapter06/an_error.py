# coding: utf-8

"""
 Created by liuying on 2018/9/15.
"""


def add(a, b):
    a += b
    return a


if __name__ == '__main__':
    a = 1
    b = 2

    a = [1, 2]
    b = [3, 4]

    a = (1, 2)
    b = (3, 4)

    rlt = add(a, b)
    print(a, b)
    print(rlt)
