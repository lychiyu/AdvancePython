# coding: utf-8

"""
 Created by liuying on 2018/9/12.
"""


class Cat:
    def say(self):
        print('i am a cat')


class Dog:
    def say(self):
        print('i am a dog')


class Duck:
    def say(self):
        print('i am a duck')


def say(obj):
    obj().say()


for animal in [Cat, Dog, Duck]:
    say(animal)



