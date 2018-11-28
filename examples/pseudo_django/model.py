from pseudo_django.descriptors import Descriptor
from pseudo_django.code_generators import generate_func_from_descriptors


class ModelMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        descriptors = []
        for name, value in clsdict.items():
            if isinstance(value, Descriptor):
                value._name = name
                descriptors.append(value)
        if '__init__' not in clsdict:
            # Add default __init__ method based on descriptor names
            # if no user-defined __init__ present
            generate_func_from_descriptors('__init__', descriptors, clsdict)
        if '__repr__' not in clsdict:
            generate_func_from_descriptors(
                '__repr__', descriptors, clsdict, clsname
            )
        return super().__new__(cls, clsname, bases, clsdict)


class Model(metaclass=ModelMeta):
    pass
