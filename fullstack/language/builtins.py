from .custom_model import SimpleType

simple_type_java_mapper = {
    'int': 'Integer',
    'str': 'String',
    'float': 'float',
    'bool': 'boolean',
    'long': 'Long',
    'date': 'LocalDate',
    'dateTime': 'LocalDateTime',
}

simple_type_java_typescript = {
    'int': 'number',
    'str': 'string',
    'float': 'number',
    'bool': 'boolean',
    'long': 'number',
    'date': 'Date',
    'dateTime': 'Date',
}

simple_types = {key: SimpleType(None, value)
                for key, value in simple_type_java_mapper.items()}

simple_types_typescript = {key: SimpleType(None, value)
                for key, value in simple_type_java_typescript.items()}
