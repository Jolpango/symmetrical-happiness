"""
Tests the unordered list class
"""

import unittest
from linter import lint
from linter import config_manager

class TestIndentationRule(unittest.TestCase):
    """ Submodule for unittests, derives from unittest.TestCase """

    def test_indent(self):
        """
        Test adding and removing indentation
        """
        test_contents = [
            r"\begin{document}",
            r"hello %aioushduasd",
            r"\begin{outer}",
            r"\begin{inner}",
            r"aioushduasd",
            r"%aioushduasd",
            r"\end{inner}",
            r"\end{outer}",
            r"\begin{outer}",
            r"\begin{inner}",
            r"              aioushduasd",
            r"                        %aioushduasd",
            r"            \end{inner}",
            r"            \end{outer}",
            r"%aioushduasd",
            r"%aioushduasd",
            r"\end{document}",
        ]
        expected = [
            r"\begin{document}",
            r"hello %aioushduasd",
            r"\begin{outer}",
            r"    \begin{inner}",
            r"        aioushduasd",
            r"        %aioushduasd",
            r"    \end{inner}",
            r"\end{outer}",
            r"\begin{outer}",
            r"    \begin{inner}",
            r"        aioushduasd",
            r"        %aioushduasd",
            r"    \end{inner}",
            r"\end{outer}",
            r"%aioushduasd",
            r"%aioushduasd",
            r"\end{document}",
        ]
        cfg = config_manager.default_config()
        output = lint.lint_indentation(test_contents, cfg)
        self.assertEqual(output, expected)
