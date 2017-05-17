#!/usr/env/bin python
import unittest
from markdown.parser.base import ContainerElement


class TestElement(unittest.TestCase):

    def test_get_blocks(self):
        elem = ContainerElement()
        self.assertEqual([], elem.get_blocks())
        child = ContainerElement()
        elem.add_block(child)
        self.assertEqual([child], elem.get_blocks())
