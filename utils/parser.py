def read_file_and_strip(file_to_read):
    new_contents = ""
    with open(file_to_read, 'r') as file:
        for line in file.readlines():
            new_contents += line.strip()
    return new_contents