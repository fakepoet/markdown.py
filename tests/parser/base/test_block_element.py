#!/usr/env/bin python
import unittest
from markdown.parser.base import BlockElement


class TestElement(unittest.TestCase):

    def test_line_num(self):
        elem = BlockElement()
        self.assertFalse(elem.is_closed())
        elem.close()
        self.assertTrue(elem.is_closed())
