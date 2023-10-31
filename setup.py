"""
Sample setup.py file
"""
from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\\n" + fh.read()

setup(
    name="HTMLCompiler",
    version='0.0.4',
    author="Mehran Nathan Ghamaty",
    author_email="mnghamaty@gmail.com",
    description="An app to compile static html pages",
    url = "https://github.com/mehranghamaty/html-compiler",
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    python_requires='>3.10',
    test_suite="tests",
    install_requires=[],
    keywords=['pypi', 'cicd', 'python'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)