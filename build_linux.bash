#!/usr/bin/env bash

$(pyinstaller linter/shlint.py -F --distpath bin/linux_x64)
