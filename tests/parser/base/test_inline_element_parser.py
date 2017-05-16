#!/usr/env/bin python
import unittest
from markdown.parser.base import InlineElementParser


class TestElement(unittest.TestCase):

    def test_line_num(self):
        parser = InlineElementParser(dict())
        self.assertEqual((None, 0), parser.parse('', 0))
