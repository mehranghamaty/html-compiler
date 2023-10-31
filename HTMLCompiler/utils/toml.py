

class TOML:
    def __init__(self, file_path=None):
        self._page = {}
        if file_path != None:
            raise NotImplementedError

    def add_section(self, section_name: str, section_content: dict):
        self._page[section_name] = section_content

    def __repr__(self):
        pass
