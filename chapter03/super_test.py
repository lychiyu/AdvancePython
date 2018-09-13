# coding: utf-8

"""
 Created by liuying on 2018/9/13.
"""


class A:
    def __init__(self):
        print('A')


class B(A):
    def __init__(self):
        print('B')
        # python2
        # super(B, self).__init__()
        # python3
        super().__init__()


class C(A):
    def __init__(self):
        print('C')
        super().__init__()


class D(B, C):
    def __init__(self):
        print('D')
        super().__init__()


if __name__ == '__main__':
    b = B()
    # super是根据mro来进行实现的
    print(D.__mro__)
    d = D()

