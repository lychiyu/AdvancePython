# coding: utf-8

"""
 Created by liuying on 2018/9/14.
"""

"""
bisect 模块是用来处理已排序的序列，用来维持一排序的序列，升序
"""

import bisect

li = []

bisect.insort(li, 3)
bisect.insort(li, 2)
bisect.insort(li, 5)
bisect.insort(li, 1)
bisect.insort(li, 6)

# 应该插入的位置
print(bisect.bisect(li, 3))
print(li)
