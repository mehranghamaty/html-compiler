import sys, os, platform
from utils.cli import parse_args, Config
from utils.translation import Translation
import json

trans = Translation()

if platform.system() != 'Windows':
    DELIM = '/'
else:
    DELIM = '\\'

def read_file_and_strip(file_to_read):
    new_contents = ""
    with open(file_to_read, 'r') as file:
        for line in file.readlines():
            new_contents += line.strip()
    return new_contents

def expand_html(html_file: str, config: Config):
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
                    to_replace = trans[f"{config.string_folder}{DELIM}{command}"]
                line = line.replace(line[npos:closingpos+2], to_replace)
                new_contents += line
                if line.find('{{') == -1:
                    break
                    
    return new_contents

def expand_folder(config: Config):
    for file_name in os.listdir(config.folder_to_compile):
        if file_name[-4:] == "html":
            new_contents = expand_html(file_name, config)
            with open(f"{config.output_folder}{DELIM}{file_name}", 'w') as file:
                file.write(new_contents)
        

if __name__ == "__main__":
    config = parse_args()
    expand_folder(config)