# coding: utf-8

"""
 Created by liuying on 2018/9/13.
"""

from collections import abc

a = [1, 2]
c = a + [3, 4]

if __name__ == '__main__':
    print(c)
    a += (1, 2)
    print(a)
    a.extend(range(3))
    print(a)
    a.append([1, 2])
    print(a)
