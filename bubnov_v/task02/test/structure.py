import os
import shutil


def create_structure(base_path: str, structure_content: list) -> None:
    if len(structure_content) == 0:
        return
    dir_name = structure_content[0]
    if os.path.exists(os.path.join(base_path, dir_name)):
        remove_structure(base_path, dir_name)

    dir_path = os.path.join(base_path, dir_name)
    os.makedirs(dir_path)
    for item in structure_content[1:]:
        if type(item) is str:
            with open(os.path.join(dir_path, item), 'w'):
                pass
        elif type(item) is list:
            create_structure(dir_path, item)


def remove_structure(base_path: str, content_structure: str) -> None:
    dir_path = os.path.join(base_path, content_structure)

    try:
        shutil.rmtree(dir_path)
    except FileNotFoundError:
        return
