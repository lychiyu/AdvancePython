# coding: utf-8

"""
 Created by liuying on 2018/9/15.
"""

import dis


def foo():
    bar()


def bar():
    pass


class Foo:
    name = 'bar'

    def __init__(self):
        pass


if __name__ == '__main__':
    print(dis.dis(foo))
    """
     10           0 LOAD_GLOBAL              0 (foo)    # 加载 名为foo的函数对象
                  2 CALL_FUNCTION            0          # 调用这个函数
                  4 POP_TOP                             # 从栈的顶端pop出
                  6 LOAD_CONST               0 (None)   # 加载函数执行后return的值没有return则为None
                  8 RETURN_VALUE                        # 返回return的值
    None
    """
