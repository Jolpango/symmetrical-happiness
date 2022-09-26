help_text = """
Welcome to the LaTeX linter symmetrical-happiness
-------------------------------------------------
This linter only accepts .tex files

The linter will load config from "sh_config.yaml", if it doesnt exist it will be generated

-h, --help      -> displays helpful information on how to use this program
-o, --overwrite -> formats your original files
-r, --reset     -> resets the config file, not reversable
<filename>      -> lints the file
<directory>/    -> lints all .tex files in directory and sub-directory

example         -> python3 shlint.py file.tex directory/ -o

Written by: Joel Funk Persson 2022
"""
def help():
    """Prints help text
    """
    print(help_text)

def unrecognized(arg: str):
    """Prints a message explaining what argument didnt work

    Args:
        arg (str): the argument that wasnt recognized
    """
    print(f"{arg} is an unrecognized command or not a .tex-file/directory.\nUse -h or --help for help")

def problem_fixed(problem: str):
    """prints a message stating that a problem was fixed

    Args:
        problem (str): _description_
    """
    print(problem + " fixed")