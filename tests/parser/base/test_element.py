#!/usr/env/bin python
import unittest
from markdown.parser.base import Element


class TestElement(unittest.TestCase):

    def test_line_num(self):
        elem = Element()
        elem.set_line_num(627)
        self.assertEqual(627, elem.line_num())

    def test_get_inlines(self):
        elem = Element()
        self.assertEqual([], elem.get_inlines())
