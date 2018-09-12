# coding: utf-8

"""
 Created by liuying on 2018/9/12.
"""
"""
抽象基类：abc模块
python是动态语言，变量是没有类型的，在python中变量其实就是一个符号而已，是可以指向任何类型的对象
"""
import abc
from collections.abc import Sized


class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __iter__(self):
        pass

    def __getitem__(self, item):
        return self.employee[item]

    def __len__(self):
        return len(self.employee)


company = Company(['ly', 'liuying', 'lychiyu'])
# 需要判断对象的类型时可以使用抽象基类
print(isinstance(company, Sized))
print(len(company))


# 需要强制某个子类必须实现某些方法

# 模拟一下抽象基类
class CacheBase():
    def get(self, key):
        raise NotImplementedError

    def set(self, key, value):
        raise NotImplementedError


class RedisCatche(CacheBase):
    def set(self, key, value):
        pass


redis_cache = RedisCatche()
# 这样只是在调用没有重写的方法是才会报错
redis_cache.get('k')


# 使用abc实现抽象基类
class CacheBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get(self, key):
        pass

    @abc.abstractmethod
    def set(self, key, value):
        pass


class RedisCatche(CacheBase):
    def set(self, key, value):
        pass


# 这样在子类实例化是就会报错
redis_cache = RedisCatche()
redis_cache.get('k')
