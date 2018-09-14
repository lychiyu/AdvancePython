# coding: utf-8

"""
 Created by liuying on 2018/9/14.
"""

# 列表生成器，性能是高于列表操作的

li = [i for i in range(21) if i % 2 == 1]
print(li, type(li))


# 生成器表达式
li = (i for i in range(21) if i % 2 == 1)
print(li, type(li))

for i in li:
    print(i)

# 字典推导式
d = {}