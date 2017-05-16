#!/usr/env/bin python
import unittest

from markdown import Parser
from markdown.parser.leaves import ParagraphElement
from markdown.parser.leaves import ThematicBreakElement


class TestThematicBreak(unittest.TestCase):

    def test_common__0_27__13(self):
        code = '***\n---\n___'
        elements = Parser.parse(code)
        self.assertEqual(3, len(elements))
        self.assertTrue(isinstance(elements[0], ThematicBreakElement))
        self.assertTrue(isinstance(elements[1], ThematicBreakElement))
        self.assertTrue(isinstance(elements[2], ThematicBreakElement))

    def test_common__0_27__14(self):
        code = '+++'
        elements = Parser.parse(code)
        self.assertEqual(1, len(elements))
        self.assertTrue(isinstance(elements[0], ParagraphElement))

    def test_common__0_27__15(self):
        code = '==='
        elements = Parser.parse(code)
        self.assertEqual(1, len(elements))
        self.assertTrue(isinstance(elements[0], ParagraphElement))

    def test_common__0_27__16(self):
        code = '--\n**\n__'
        elements = Parser.parse(code)
        self.assertEqual(1, len(elements))
        self.assertTrue(isinstance(elements[0], ParagraphElement))

    def test_common__0_27__17(self):
        code = '***\n ***\n   ***'
        elements = Parser.parse(code)
        self.assertEqual(3, len(elements))
        self.assertTrue(isinstance(elements[0], ThematicBreakElement))
        self.assertTrue(isinstance(elements[1], ThematicBreakElement))
        self.assertTrue(isinstance(elements[2], ThematicBreakElement))

    def test_common__0_27__28(self):
        code = 'Foo\n***\nbar'
        elements = Parser.parse(code)
        self.assertEqual(3, len(elements))
        self.assertTrue(isinstance(elements[0], ParagraphElement))
        self.assertTrue(isinstance(elements[1], ThematicBreakElement))
        self.assertTrue(isinstance(elements[2], ParagraphElement))

    def test_common__0_27__29(self):
        code = 'Foo\n---\nbar'
        elements = Parser.parse(code)
        self.assertEqual(2, len(elements))
        self.assertTrue(isinstance(elements[0], ParagraphElement))
        self.assertTrue(isinstance(elements[1], ParagraphElement))
