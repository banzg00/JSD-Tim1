from .custom_model import SimpleType

simple_type_java_mapper = {
    'int': 'Integer',
    'str': 'String',
    'float': 'float',
    'bool': 'boolean',
    'Long': 'Long'
}

simple_types = {key: SimpleType(None, value)
                for key, value in simple_type_java_mapper.items()}
