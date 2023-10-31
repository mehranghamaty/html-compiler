import os

from utils.cli import ArgsConfig
from utils.translation import Translation
from utils.parser import read_file_and_strip
from utils.config import DELIM

def expand_html(html_file: str, trans: Translation, config: ArgsConfig):
    new_contents = ""
    with open(f"{config.folder_to_compile}{DELIM}{html_file}", 'r') as file:
        for line in file.readlines():
            while True:
                line = line.strip()
                npos = line.find('{{')
                if npos == -1:
                    new_contents += line.strip()
                    break
                closingpos = line.find('}}')
                command = line[npos+2:closingpos].strip()
                if command[-4:] == "html":
                    to_replace = read_file_and_strip(f"{config.template_folder}{DELIM}{command}")
                else:
                    to_replace = trans[command]
                line = line.replace(line[npos:closingpos+2], to_replace)
                new_contents += line
                if line.find('{{') == -1:
                    break
                    
    return new_contents

def expand_folder(trans: Translation, config: ArgsConfig):
    for file_name in os.listdir(config.folder_to_compile):
        if file_name[-4:] == "html":
            new_contents = expand_html(file_name, trans, config)
            with open(f"{config.output_folder}{DELIM}{file_name}", 'w') as file:
                file.write(new_contents)
