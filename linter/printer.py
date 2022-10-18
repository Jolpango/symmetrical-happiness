""" Module for printing information
"""

HELP_TEXT = """
\033[1mWelcome to the LaTeX linter symmetrical-happiness\033[0m
-------------------------------------------------
This linter only accepts .tex files

The linter will load config from "sh_config.yaml" in your current directory, if it doesnt exist it will be generated

\033[1mUsage:\033[0m
    shlint [options...] [arguments..]
\033[1mOptions:\033[0m
    -h, --help      -> displays helpful information on how to use this program
    -o, --overwrite -> formats your original files
    -r, --reset     -> resets the config file, not reversable
\033[1mArguments:\033[0m
    <filename>      -> lints the file
    <directory>/    -> lints all .tex files in directory and sub-directory

Written by: Joel Funk Persson 2022
"""
def usage():
    """Prints help text
    """
    print(HELP_TEXT)

def unrecognized(arg: str):
    """Prints a message explaining what argument didnt work

    Args:
        arg (str): the argument that wasnt recognized
    """
    print(f"{arg} is an unrecognized command or not a .tex-file/directory.")
    print("Use -h or --help for help")

def problem_fixed(problem: str, file_path: str):
    """prints a message stating that a problem was fixed

    Args:
        problem (str): description of problem
        file (str): file path with problem
    """
    print(f"    • Problem <{problem}> in <{file_path}> has been fixed")

def generate_config():
    """prints message saying that new config has been generated
    """
    print("New config file has been generated or old one was overwritten")

def config_loaded():
    """_summary_
    """
    print("Existing config found")

def overwrite_enabled():
    """_summary_
    """
    print("Overwriting has been forced.")
