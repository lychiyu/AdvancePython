# coding: utf-8

"""
 Created by liuying on 2018/9/15.
"""


# 生成器函数，只要有yield关键字的函数

def gen_func():
    yield 1
    yield 2


def gen_fib(index):
    n, a, b = 0, 0, 1
    while n < index:
        yield b
        a, b = b, a + b
        n += 1


if __name__ == '__main__':
    # 返回的是一个生成器对象，在python编译字节码的时候就产生了
    gen = gen_func()
    for value in gen:
        print(value)
    print(gen)

    for i in gen_fib(10):
        print(i)
