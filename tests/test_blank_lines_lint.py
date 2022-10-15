"""
Tests the unordered list class
"""

import unittest
from linter import lint
from linter import config_manager

class TestBlankLinesRule(unittest.TestCase):
    """ Submodule for unittests, derives from unittest.TestCase """

    def test_too_few_blanklines(self):
        """
        Test adding blanklines where there is not enough
        """
        test_contents = [
            r"hello %aioushduasd",
            r"\section{aioushduasd}",
            r"%aioushduasd",
            r"hello %aioushduasd",
            r"hello %aioushduasd",
            r"%aioushduasd",
            r"\section{asd}",
            r"hello %aioushduasd",
            r"%aioushduasd",
        ]
        expected = [
            r"hello %aioushduasd",
            r"",
            r"\section{aioushduasd}",
            r"%aioushduasd",
            r"hello %aioushduasd",
            r"hello %aioushduasd",
            r"%aioushduasd",
            r"",
            r"\section{asd}",
            r"hello %aioushduasd",
            r"%aioushduasd",
        ]
        cfg = config_manager.default_config()
        output = lint.lint_blanklines(test_contents, cfg)
        self.assertEqual(output, expected)

    def test_too_many_blanklines(self):
        """
        Test adding blanklines where there is too many
        """
        test_contents = [
            r"hello %aioushduasd",
            r"",
            r"",
            r"",
            r"\section{aioushduasd}",
            r"%aioushduasd",
            r"hello %aioushduasd",
            r"hello %aioushduasd",
            r"%aioushduasd",
            r"",
            r"",
            r"",
            r"",
            r"",
            r"",
            r"",
            r"\section{asd}",
            r"hello %aioushduasd",
            r"%aioushduasd",
        ]
        expected = [
            r"hello %aioushduasd",
            r"",
            r"\section{aioushduasd}",
            r"%aioushduasd",
            r"hello %aioushduasd",
            r"hello %aioushduasd",
            r"%aioushduasd",
            r"",
            r"\section{asd}",
            r"hello %aioushduasd",
            r"%aioushduasd",
        ]
        cfg = config_manager.default_config()
        output = lint.lint_blanklines(test_contents, cfg)
        self.assertEqual(output, expected)
