import json

class Translation:
    def __init__(self):
        self._maps = {}

    def __getitem__(self, val) -> str:
        periodl = val.find('.')
        file_name = f"{val[:periodl]}.json"
        if file_name not in self._maps:
            with open(file_name, 'r') as fh:
                self._maps[file_name] = json.load(fh)
        return self._maps[file_name][val[periodl+1:]]
