import os
import argparse

from utils.cli import ArgsConfig
from utils.translation import Translation
from utils.compile import expand_folder
from utils.generate import generate_project

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="HTMLCompiler",
        description='Enables fast development of plain html clients')
    subparsers = parser.add_subparsers(help='help for subcommand', dest='subcommand')

    folder_parser = subparsers.add_parser('compile')
    folder_parser.add_argument('-ftc', '--folder-to-compile', 
                        type=str, default="html_pages")
    folder_parser.add_argument('-tf', '--template-folder', 
                        type=str, default="html_fragments")
    folder_parser.add_argument('-of', '--output-folder', 
                        type=str, default="html_output")
    folder_parser.add_argument('-sf', '--string-folder', 
                        type=str, default="strings")
    folder_parser.add_argument('-t', '--toml', 
                               type=str, default=None, 
                               help='not currently implemented')

    gen_parser = subparsers.add_parser('generate')
    gen_parser.add_argument('generate', help='generate a project folder')
    gen_parser.add_argument('-g', '--generate', type=str, default='.', help='generate a project folder')

    args = parser.parse_args()

    match args.subcommand:
        case 'compile':
            if args.toml != None:
                raise NotImplementedError
            config = ArgsConfig(args.folder_to_compile,
                                args.template_folder, args.output_folder, args.string_folder)
            trans = Translation(config)
            expand_folder(trans, config)
        case 'generate':
            generate_project(args.generate)
            #generate_project(args.generate)
        case _:
            parser.print_help()
    