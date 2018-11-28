class CheckMethodsExistMeta(type):
    def __init__(cls, name, bases, clsdict):
        super().__init__(name, bases, clsdict)
        if not bases:
            return
        if not hasattr(cls, '_required_methods'):
            return
        for method in cls._required_methods:
            if not hasattr(cls, method):
                raise TypeError(f'Method {method} not present in {name}')
        print(f'{name} implements required methods:', *cls._required_methods)


class FooBarMustExist(metaclass=CheckMethodsExistMeta):
    _required_methods = ['foo', 'bar']


try:
    class FirstBadClass(FooBarMustExist):
        def foo(self):
            pass
except TypeError as e:
    print(e)


try:
    class SecondBadClass(FooBarMustExist):
        def bar(self):
            pass
except TypeError as e:
    print(e)


class GoodClass(FooBarMustExist):
    def foo(self):
        pass

    def bar(self):
        pass


# Metaclass propagates down the class hierarchy
class BetterClass(GoodClass):
    pass
