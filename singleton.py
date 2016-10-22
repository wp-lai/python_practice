"""
Author: Alan Lai
Date: Oct 22, 2016

Task:
Implement singleton design pattern

>>> a = MyClass()
>>> b = MyClass()
>>> a is b
True
"""
def singleton(cls, *args, **kwargs):
    instance = {}
    def get_instance(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return get_instance


@singleton
class MyClass():
    pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()
