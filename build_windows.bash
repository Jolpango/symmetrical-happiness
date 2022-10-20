#!/usr/bin/env bash

$(pyinstaller linter/shlint.py -F --distpath bin/windows_x64)
