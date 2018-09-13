# coding: utf-8

"""
 Created by liuying on 2018/9/13.
"""
from chapter03.class_method import Date


class User:
    def __init__(self, birthday):
        self.__birthday = birthday
        self._birthday = birthday
        self.birthday = birthday

    def get_age(self):
        return 2018 - self.birthday.year


if __name__ == '__main__':
    user = User(Date(1996, 12, 29))
    print(user.get_age())
    print(user.birthday)
    print(user._birthday)
    # 双下划线私有属性， 只能在类里面的共有方法里访问  ==> _User__birthday
    print(user._User__birthday)
    print(user.__birthday)
