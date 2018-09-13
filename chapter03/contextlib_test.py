# coding: utf-8

"""
 Created by liuying on 2018/9/13.
"""

import contextlib


@contextlib.contextmanager  # 这个装饰器必须修饰一个生成器, 将一个函数变为上下文管理器
def file_open(file_name):
    print('file open')  # 理解为enter
    yield {}
    print('file end')  # 理解为exit


if __name__ == '__main__':
    # 使用contextlib来简化上下文管理器
    with file_open('111.txt') as f:
        print('file process')
