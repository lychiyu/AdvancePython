# coding: utf-8

"""
 Created by liuying on 2018/9/12.
"""
"""
python中一切皆是对象

函数和类也是对象，属于python的一等公民
"""

def ask(name='lychiyu func'):
    print(name)


class Person:
    def __init__(self):
        print('lychiyu class')


obj_list = []
obj_list.append(ask)
obj_list.append(Person)

for obj in obj_list:
    print(obj())


def decorator_func():
    print('decorator_func')
    return ask


my_func = ask
my_func()

my_class = Person
my_class()

decorator_ask = decorator_func()
decorator_ask('decorator_ask lychiyu')
