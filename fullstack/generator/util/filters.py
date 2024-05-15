from fullstack.language.builtins import simple_type_java_mapper, simple_types_typescript


def format_type(obj_type):
    if obj_type.__class__.__name__ == 'SimpleType':
        return simple_type_java_mapper.get(obj_type.name)
    else:
        return obj_type.name
    
def format_type_typescript(obj_type):
    if obj_type.__class__.__name__ == 'SimpleType':
        return simple_types_typescript.get(obj_type.name)
    else:
        return obj_type.name


cardinality_map = {
    '@1..1': '@OneToOne',
    '@1..*': '@OneToMany',
    '@*..1': '@ManyToOne',
    '@*..*': '@ManyToMany'
}


def format_cardinality(cardinality):
    return cardinality_map.get(cardinality, '')
