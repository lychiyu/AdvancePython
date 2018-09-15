# coding: utf-8

"""
 Created by liuying on 2018/9/15.
"""


class User:
    def __new__(cls, *args, **kwargs):
        # __new__ 是在新式类中才有，可以自定义对象的生成过程
        print("__new__")
        return super().__new__(cls)

    def __init__(self, name):
        # __init__ 是用于完善对象的，如果__new__不返回对象，__init__便不会调用
        print("__init__")
        self.name = name


if __name__ == '__main__':
    user = User(name='lychiyu')
