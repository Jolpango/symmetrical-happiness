"""
Tests the unordered list class
"""

import unittest
from linter import lint
from linter import config_manager

class TestCommentRule(unittest.TestCase):
    """ Submodule for unittests, derives from unittest.TestCase """

    def test_sentence_splitting(self):
        """
        Test splitting sentences. Tests edge cases
        """
        test_contents = [
            r"This is a sentence. This is a sentence after a sentence. % this is a. comment",
            r"Is this a sentence? This is a \href{https://url.se} url {in} a sentence.",
            r"This is sentence! This is a sentence with a number 3.14. % also comment"
        ]
        expected = [
            r"This is a sentence.",
            r"This is a sentence after a sentence. % this is a. comment",
            r"Is this a sentence?",
            r"This is a \href{https://url.se} url {in} a sentence.",
            r"This is sentence!",
            r"This is a sentence with a number 3.14. % also comment"
        ]
        cfg = config_manager.default_config()
        output = lint.lint_sentences(test_contents, cfg)
        self.assertEqual(output, expected)
