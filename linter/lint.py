"""This module will handle loading and linting of the files"""
from dataclasses import replace
import glob
import re

def lint_file(file_path: str, config):
    """lints a file

    Args:
        file_path (str): path to the file
        config (_type_): config dictionary
    """
    print("linting file <" + file_path + ">")
    with open(file_path) as f:
        contents = f.read()
        contents = contents.split("\n")
        contents = lint_blanklines(contents, config)
        contents = lint_indentation(contents, config)
        # contents = lint_sentences(contents, config)
        contents = lint_comments(contents, config)
        with open("debug.tex", "w") as output:
            output.write("\n".join(contents))
        # print("\n".join(contents))

def lint_directory(directory: str, config):
    """lints all .tex files in directory and subdirectories

    Args:
        directory (str): _description_
        config (_type_): _description_
    """
    print("linting directory <" + directory + ">")
    files = glob.glob(f"{directory}**/*.tex", recursive=True)
    for file in files:
        lint_file(file, config)

def lint_comments(file_contents, config):
    """Lints the comments of a .tex file according to the config

    Args:
        file_contents (str[]): the entirety of contents in a file
        config (dict): lint config

    Returns:
        str[]: file_contents but modified
    """

    spaces = config["formatting"]["comments"]["spaces"]
    lines_with_comments = [index for index, line in enumerate(file_contents) if "%" in line]
    for index in lines_with_comments:
        # Replaces %<any nr of spaces> or %<no_spaces> with %<x*" "> and doesnt have a \ before the %
        expression = r"^(?!\\)(\%\s+|\%)"
        replacement =  "%" + " " * spaces
        file_contents[index] = re.sub(expression, replacement, file_contents[index])
    return file_contents


def lint_indentation(file_contents, config):
    """_summary_

    Args:
        file_contents (str[]): the entirety of contents in a file
        config (dict): lint config

    Returns:
        str[]: file_contents but modified
    """

    return file_contents

def lint_sentences(file_contents, config):
    """_summary_

    Args:
        file_contents (str[]): the entirety of contents in a file
        config (dict): lint config

    Returns:
        str[]: file_contents but modified
    """
    if config["formatting"]["git_support"]["newline_after_sentence"]:
        lines_with_dots = [index for index, line in enumerate(file_contents) if "." in line]
        for line in lines_with_dots:
            comment_index = file_contents[line].find("%")
            dot_indices = [m.start() for m in re.finditer(r"\.", file_contents[line])]
            dot_indices_before = [x for x in dot_indices if (comment_index == -1 or x < comment_index) and x + 1 < len(file_contents[line])]
            for dot_index in dot_indices_before:
                file_contents[line] = file_contents[line][:dot_index + 1] + "\n" + file_contents[line][dot_index + 1:]
        file_contents = "\n".join(file_contents)
        file_contents = file_contents.split("\n")
    return file_contents

def lint_blanklines(file_contents, config):
    """_summary_

    Args:
        file_contents (str[]): the entirety of contents in a file
        config (dict): lint config

    Returns:
        str[]: file_contents but modified
    """

    return file_contents