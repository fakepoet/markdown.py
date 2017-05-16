#!/usr/env/bin python
import unittest
from markdown.parser.base import ElementParser


class TestElement(unittest.TestCase):

    def test_line_num(self):
        parser = ElementParser(dict())
        self.assertEqual((None, 0), parser.parse('', 0))
