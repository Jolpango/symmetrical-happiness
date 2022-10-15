"""
Tests the unordered list class
"""

import unittest
from linter import lint
from linter import config_manager

class TestCommentRule(unittest.TestCase):
    """ Submodule for unittests, derives from unittest.TestCase """

    def test_comment_few_spaces(self):
        """
        Test adding spaces to not enough spaces
        """
        test_contents = [
            r"hello %aioushduasd",
            r"hello %aioushduasd",
            r"%aioushduasd",
        ]
        expected = [
            r"hello % aioushduasd",
            r"hello % aioushduasd",
            r"% aioushduasd",
        ]
        cfg = config_manager.default_config()
        output = lint.lint_comments(test_contents, cfg)
        self.assertEqual(output, expected)

    def test_comment_many_spaces(self):
        """
        Test removing spaces after % sign when there is to many
        """
        test_contents = [
            r"hello %         aioushduasd",
            r"hello      %  aioushduasd",
            r"%              aioushduasd",
        ]
        expected = [
            r"hello % aioushduasd",
            r"hello      % aioushduasd",
            r"% aioushduasd",
        ]
        cfg = config_manager.default_config()
        output = lint.lint_comments(test_contents, cfg)
        self.assertEqual(output, expected)

