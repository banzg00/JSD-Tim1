import os


def create_output_file(output_path):
    if output_path is None:
        output_path = os.getcwd()
    output_path = os.path.join(output_path, 'generated_springboot', '')
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    return output_path


def get_main_folder_path(output_path, context):
    return os.path.join(output_path, context['app_name_lower'],
                        'src/main/java',
                        context['group_name'].replace('.', '/'), context['app_name_lower'])

