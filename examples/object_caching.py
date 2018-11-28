import weakref


class CachedMeta(type):
    def __init__(cls, *args, **kwargs):
        print('CachedMeta.__init__')
        super().__init__(*args, **kwargs)
        # As soon as an instance is garbage-collected the corresponding
        # value should be removed from the dictionary
        # (hence the use of a WeakValueDictionary)
        cls.__cache = weakref.WeakValueDictionary()

    def __call__(cls, *args):
        # Notice the limitation: the objects cannot be constructed with
        # keyword arguments :'(
        print('CachedMeta.__call__')
        args_str = map(str, args)

        if args in cls.__cache:
            print(f'Use cached instance {cls.__name__}({", ".join(args_str)})')
            return cls.__cache[args]

        print(f'Create instance {cls.__name__}({", ".join(args_str)})')
        obj = super().__call__(*args)
        cls.__cache[args] = obj
        return obj


class Spam(metaclass=CachedMeta):
    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    eggs = Spam('eggs')
    eggs_other = Spam('eggs')
    print('Are the objects the same?', eggs is eggs_other)
