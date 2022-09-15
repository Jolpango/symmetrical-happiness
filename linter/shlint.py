import sys
import printer
import lint

def main():
    # If no arguments, print help
    sys.argv.pop(0)
    if len(sys.argv) < 1:
        printer.help()
        exit(1)
    files = []
    directories = []
    config = {}
    for _, arg in enumerate(sys.argv):
        if arg in ["-h", "--help"]:
            printer.help()
        elif arg in ["-o", "--overwrite"]:
            config["overwrite"] = True
        elif arg.endswith("/"):
            directories.append(arg)
        elif arg.endswith((".tex")):
            files.append(arg)
        else:
            printer.unrecognized(arg)
    print("files:")
    print(files)
    print("directories:")
    print(directories)
    print("config:")
    print(config)
    for f in files:
        lint.lint_file(f, "")
    for d in directories:
        lint.lint_directory(d, "")


if __name__ == "__main__":
    main()
