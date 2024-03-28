from ..language.builtins import simple_type_java_mapper


def format_type(obj_type):
    if obj_type.__class__.__name__ == 'SimpleType':
        return simple_type_java_mapper.get(obj_type.name)
    else:
        return obj_type.name
