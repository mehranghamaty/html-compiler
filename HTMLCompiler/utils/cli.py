import  os
from dataclasses import dataclass 

@dataclass
class ArgsConfig:
    folder_to_compile: str
    template_folder: str
    output_folder: str
    string_folder : str

    def __post_init__(self):
        
        if not os.path.exists(self.template_folder):
            print(f"Template folder does not exist; {self.template_folder}")
            raise NotADirectoryError

        if not os.path.exists(self.folder_to_compile):
            print(f"Template folder does not exist; {self.folder_to_compile}")
            raise NotADirectoryError
        
        if not os.path.exists(self.folder_to_compile):
            print(f"Template folder does not exist; {self.folder_to_compile}")
            raise NotADirectoryError

        if not os.path.exists(self.string_folder):
            print(f"Template folder does not exist; {self.string_folder}")
            raise NotADirectoryError
