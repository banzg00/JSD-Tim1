import os

from textx import generator
from textxjinja import textx_jinja_generator

from .util.file_util import create_output_file, get_main_folder_path
from ..filters import format_type

__version__ = "0.1.0.dev"
THIS_FOLDER = os.path.dirname(__file__)


@generator('fullstack', 'springboot')
def fullstack_generate_springboot(metamodel, model, output_path, overwrite, debug, **custom_args):
    """Generator for springboot from fullstack descriptions"""
    project_name = model.project_info.projectName
    # Prepare context dictionary
    context = {'group_name': '.'.join(model.project_info.group) if model.project_info.group else 'com.example',
               'app_name': project_name if project_name else 'Demo',
               'app_name_lower': project_name.lower() if project_name else 'demo',
               'app_name_cap':  project_name[0].upper() + project_name[1:] if project_name else 'Demo',
               'project_info': model.project_info,
               'entities': model.entities
               }

    filters = {'format_type': format_type}

    # structure generator
    springboot_structure_template = os.path.join(THIS_FOLDER, 'template/springboot_structure')
    output_path = create_output_file(output_path)
    textx_jinja_generator(springboot_structure_template, output_path, context, overwrite, filters=filters)

    # main class generator
    main_file_template = os.path.join(THIS_FOLDER, 'template/main_file')
    main_folder_path = get_main_folder_path(output_path, context)
    textx_jinja_generator(main_file_template, main_folder_path, context, overwrite, filters=filters)

    # entity content generator
    content_structure_template = os.path.join(THIS_FOLDER, 'template/content_structure')

    for entity in model.entities:
        context['properties'] = entity.properties
        context['entity'] = entity
        context['entity_name'] = entity.name

        # Run Jinja generator
        textx_jinja_generator(content_structure_template, main_folder_path, context, overwrite, filters=filters)


