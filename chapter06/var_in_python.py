# coding: utf-8

"""
 Created by liuying on 2018/9/15.
"""

"""
python中的变量是一个指针，大小一样
"""

# 在内存空间申请一个int大小的空间===>先生成int对象
# 在把a这个标记贴到1上面====>再进行分配
a = 1

b = [1, 2, 3]
a = b
b.append(4)
print(a)
print(a is b)

print(id(a), id(b))
