import os


def create_output_file(output_path, generated_folder_name):
    if output_path is None:
        output_path = os.getcwd()
    output_path = os.path.join(output_path, generated_folder_name, '')
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    return output_path


def get_main_java_folder_path(output_path, context):
    return os.path.join(output_path, context['app_name_lower'],
                        'src/main/java',
                        context['group_name'].replace('.', '/'), context['app_name_lower'])


def get_pages_angular_folder_path(output_path, context):
    return os.path.join(output_path, 'src/app/pages')


def get_pages_react_folder_path(output_path, context):
    return os.path.join(output_path, 'src/components')


def format_template_name(path):
    return os.path.split(path)[-1]
