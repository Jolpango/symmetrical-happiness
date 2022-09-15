def lint_file(file_path: str, config):
    print("linting file <" + file_path + ">")

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