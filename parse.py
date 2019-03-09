
import pathlib
import argparse


def parse_text_file(file_path):

    try:
        file_paths = []
        file = open(file_path, 'r')

        for line in file:
            file_paths.append(line.strip('\n'))

    finally:
        file.close()

    return file_paths


def parse_arguments():
    parser = argparse.ArgumentParser(prog='PROG', description="""This is a simple crc sum and hash calculator with
                                     focus on simple operation and the ability to process large batches of files for 
                                     a somewhat automated approach.""")

    subparsers = parser.add_subparsers()

    parser_single = subparsers.add_parser('single', help='Single file for hashing')
    parser_single.add_argument("input", help="A path to a single file to process", type=str)
    parser_single.set_defaults(func=handle_single)

    parser_list = subparsers.add_parser('list', help='Takes list of files to process from text file')
    parser_list.add_argument("input", help="A text file containing file paths to process", type=str)
    parser_list.set_defaults(func=handle_list)

    parser_pattern = subparsers.add_parser('glob', help='Takes all files from given path or current directory that '
                                                        'match a given pattern or a set of patterns')
    parser_pattern.add_argument("input", help="Directory to process by pattern, current directory if not given",
                                nargs='?', type=str, default='.')
    parser_pattern.add_argument("pattern", help="""File suffixes given in the form ".ex1, 
                                .ex2, .ex3" """, nargs='+', type=str)
    parser_pattern.set_defaults(func=handle_glob)

    args = parser.parse_args()

    return args


def handle_single(args):

    file_path = args.input
    return [file_path]


def handle_list(args):

    file_paths = parse_text_file(args.input)
    return file_paths


def handle_glob(args):

    file_paths_final = []

    pattern_list = args.pattern

    for pattern in pattern_list:
        pattern = '*'+pattern
        file_paths = pathlib.Path(args.input).glob(pattern)
        file_paths_final = file_paths_final + list(file_paths)

    return file_paths_final
