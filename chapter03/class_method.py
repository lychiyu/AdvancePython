# coding: utf-8

"""
 Created by liuying on 2018/9/13.
"""


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @staticmethod
    def parse_from_string(date_str):
        year, month, day = tuple(date_str.split('-'))
        return Date(int(year), int(month), int(day))

    @classmethod
    def from_string(cls, date_str):
        year, month, day = tuple(date_str.split('-'))
        return cls(int(year), int(month), int(day))

    def tomorrow(self):
        self.day += 1

    def __str__(self):
        return (f'{self.year}-{self.month}-{self.day}')

if __name__ == '__main__':
    date = Date(2018, 9, 13)
    print(date)

    date.tomorrow()
    print(date)
