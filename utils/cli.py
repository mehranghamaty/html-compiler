import sys, os
from dataclasses import dataclass 

@dataclass
class Config:
    folder_to_compile: str
    template_folder: str
    output_folder: str
    string_folder : str

def parse_args() -> Config:
    if len(sys.argv) != 5:
        print(f"Usage: {sys.argv[0]} template_folder folder_to_compile output_folder string_folder")
        exit(0)

    template_folder = sys.argv[1]
    folder_to_compile = sys.argv[2]
    output_folder = sys.argv[3]
    string_folder = sys.argv[4]

    if not os.path.exists(template_folder):
        print(f"Template folder does not exist; {template_folder}")
        exit(0)

    if not os.path.exists(folder_to_compile):
        print(f"Template folder does not exist; {folder_to_compile}")
        exit(0)
    
    if not os.path.exists(folder_to_compile):
        print(f"Template folder does not exist; {folder_to_compile}")
        exit(0)

    if not os.path.exists(string_folder):
        print(f"Template folder does not exist; {string_folder}")
        exit(0)

    return Config(folder_to_compile, template_folder, output_folder, string_folder)