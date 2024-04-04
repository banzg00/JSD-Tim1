import os

from textx import generator
from textxjinja import textx_jinja_generator

from fullstack.generator.util.filters import format_type, format_cardinality
from ..util.file_util import create_output_file, get_main_java_folder_path
from ..util.string_format_util import capitalize_str

__version__ = "0.1.0.dev"
THIS_FOLDER = os.path.dirname(__file__)


@generator('fullstack', 'springboot')
def fullstack_generate_springboot(metamodel, model, output_path, overwrite, debug, **custom_args):
    """Generator for springboot from fullstack descriptions"""

    context = get_context(model)
    filters = get_filters()

    # structure generator
    output_path = generate_springboot_structure(context, filters, output_path, overwrite)
    main_folder_path = generate_main_file(context, filters, output_path, overwrite)
    generate_entity_files(context, filters, main_folder_path, model, overwrite)


def generate_entity_files(context, filters, main_folder_path, model, overwrite):
    content_structure_template = os.path.join(THIS_FOLDER, 'template/content_structure')
    for entity in model.entities:
        context['properties'] = entity.properties
        context['entity'] = entity
        context['entity_name'] = entity.name

        # Run Jinja generator
        textx_jinja_generator(content_structure_template, main_folder_path, context, overwrite, filters=filters)


def generate_main_file(context, filters, output_path, overwrite):
    main_file_template = os.path.join(THIS_FOLDER, 'template/main_file')
    main_folder_path = get_main_java_folder_path(output_path, context)
    textx_jinja_generator(main_file_template, main_folder_path, context, overwrite, filters=filters)
    return main_folder_path


def generate_springboot_structure(context, filters, output_path, overwrite):
    springboot_structure_template = os.path.join(THIS_FOLDER, 'template/springboot_structure')
    output_path = create_output_file(output_path, 'generated_springboot')
    textx_jinja_generator(springboot_structure_template, output_path, context, overwrite, filters=filters)
    return output_path


def get_filters():
    return {'format_type': format_type,
            'format_cardinality': format_cardinality
            }


def get_context(model):
    project_name = model.project_info.projectName
    # Prepare context dictionary
    context = {'group_name': '.'.join(model.project_info.group) if model.project_info.group else 'com.example',
               'app_name': project_name if project_name else 'Demo',
               'app_name_lower': project_name.lower() if project_name else 'demo',
               'app_name_cap': capitalize_str(project_name) if project_name else 'Demo',
               'project_info': model.project_info,
               'entities': model.entities
               }
    return context


