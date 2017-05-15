#!/usr/env/bin python
import unittest
from markdown import Parser
from markdown import CommonHTMLPrinter


class TestCommonHTMLPrinterThematicBreak(unittest.TestCase):

    def test_common__0_27__13(self):
        code = '***\n---\n___'
        paragraphs = Parser.parse(code)
        html = str(CommonHTMLPrinter(paragraphs))
        self.assertEqual('<hr />\n<hr />\n<hr />\n', html)

    def test_common__0_27__14(self):
        code = '+++'
        paragraphs = Parser.parse(code)
        html = str(CommonHTMLPrinter(paragraphs))
        self.assertEqual('<p>+++</p>\n', html)

    def test_common__0_27__15(self):
        code = '==='
        paragraphs = Parser.parse(code)
        html = str(CommonHTMLPrinter(paragraphs))
        self.assertEqual('<p>===</p>\n', html)

    def test_common__0_27__16(self):
        code = '--\n**\n__'
        paragraphs = Parser.parse(code)
        html = str(CommonHTMLPrinter(paragraphs))
        self.assertEqual('<p>--\n**\n__</p>\n', html)

    def test_common__0_27__17(self):
        code = '***\n ***\n   ***'
        paragraphs = Parser.parse(code)
        html = str(CommonHTMLPrinter(paragraphs))
        self.assertEqual('<hr />\n<hr />\n<hr />\n', html)
