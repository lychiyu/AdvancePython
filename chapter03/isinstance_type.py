# coding: utf-8

"""
 Created by liuying on 2018/9/12.
"""


class A:
    pass


class B(A):
    pass


b = B()

print(isinstance(b, B))
print(isinstance(b, A))

print(type(b))
print(type(b) is B)
print(type(b) is A)

