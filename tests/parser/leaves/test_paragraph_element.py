#!/usr/env/bin python
import unittest
from markdown.parser.leaves.paragraph_element import ParagraphElement


class TestParagraphElement(unittest.TestCase):

    def setUp(self):
        self.elem = ParagraphElement()

    def test_lines(self):
        self.assertEqual([], self.elem.get_lines())
        self.elem.append('GU Games')
        self.assertEqual(['GU Games'], self.elem.get_lines())
        self.elem.del_last_line()
        self.assertEqual([], self.elem.get_lines())

    def test_close_with_empty_lines(self):
        self.assertFalse(self.elem.is_closed())
        self.elem.close()
        self.assertEqual([], self.elem.get_lines())
        self.assertTrue(self.elem.is_closed())

    def test_close_strip(self):
        self.assertFalse(self.elem.is_closed())
        self.elem.append('GU Games    ')
        self.elem.close()
        self.assertEqual(['GU Games'], self.elem.get_lines())
        self.assertTrue(self.elem.is_closed())

    def test_tight(self):
        self.assertFalse(self.elem.is_tight())
        self.elem.set_tight(True)
        self.assertTrue(self.elem.is_tight())

    def test_setext(self):
        self.assertFalse(self.elem.is_setext())
        self.assertEqual(0, self.elem.get_level())
        self.elem.set_level(1)
        self.assertTrue(self.elem.is_setext())
        self.assertEqual(1, self.elem.get_level())
