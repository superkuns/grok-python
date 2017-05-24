#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/24 22:00
# @Author  : Matrix
# @Site    : 
# @File    : singleton.py
# @Software: PyCharm

__author__ = 'blackmatrix'


class Singleton(type):

    def __init__(cls, *args, **kwargs):
        cls.__instance = None
        super().__init__(*args, **kwargs)

    # __call__ 是对于类实例有效，比如说Spam类，是type类的实例
    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            # TODO 为什么是__call__ 方法，而不是__init__ 或者  __new__ ?
            # TODO type 中，__call__ 和 __init__ 还有 __new__ 是什么关系？
            cls.__instance = super().__call__(*args, **kwargs)
            return cls.__instance
        else:
            return cls.__instance


class Spam(metaclass=Singleton):

    def __init__(self):
        print('Creating Spam')

if __name__ == '__main__':
    a = Spam()
    b = Spam()
    print(a is b)
    c = Spam()
    print(a is c)