# coding: utf-8

"""
 Created by liuying on 2018/9/14.
"""

from collections.abc import Mapping, MutableMapping

# dict 是属于 Mapping类型
# MutableMapping --> Mapping --> Collection

a = {}

print(isinstance(a, Mapping))
print(isinstance(a, MutableMapping))
