import sys, os, platform

if platform.system() != 'Windows':
    DELIM = '/'
else:
    DELIM = '\\'

def parse_args():
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} template_folder folder_to_compile output_folder")
        exit(0)

    template_folder = sys.argv[1]
    folder_to_compile = sys.argv[2]
    output_folder = sys.argv[3]

    if not os.path.exists(template_folder):
        print(f"Template folder does not exist; {template_folder}")
        exit(0)

    if not os.path.exists(folder_to_compile):
        print(f"Template folder does not exist; {folder_to_compile}")
        exit(0)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    return folder_to_compile, template_folder, output_folder

def read_file_and_strip(file_to_read):
    new_contents = ""
    with open(file_to_read, 'r') as file:
        for line in file.readlines():
            new_contents += line.strip()
    return new_contents

def expand(html_file, folder_to_compile, path_to_template_folder, output_folder):
    new_contents = ""
    with open(f"{folder_to_compile}{DELIM}{html_file}", 'r') as file:
        for line in file.readlines():
            while True:
                line = line.strip()
                npos = line.find('{{')
                if npos == -1:
                    new_contents += line.strip()
                    break
                closingpos = line.find('}}')
                file_to_insert = line[npos+2:closingpos].strip()
                print(f"{path_to_template_folder}{DELIM}{file_to_insert}")
                to_replace = read_file_and_strip(f"{path_to_template_folder}{DELIM}{file_to_insert}")
                line = line.replace(line[npos:closingpos+2], to_replace)
                new_contents += line
    
    return new_contents


def expand_folder(folder_to_compile, template_folder, output_folder):
    for file_name in os.listdir(folder_to_compile):
        if file_name[-4:] == "html":
            new_contents = expand(file_name, folder_to_compile, template_folder, output_folder)
            with open(f"{output_folder}{DELIM}{file_name}", 'w') as file:
                file.write(new_contents)

if __name__ == "__main__":
    folder_to_compile, template_folder, output_folder = parse_args()
    expand_folder(folder_to_compile, template_folder, output_folder)