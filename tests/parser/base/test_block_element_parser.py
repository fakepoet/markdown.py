#!/usr/env/bin python
import unittest
from markdown.parser.base import BlockElementParser


class TestElement(unittest.TestCase):

    def setUp(self):
        self.parser = BlockElementParser(dict())

    def test_line_num(self):
        self.assertEqual((None, 0), self.parser.parse('', 0))

    def test_get_unclosed(self):
        self.assertIsNone(self.parser.get_unclosed(None))
        self.assertIsNone(self.parser.get_unclosed(dict()))
        self.assertEqual('GU Games', self.parser.get_unclosed({
            BlockElementParser.AUX_UNCLOSED: 'GU Games'
        }))

    def test_is_interrupting(self):
        self.assertFalse(self.parser.is_interrupting(None))
        self.assertFalse(self.parser.is_interrupting(dict()))
        self.assertTrue(self.parser.is_interrupting({
            BlockElementParser.AUX_INTERRUPT: True
        }))
        self.assertFalse(self.parser.is_interrupting({
            BlockElementParser.AUX_INTERRUPT: False
        }))
