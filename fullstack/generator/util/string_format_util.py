import re


def dash_case(name):
    return re.sub(r'([a-zA-Z])(?=[A-Z])', r'\1-', name).lower()


def capitalize_str(name):
    return name[0].upper() + name[1:]


def lower_first_str(name):
    return name[0].lower() + name[1:]
