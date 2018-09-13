# coding: utf-8

"""
 Created by liuying on 2018/9/13.
"""
"""
python自省: 通过一定的机制查询到对象的内部结构
"""

# coding: utf-8

"""
 Created by liuying on 2018/9/13.
"""
from chapter03.class_method import Date


class Person:
    name = 'Person'


class Student(Person):
    name = 'Student'

    def __init__(self, school_name):
        self.school_name = school_name


if __name__ == '__main__':
    stu = Student('大学')

    # 通过__dict__查询属性   {'school_name': '大学'}
    print(stu.__dict__)
    print(stu.name)
    # 动态操作
    stu.__dict__['addr'] = '深圳'
    print(stu.addr)
    print(Person.__dict__)
    print(Student.__dict__)

    # dir 会列出对象的所有属性名称
    print(dir(stu))
