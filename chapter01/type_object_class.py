# coding: utf-8

"""
 Created by liuying on 2018/9/12.
"""

"""
类是由type这个类所生成的对象
object是所有类都要继承的顶层类
type是个类同时也是一个对象，父类是object
object类也是由type所生成的, object的父类为空
"""

a = 1
b = 'abc'

# type--->int----->1
print(type(1))
print(type(int))

# type--->str----->'abc'
print(type(b))
print(type(str))


class Person:
    pass


class Student(Person):
    pass


# type--->Person----->person
person = Person()
print(type(person))
print(type(Person))

print(int.__bases__)
print(str.__bases__)
print(Person.__bases__)
print(Student.__bases__)
print(type.__bases__)
print(type(object))
print(object.__bases__)
print(type(type))
