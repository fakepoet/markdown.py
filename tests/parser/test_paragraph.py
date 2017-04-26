#!/usr/env/bin python
import unittest
from markdown import Parser


class TestParagraph(unittest.TestCase):

    def test_common__0_27__180(self):
        code = 'aaa\n\nbbb'
        paragraphs = Parser.parse(code)
        self.assertEquals(2, len(paragraphs))
        self.assertEquals(['aaa'], paragraphs[0].get_inlines())
        self.assertEquals(['bbb'], paragraphs[1].get_inlines())

    def test_common__0_27__181(self):
        code = 'aaa\nbbb\n\nccc\nddd'
        paragraphs = Parser.parse(code)
        self.assertEquals(2, len(paragraphs))
        self.assertEquals(['aaa\nbbb'], paragraphs[0].get_inlines())
        self.assertEquals(['ccc\nddd'], paragraphs[1].get_inlines())

    def test_common__0_27__182(self):
        code = 'aaa\n\n\nbbb'
        paragraphs = Parser.parse(code)
        self.assertEquals(2, len(paragraphs))
        self.assertEquals(['aaa'], paragraphs[0].get_inlines())
        self.assertEquals(['bbb'], paragraphs[1].get_inlines())

    def test_common__0_27__183(self):
        code = ' aaa\nbbb'
        paragraphs = Parser.parse(code)
        self.assertEquals(1, len(paragraphs))
        self.assertEquals(['aaa\nbbb'], paragraphs[0].get_inlines())

    def test_common__0_27__184(self):
        code = 'aaa\n             bbb\n                                       ccc'
        paragraphs = Parser.parse(code)
        self.assertEquals(1, len(paragraphs))
        self.assertEquals(['aaa\nbbb\nccc'], paragraphs[0].get_inlines())
