import os
from textx import language, metamodel_from_file
from .custom_model import *
from .builtins import *
from .processors import *

__version__ = "0.1.0.dev"

# from .processors import input_dto_mapping_custom_type_processor

THIS_FOLDER = os.path.dirname(__file__)


@language('fullstack', '*.fs')
def fullstack_language():
    """fullstack language"""

    fullstack_grammar_path = os.path.join(THIS_FOLDER, 'fullstack.tx')

    metamodel = metamodel_from_file(fullstack_grammar_path,
                                    classes=[SimpleType],
                                    builtins=simple_types,
                                    debug=False)

    # Here if necessary register object processors or scope providers
    # http://textx.github.io/textX/stable/metamodel/#object-processors
    # http://textx.github.io/textX/stable/scoping/

    metamodel.register_model_processor(semantic_check)

    # metamodel.register_obj_processors({
    #     'InputDTOMapping_CustomType': input_dto_mapping_custom_type_processor,
    # })

    return metamodel
