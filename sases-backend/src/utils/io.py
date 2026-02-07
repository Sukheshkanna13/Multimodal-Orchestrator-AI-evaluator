def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

def append_to_file(file_path, content):
    with open(file_path, 'a') as file:
        file.write(content)

def delete_file(file_path):
    import os
    if os.path.exists(file_path):
        os.remove(file_path)

def file_exists(file_path):
    import os
    return os.path.isfile(file_path)