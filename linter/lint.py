"""This module will handle loading and linting of the files"""
import glob

def lint_file(file_path: str, config):
    """lints a file

    Args:
        file_path (str): path to the file
        config (_type_): config dictionary
    """
    print("linting file <" + file_path + ">")
    with open(file_path) as f:
        contents = f.read()
        # print(contents)

def lint_directory(directory: str, config):
    """lints all .tex files in directory and subdirectories

    Args:
        directory (str): _description_
        config (_type_): _description_
    """
    print("linting directory <" + directory + ">")
    # find files
    # call lint_file
    # find directories
    # call lint_directory
    files = glob.glob(f"{directory}**/*.tex", recursive=True)
    # print("Found these files:")
    # print(files)
    for file in files:
        lint_file(file, config)
