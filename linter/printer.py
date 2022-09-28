help_text = """
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