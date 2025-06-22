import os


def get_files_info(working_directory, directory=None):
    if os.path.abspath(directory).startswith(working_directory) is False:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if os.path.isdir(directory) is False:
        return f'Error: "{directory}" is not a directory'
    
    for item in directory:
        print(f'- {item}: file_size={os.path.getsize(item)}, is_dir={os.path.isdir(item)}')





