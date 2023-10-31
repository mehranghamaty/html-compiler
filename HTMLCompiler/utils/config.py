import platform

if platform.system() != 'Windows':
    DELIM = '/'
else:
    DELIM = '\\'

translation_subfolder = "translated"