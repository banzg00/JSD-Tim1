import os
from functools import partial
from textx import generator

__version__ = "0.1.0.dev"

from textxjinja import textx_jinja_generator

THIS_FOLDER = os.path.dirname(__file__)


@generator('fullstack', 'angular')
def fullstack_generate_angular(metamodel, model, output_path, overwrite, debug, **custom_args):
    "Generator for generating angular from fullstack descriptions"

    context = {'group_name': "uns.ac.rs",
               'app_name': "JSDGenerator",
               'entities': model.entities
               }

    template_folder = os.path.join(THIS_FOLDER, 'template')
    output_path = create_output_file(output_path)

    # Run Jinja generator
    textx_jinja_generator(template_folder, output_path, context, overwrite)
    # filters: Any = None,
    # transform_names: Any = None


def create_output_file(output_path):
    if output_path is None:
        output_path = os.getcwd()
    output_path = os.path.join(output_path, 'generated_angular', '')
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    return output_path
