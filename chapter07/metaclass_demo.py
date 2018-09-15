# coding: utf-8

"""
 Created by liuying on 2018/9/15.
"""

"""
类是对象 type是创建类的类,
元类就是创建类的类
type-->class(对象)--->对象
"""


def create_class(name):
    if name == 'user':
        class User:
            def __str__(self):
                return 'user'

        return User
    elif name == 'company':
        class Company:
            def __str__(self):
                return 'company'

        return Company


def type_create_class(name, base, kwargs):
    return type(name, base, kwargs)


def say(self):
    return 'i am user'


"""
在python中类的实例化过程：
metaclass
"""


class MetaClass(type):
    def __new__(cls, *args, **kwargs):
        print('MetaClass')
        return super().__new__(cls, *args, **kwargs)


class User(metaclass=MetaClass):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'user'


if __name__ == '__main__':
    my_class = create_class('user')

    my_obj = my_class()
    print(my_obj)

    my_type_class = type_create_class('User', (), {'name': 'user', 'say': say})
    my_type_obj = my_type_class()
    print(type(my_type_obj))
    print(my_type_obj.name)
    print(my_type_obj.say())

    user = User('lychiyu')
    print(user)
