#!/usr/env/bin python
import unittest
from markdown import Parser
from markdown.parser.leaves.setext_heading_element import SetextHeadingElement


class TestSetext(unittest.TestCase):

    def test_common__0_27__52(self):
        code = 'Foo\n-------------------------\n\nFoo\n='
        paragraphs = Parser.parse(code)
        self.assertEqual(2, len(paragraphs))
        self.assertEqual(['Foo'], paragraphs[0].get_inlines())
        self.assertTrue(isinstance(paragraphs[0], SetextHeadingElement))
        self.assertEqual(2, paragraphs[0].get_level())
        self.assertEqual(['Foo'], paragraphs[1].get_inlines())
        self.assertTrue(isinstance(paragraphs[1], SetextHeadingElement))
        self.assertEqual(1, paragraphs[1].get_level())

    def test_common__0_27__53(self):
        code = '   Foo\n---\n\n  Foo\n-----\n\n  Foo\n  ==='
        paragraphs = Parser.parse(code)
        self.assertEqual(3, len(paragraphs))
        self.assertEqual(['Foo'], paragraphs[0].get_inlines())
        self.assertTrue(isinstance(paragraphs[0], SetextHeadingElement))
        self.assertEqual(2, paragraphs[0].get_level())
        self.assertEqual(['Foo'], paragraphs[1].get_inlines())
        self.assertTrue(isinstance(paragraphs[1], SetextHeadingElement))
        self.assertEqual(2, paragraphs[1].get_level())
        self.assertEqual(['Foo'], paragraphs[2].get_inlines())
        self.assertTrue(isinstance(paragraphs[2], SetextHeadingElement))
        self.assertEqual(1, paragraphs[2].get_level())

    def test_common__0_27__55(self):
        code = 'Foo\n   ----      '
        paragraphs = Parser.parse(code)
        self.assertEqual(1, len(paragraphs))
        self.assertEqual(['Foo'], paragraphs[0].get_inlines())
        self.assertTrue(isinstance(paragraphs[0], SetextHeadingElement))
        self.assertEqual(2, paragraphs[0].get_level())

    def test_common__0_27__56(self):
        code = 'Foo\n    ----      '
        paragraphs = Parser.parse(code)
        self.assertEqual(1, len(paragraphs))
        self.assertEqual(['Foo\n----'], paragraphs[0].get_inlines())
        self.assertFalse(isinstance(paragraphs[0], SetextHeadingElement))

    def test_common__0_27__57_a(self):
        code = 'Foo\n= ='
        paragraphs = Parser.parse(code)
        self.assertEqual(1, len(paragraphs))
        self.assertEqual(['Foo\n= ='], paragraphs[0].get_inlines())
        self.assertFalse(isinstance(paragraphs[0], SetextHeadingElement))

    def test_multi_line(self):
        code = 'a\nb\n==='
        paragraphs = Parser.parse(code)
        self.assertEqual(1, len(paragraphs))
        self.assertTrue(isinstance(paragraphs[0], SetextHeadingElement))
        self.assertEqual(['a\nb'], paragraphs[0].get_inlines())
