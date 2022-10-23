# Symmetrical-Happiness LaTeX Linter
<img src="logo.png">

A LaTeX linter written in python

## Requirements

* No special requirements needed if you have a 64-bit Linux or Windows.
* You can run the source code yourself with python3

## Features

* Lint all files in directories and subdirectories
* Configurable linter rules
* Overwrite or create new files
* It can fix indentation
* Sentence linting for better git support
* Comment linting
* Blank lines before sections

## Installation

1. Download the binary for your system.*
2. Put the binary file somewhere. Preferably in your project folder.
3. Run the program from your command-line.

\* If there is not a binary for your system you can compile it yourself.
Clone the reposotory. Use pyinstaller to compile the file shlint.py.
For pyinstaller to work correctly you need to remove the file linter/__init\__.py

<a href="https://pyinstaller.org/en/stable/index.html">Link to pyinstaller</a>

    pyinstaller linter/shlint.py -F --distpath bin/linux_x64


## Usage

    shlint [options...] [arguments..]

    Options:
        -h, --help      -> displays helpful information on how to use this program
        -o, --overwrite -> formats your original files
        -r, --reset     -> resets the config file, not reversable
    Arguments:
        <filename>      -> lints the file
        <directory>/    -> lints all .tex files in directory and sub-directory

### Configuration

Symmetrical-Happiness load a configuration file from your current location in your command line. If there is none, a default one will be generated for you.

With the configuration file you can change how the rules are applied. For example how many spaces you want to indent blocks with, and which blocks should be excluded.

## Built using
### pyinstaller
    Used to compile the code into a single binary.

### python3
    pyyaml - Parses the yaml config file.
    glob - Used to recursively find .tex files in directories and sub-directories.
    re - Regex for matching and replacing text.
    sys - Used to get arguments passed from user.
    os - Used to create directories.
    unittest - Used to test functionality of linter rules.

## Tests
Every linter rule is unit tested. To run the test, run the file test.py
All tests are located in the tests folder

    python3 test.py