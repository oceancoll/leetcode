# coding:utf-8
# 装饰器
import functools
def single(func):
    instance = {}
    functools.wraps(func)
    def _single(*args, **kwargs):
        if func not in instance:
            instance[func] = func(*args, **kwargs)
        return instance[func]
    return _single

@single
class Single1(object):
    def __init__(self):
        self.a = 1

s1 = Single1()
s2 = Single1()
print s1 is s2  # True
print s1.a is s2.a  # True


# __new__
class Single2(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            origin = super(Single2, cls)
            cls._instance = origin.__new__(cls)
        return cls._instance


class Myclass(Single2):
    def __init__(self):
        self.a = 1

s3 = Myclass()
s4 = Myclass()
print s3 is s4
print s3.a is s3.a




