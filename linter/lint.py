"""This module will handle loading and linting of the files"""
import glob
import re
import os

def lint_file(file_path: str, config):
    """lints a file

    Args:
        file_path (str): path to the file
        config (_type_): config dictionary
    """
    print("linting file <" + file_path + ">")
    linted_file_string = ""
    with open(file_path, "r+") as f:
        contents = f.read()
        contents = contents.split("\n")
        contents = lint_blanklines(contents, config)
        contents = lint_sentences(contents, config)
        contents = lint_indentation(contents, config)
        contents = lint_comments(contents, config)
        linted_file_string = "\n".join(contents)
    if config["overwrite"]:
        with open(file_path, "w") as f:
            f.write(linted_file_string)
    else:
        new_path = f"output/{file_path}"
        os.makedirs(os.path.dirname(new_path), exist_ok=True)
        with open(new_path, "w") as output:
            output.write(linted_file_string)

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
        expression = r"(?<!\\)(\%\s*)"
        replacement =  "%" + " " * spaces
        file_contents[index] = re.sub(expression, replacement, file_contents[index])
    return file_contents

def lint_indentation(file_contents, config):
    """Formats the indentation of file contents according to your configuration

    Args:
        file_contents (str[]): the entirety of contents in a file
        config (dict): lint config

    Returns:
        str[]: file_contents but modified
    """
    spaces = config["formatting"]["indentation"]["spaces"]
    excluded_blocks = config["formatting"]["indentation"]["excluded_blocks"]
    blocks = ([(index, line.strip()) for index, line in enumerate(file_contents)
        if line.startswith(r"\begin{") and not any(ex in line for ex in excluded_blocks)])
    for i, line in enumerate(file_contents):
        file_contents[i] = line.lstrip()
    for _, block in enumerate(blocks):
        end_block = block[1].replace("begin", "end")
        end_block = end_block[:end_block.find("}") + 1]
        for index in range(block[0] + 1, len(file_contents)):
            if end_block in file_contents[index]:
                break
            if file_contents[index] != "":
                file_contents[index] = file_contents[index].rjust(len(file_contents[index]) + spaces)

    return file_contents

def lint_sentences(file_contents, config):
    """Makes a new line after every sentence if it is not already on its own line

    Args:
        file_contents (str[]): the entirety of contents in a file
        config (dict): lint config

    Returns:
        str[]: file_contents but modified
    """
    if config["formatting"]["git_support"]["newline_after_sentence"]:
        lines_with_dots = [index for index, line in enumerate(file_contents) if ". " in line]
        for line in lines_with_dots:
            comment_index = file_contents[line].find("%")
            dot_indices = [m.start() for m in re.finditer(r"\.\s+", file_contents[line])]
            dot_indices_before = [x for x in dot_indices if (comment_index == -1 or x < comment_index) and x + 1 < len(file_contents[line])]
            between_brackets = [x.span() for x in re.finditer(r"(\{.*?\}|\(.*?\))", file_contents[line])]
            dot_before_comment = [x.span() for x in re.finditer(r"\.\s*\%", file_contents[line])]
            dots_to_remove = []
            if between_brackets:
                for dot_index, dot in enumerate(dot_indices_before):
                    for ignored in between_brackets:
                        if ignored[0] <= dot <= ignored[1]:
                            dots_to_remove.append(dot)
            if dot_before_comment:
                for dot_index, dot in enumerate(dot_indices_before):
                    for ignored in dot_before_comment:
                        if ignored[0] <= dot <= ignored[1]:
                            dots_to_remove.append(dot)
            for dot in dots_to_remove:
                dot_indices_before.remove(dot)
            for dot_index in dot_indices_before:
                file_contents[line] = file_contents[line][:dot_index + 1] + "\n" + file_contents[line][dot_index + 2:]
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
    blank_lines = config["formatting"]["blank_lines"]["nr"]
    # contents_string = "\n".join(file_contents)
    # expression = r"^\n*(\\(section|subsection)\{\w+\})"
    # new_lines = blank_lines * r"\n"
    # replacement = new_lines + r"\g<1>"
    # contents_string = re.sub(expression, replacement, contents_string, flags=re.MULTILINE)
    # file_contents = contents_string.split(r"\n")
    # return file_contents
    section_lines = [index for index, line in enumerate(file_contents) if r"\section" in line and index != 0]
    adjustment = 0
    for line_index in section_lines:
        real_index = line_index + adjustment
        current = real_index - 1
        current_blank_lines = 0
        while current >= 0 and file_contents[current] == "":
            current = current - 1
            current_blank_lines = current_blank_lines + 1
        if current_blank_lines < blank_lines:
            #add a few lines
            nr_lines_to_add = blank_lines - current_blank_lines
            file_contents = file_contents[:real_index] + ["" for _ in range(nr_lines_to_add)] + file_contents[real_index:]
            adjustment += nr_lines_to_add
        elif current_blank_lines > blank_lines:
            #remove a few lines
            nr_lines_to_remove = current_blank_lines - blank_lines
            file_contents = file_contents[:real_index - nr_lines_to_remove] + file_contents[real_index:]
            adjustment -= nr_lines_to_remove

    return file_contents