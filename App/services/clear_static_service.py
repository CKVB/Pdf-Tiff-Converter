import os


def clear_static_service(folder_path: str):
    for file in os.listdir(folder_path):
        os.remove(os.path.join(folder_path, file))
