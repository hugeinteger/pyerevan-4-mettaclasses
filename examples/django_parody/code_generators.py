def generate_init_code_from_descriptors(descriptors):
    if not descriptors:
        return 'def __init__(self): pass'

    descriptor_names = [descriptor._name for descriptor in descriptors]
    code = [
        f'def __init__(self, {", ".join(descriptor_names)}):'
    ]
    for descriptor_name in descriptor_names:
        code.append(
            f'    self.{descriptor_name} = {descriptor_name}'
        )
    return '\n'.join(code)


def generate_repr_code_from_descriptors(descriptors, name):
    code_parts = [
        '{' + f'self.{descriptor._name}' + '}' for descriptor in descriptors
    ]
    inside_brackets = ', '.join(code_parts)
    return f'def __str__(self):\n    return f"{name}({inside_brackets})"'


function_code_generators = {
    '__init__': generate_init_code_from_descriptors,
    '__repr__': generate_repr_code_from_descriptors
}


def generate_func_from_descriptors(
    func_name, descriptors, namespace=None, *args, **kwargs
):
    if namespace is None:
        namespace = {}
    code = function_code_generators[func_name](descriptors, *args, **kwargs)
    exec(code, globals(), namespace)
    return namespace
