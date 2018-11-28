class SingletonMeta(type):
    def __call__(cls, *args, **kwargs):
        print('SingletonMeta.__call__')
        if hasattr(cls, '_instance'):
            print(f'Use saved instance of {cls.__name__}')
            return cls._instance
        print(f'Creating instance of {cls.__name__}')
        cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class Spam(metaclass=SingletonMeta):
    def __init__(self):
        print('Spam.__init__')


if __name__ == '__main__':
    s_1 = Spam()
    s_2 = Spam()
    print('Are the objects the same?', s_1 is s_2)
