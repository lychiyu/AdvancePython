# coding: utf-8

"""
 Created by liuying on 2018/9/14.
"""
import numbers

"""
实现一个可切片的对象
实现 Sequence 的协议
"""

from collections import abc


class Group:
    def __init__(self, group_name, company_name, staffs):
        self.group_name = group_name
        self.company_name = company_name
        self.staffs = staffs

    def __getitem__(self, item):
        cls = type(self)
        if isinstance(item, slice):
            return cls(group_name=self.group_name, company_name=self.company_name, staffs=self.staffs[item])
        elif isinstance(item, numbers.Integral):
            return cls(group_name=self.group_name, company_name=self.company_name, staffs=[self.staffs[item]])

    def __reversed__(self):
        self.staffs.reverse()

    def __len__(self):
        return len(self.staffs)

    def __iter__(self):
        return iter(self.staffs)

    def __contains__(self, item):
        if item in self.staffs:
            return True
        return False


staffs = ['lychiyu', 'ly', 'liuying']
group = Group(company_name='sz', group_name='dev', staffs=staffs)

sub_group = group[:2]

print(sub_group)
