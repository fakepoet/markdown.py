#!/usr/env/bin python
import unittest
from markdown import Parser
from markdown import CommonHTMLPrinter


class TestCommonHTMLPrinterParagraph(unittest.TestCase):

    def test_common__0_27__180(self):
        code = 'aaa\n\nbbb'
        paragraphs = Parser.parse(code)
        html = str(CommonHTMLPrinter(paragraphs))
        self.assertEqual('<p>aaa</p>\n<p>bbb</p>\n', html)

    def test_common__0_27__181(self):
        code = 'aaa\nbbb\n\nccc\nddd'
        paragraphs = Parser.parse(code)
        html = str(CommonHTMLPrinter(paragraphs))
        self.assertEqual('<p>aaa\nbbb</p>\n<p>ccc\nddd</p>\n', html)

    def test_common__0_27__182(self):
        code = 'aaa\n\n\nbbb'
        paragraphs = Parser.parse(code)
        html = str(CommonHTMLPrinter(paragraphs))
        self.assertEqual('<p>aaa</p>\n<p>bbb</p>\n', html)

    def test_common__0_27__183(self):
        code = ' aaa\nbbb'
        paragraphs = Parser.parse(code)
        html = str(CommonHTMLPrinter(paragraphs))
        self.assertEqual('<p>aaa\nbbb</p>\n', html)

    def test_common__0_27__184(self):
        code = 'aaa\n             bbb\n                                       ccc'
        paragraphs = Parser.parse(code)
        html = str(CommonHTMLPrinter(paragraphs))
        self.assertEqual('<p>aaa\nbbb\nccc</p>\n', html)
