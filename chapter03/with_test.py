# coding: utf-8

"""
 Created by liuying on 2018/9/13.
"""


class Sample:
    def __enter__(self):
        print('enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')

    def do_something(self):
        print("do_something")


# 上下文管理器
if __name__ == '__main__':
    with Sample() as sample:
        sample.do_something()
