import os

from textx import generator
from textxjinja import textx_jinja_generator

__version__ = "0.1.0.dev"
THIS_FOLDER = os.path.dirname(__file__)


@generator('fullstack', 'springboot')
def fullstack_generate_springboot(metamodel, model, output_path, overwrite, debug, **custom_args):
    """Generator for springboot from fullstack descriptions"""

    # Prepare context dictionary
    context = {'group_name': "uns.ac.rs",
               'app_name': "JSDGenerator",
               'entities': model.entities
               }

    template_folder = os.path.join(THIS_FOLDER, 'template')
    output_path = create_output_file(output_path)

    for entity in model.entities:
        context['properties'] = entity.properties
        context['entity'] = entity
        context['entity_name'] = entity.name

        # Run Jinja generator
        textx_jinja_generator(template_folder, output_path, context, overwrite)

    # filters: Any = None,
    # transform_names: Any = None


def create_output_file(output_path):
    if output_path is None:
        output_path = os.getcwd()
    output_path = os.path.join(output_path, 'generated_springboot', '')
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    return output_path

