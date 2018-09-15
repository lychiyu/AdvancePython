# coding: utf-8

"""
 Created by liuying on 2018/9/15.
"""

"""
属性描述符: 自定义一个类，只只需要实现 get set delete 三个魔法函数中的任意一个就是 属性描述符
"""

import datetime


class CharField:
    # 数据属性描述符
    def __get__(self, instance, owner):
        return self.item

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError('str value need')
        self.item = value

    def __delete__(self, instance):
        pass


class NoDateField:
    # 非数据属性描述符
    def __get__(self, instance, owner):
        pass

class UserModel:
    name = CharField()


class User:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        self._age = 0

    @property
    def age(self):
        return datetime.datetime.now().year - self.birthday.year

    @age.setter
    def age(self, value):
        self._age = value

    def __getattr__(self, item):
        print(f'__getattr__ {item}')
        return item

    def __getattribute__(self, item):
        print(f'__getattribute__ {item}')
        return item


if __name__ == '__main__':
    # user = User('lychiyu', datetime.date(1996, 12, 29))
    # print(user.age)
    # user.age = 20
    # print(user.age)
    user = UserModel()
    user.name = '11'
    print(user.name)
