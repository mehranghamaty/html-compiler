import os
import logging

from utils.config import DELIM

def generate_project(folder_location: str):
    print(f"Hello generating into {folder_location}")
    if os.path.exists(folder_location):
        logging.exception(f"Directory already exists: {folder_location}")
        raise IsADirectoryError

    folder_to_compile = "html_pages"
    template_folder = "html_fragments"
    output_folder = "compiled"
    string_folder = "strings"

    default_config = f"""[config]
folder_to_compile = {folder_to_compile}
template_folder = {template_folder}
output_folder = {output_folder}
string_folder = {string_folder}"""
    
    os.makedirs(folder_location)
    os.makedirs(f"{folder_location}{DELIM}{folder_to_compile}")
    os.makedirs(f"{folder_location}{DELIM}{template_folder}")
    os.makedirs(f"{folder_location}{DELIM}{output_folder}")
    os.makedirs(f"{folder_location}{DELIM}{string_folder}")

    config_path = f"{folder_location}{DELIM}config.toml"

    with open(config_path, 'w') as fh:
        fh.write(default_config)