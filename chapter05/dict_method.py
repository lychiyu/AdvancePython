# coding: utf-8

"""
 Created by liuying on 2018/9/14.
"""

a = {
    'ly': {'name': 'lychiyu', 'city': 'sz'},
    'liuying': {'name': 'liuying', 'city': 'nc'},
}

a.clear()

print(a)

a = {
    'ly': {'name': 'lychiyu', 'city': 'sz'},
    'liuying': {'name': 'liuying', 'city': 'nc'},
}
b = a.copy()  # 浅拷贝
print(a, b)

b['liuying']['name'] = 'lll'
print(a, b)
