# coding: utf-8

"""
 Created by liuying on 2018/9/15.
"""

"""
__getattribute__ 访问属性时便会访问
__getattr__ 在查找不到属性的时候调用
"""
import datetime


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
    user = User('lychiyu', datetime.date(1996, 12, 29))
    print(user.age)
    user.age = 20
    print(user.age)

