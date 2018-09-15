# coding: utf-8

"""
 Created by liuying on 2018/9/15.
"""

from collections.abc import Iterable, Iterator

a = [1, 2]
# 可迭代类型 True
print(isinstance(a, Iterable))

# 迭代器 False
print(isinstance(a, Iterator))
iter_rator = iter(a)

# 迭代器 True
print(isinstance(iter_rator, Iterator))
