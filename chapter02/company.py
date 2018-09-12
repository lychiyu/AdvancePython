# coding: utf-8

"""
 Created by liuying on 2018/9/12.
"""
"""
魔法函数，就是以双下划线开头和结尾
"""


class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __iter__(self):
        pass

    def __getitem__(self, item):
        return self.employee[item]

    def __repr__(self):
        return ''.join(self.employee)

    def __str__(self):
        return ''.join(self.employee)

    def __len__(self):
        return len(self.employee)

company = Company(['ly', 'liuying', 'lychiyu'])
employee = company.employee

for i in employee:
    print(i)

# __getitem__
for e in company:
    print(e)
