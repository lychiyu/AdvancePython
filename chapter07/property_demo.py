# coding: utf-8

"""
 Created by liuying on 2018/9/15.
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


if __name__ == '__main__':
    user = User('lychiyu', datetime.date(1996, 12, 29))
    print(user.age)
    user.age = 20
    print(user.age)
