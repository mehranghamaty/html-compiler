class TOML:
    def __init__(self):
        self._page = {}

    def add_section(self, section_name: str, section_content: dict):
        self._page[section_name] = section_content

    def __repr__(self) -> str:
        print(self._page)
        repr = ""
        for config_name, config in self._page.items():
            repr += f"[{config_name}]\n"
            for k, v in config.items():
                repr += f"{k} = {v}\n"
        return repr

def parse_file(file_path: str) -> TOML:
    toml = TOML()
    with open(file_path, 'r') as fh:
        section_name = None
        section = {}
        for line in fh.readlines():
            if line == '':
                if section_name:
                    toml.add_section(section_name, section)

            elif '[' in line:
                key_start = line.find('[')
                key_end = line.find(']')
                section_name = line[key_start+1:key_end]
            else:
                npos = line.find('=')
                section[line[:npos].strip()] = line[npos+1:].strip()
    if section_name:
        toml.add_section(section_name, section)
    return toml

                