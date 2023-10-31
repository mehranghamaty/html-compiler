import unittest
import os
from HTMLCompiler.utils.toml import parse_file



test_file_contents = """[config]
folder_to_compile = test
template_folder = template
output_folder = output
string_folder = strings
"""

class UtilsTest(unittest.TestCase):
    def setUp(self):
        self._test_file_name = 'tmp.toml'
        with open(self._test_file_name, 'w') as fh:
            fh.write(test_file_contents)

    def tearDown(self):
        os.remove(self._test_file_name)

    def test_read(self):
        toml = parse_file(self._test_file_name)
        print("toml")
        print(toml)
        print("file contents")
        print(test_file_contents)
        self.assertEqual(str(toml), test_file_contents, "File contents not the same")
        

if __name__ == '__main__':
    unittest.main()