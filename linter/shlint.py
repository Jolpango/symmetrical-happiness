"""
Main module of symmetrical-happiness the LaTeX-linter

- Joel Funk Persson 2022
"""
import time
import sys
import printer
import lint
import config_manager

def main():
    """Main program of symmetrical-happiness
    """
    # If no arguments, print help
    sys.argv.pop(0)
    if len(sys.argv) < 1:
        printer.help()
        sys.exit(1)
    files = []
    directories = []
    config = config_manager.load_config()
    for _, arg in enumerate(sys.argv):
        if arg in ["-h", "--help"]:
            printer.usage()
            sys.exit(0)
        elif arg in ["-o", "--overwrite"]:
            config["overwrite"] = True
            printer.overwrite_enabled()
        elif arg in ["-r", "--reset"]:
            config = config_manager.generate_config()
            sys.exit(0)
        elif arg.endswith("/") or arg.endswith(r"\\"):
            if arg not in directories:
                directories.append(arg)
        elif arg.endswith((".tex")):
            if arg not in files:
                files.append(arg)
        else:
            printer.unrecognized(arg)
            sys.exit(0)

    start = time.time()

    for file_path in files:
        lint.lint_file(file_path, config)

    for dir_path in directories:
        lint.lint_directory(dir_path, config)

    end = time.time()
    time_ms = round((end - start) * 1000, 2)
    print(f"Time elapsed: {time_ms}ms")


if __name__ == "__main__":
    main()
