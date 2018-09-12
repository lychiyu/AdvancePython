# coding: utf-8

"""
 Created by liuying on 2018/9/12.
"""


class A:
    # 类变量
    c = 1

    def __init__(self, x, y):
        # 对象变量
        self.x = x
        self.y = y


a = A('x', 'y')

print(a.x, a.y, a.c)
print(A.c)

A.c = 'C'

print('类修改')
print(a.x, a.y, a.c)
print(A.c)

# 这里会在实例a中创建一个对象变量c值是100
a.c = 100
print('对象修改')
print(a.x, a.y, a.c)
print(A.c)
