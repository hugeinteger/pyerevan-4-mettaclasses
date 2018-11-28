class Descriptor:
    def __init__(self, name=None):
        self._name = name

    def __set__(self, instance, value):
        instance.__dict__[self._name] = value


class TypedDescriptor(Descriptor):
    _expected_type = type(None)

    def __set__(self, instance, value):
        if not isinstance(value, self._expected_type):
            raise TypeError(
                f'Expected instance of {self._expected_type.__name__} '
                f'but got {type(value).__name__}'
            )
        super().__set__(instance, value)


class Integer(TypedDescriptor):
    _expected_type = int


class Float(TypedDescriptor):
    _expected_type = float


class String(TypedDescriptor):
    _expected_type = str
