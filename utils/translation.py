import json, os
from utils.cli import ArgsConfig
from utils.config import DELIM, translation_subfolder

class Translation:
    def __init__(self, config : ArgsConfig):
        self._maps = {}
        self._argsConfig = config
        self._transFolder = f"{self._argsConfig.string_folder}{DELIM}{translation_subfolder}"
        if not os.path.exists(self._transFolder):
            os.makedirs(self._transFolder)

    def __getitem__(self, val) -> str:
        periodl = val.find('.')
        file_name = f"{self._argsConfig.string_folder}{DELIM}{val[:periodl]}.json"
        if file_name not in self._maps:
            with open(file_name, 'r') as fh:
                self._maps[file_name] = json.load(fh)
        return self._maps[file_name][val[periodl+1:]]
