import os
from textx import generator

__version__ = "0.1.0.dev"

from textxjinja import textx_jinja_generator

from fullstack.generator.util.filters import format_type_typescript
from fullstack.generator.util.file_util import create_output_file, get_pages_react_folder_path
from fullstack.generator.util.string_format_util import dash_case, capitalize_str, lower_first_str

THIS_FOLDER = os.path.dirname(__file__)

# NOTE: In order to make successful build, you need to first uninstall build and dist packages
# command for that is: Remove-Item -Recurse -Force build, dist


@generator('fullstack', 'react')
def fullstack_generate_react(metamodel, model, output_path, overwrite, debug, **custom_args):
    "Generator for generating react from fullstack descriptions"

    context = get_context(model)
    filters = get_filters()

    # structure generator
    output_path = generate_react_structure(context, filters, model, output_path, overwrite)    

    # entity content generator
    generate_entity_components(context, filters, model, output_path, overwrite)


def generate_entity_components(context, filters, model, output_path, overwrite):
    component_files_template = os.path.join(THIS_FOLDER, 'template/component_files')
    pages_folder = get_pages_react_folder_path(output_path, context)
    for entity in model.entities:
        context['properties'] = entity.properties
        context['entity'] = entity
        context['entity_name_dash'] = dash_case(entity.name)
        context['entity_name'] = entity.name

        # Run Jinja generator
        textx_jinja_generator(component_files_template, pages_folder, context, overwrite, filters=filters)


def generate_react_structure(context, filters, model, output_path, overwrite):
    react_structure_template = os.path.join(THIS_FOLDER, 'template/react_structure')
    output_path = create_output_file(output_path, 'generated_react')
    for entity in model.entities:
        context['properties'] = entity.properties
        context['entity'] = entity
        context['entity_name'] = entity.name

        textx_jinja_generator(react_structure_template, output_path, context, overwrite, filters=filters)
    return output_path


def get_context(model):
    project_name = model.project_info.projectName
    project_name_dash_case = dash_case(project_name) if project_name else 'demo'

    context = {'app_name': project_name if project_name else 'Demo',
               'app_name_dash': project_name_dash_case,
               'app_name_lower': project_name.lower() if project_name else 'demo',
               'app_name_cap': capitalize_str(project_name) if project_name else 'Demo',
               'project_info': model.project_info,
               'entities': model.entities
               }
    return context


def get_filters():
    return {'format_type': format_type_typescript,
            'capitalize_str': capitalize_str,
            'lower_first_str': lower_first_str
            }