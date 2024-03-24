import os
from textx import language, metamodel_from_file
from .custom_model import SimpleType

__version__ = "0.1.0.dev"
THIS_FOLDER = os.path.dirname(__file__)


@language('fullstack', '*.fs')
def fullstack_language():
    """fullstack language"""

    fullstack_grammar_path = os.path.join(THIS_FOLDER, 'fullstack.tx')
    builtin_types = {
        'int': SimpleType(None, 'int'),
        'string': SimpleType(None, 'String'),
        'float': SimpleType(None, 'float'),
        'boolean': SimpleType(None, 'boolean'),
        'Long': SimpleType(None, 'Long')
    }
    metamodel = metamodel_from_file(fullstack_grammar_path,
                                    classes=[SimpleType],
                                    builtins=builtin_types,
                                    debug=False)

    # Here if necessary register object processors or scope providers
    # http://textx.github.io/textX/stable/metamodel/#object-processors
    # http://textx.github.io/textX/stable/scoping/

    # metamodel.register_obj_processors({
    #     'BasicInfo': basic_info_processor,
    # })

    return metamodel
