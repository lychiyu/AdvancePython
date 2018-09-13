# coding: utf-8

"""
 Created by liuying on 2018/9/12.
"""


class D:
    pass


class C(D):
    pass


class B(D):
    pass


class A(B, C):
    pass

# C3算法
print(A.__mro__)
