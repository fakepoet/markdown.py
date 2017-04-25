#!/usr/env/bin python
import unittest
from tests.parser.test_paragraph import TestParagraph
from markdown.printer.common_html_printer import CommonHTMLPrinter


class TestCommonHTMLPrinterParagraph(unittest.TestCase):

    def test_common__0_27__180(self):
        code = 'aaa\n\nbbb'
        paragraphs = TestParagraph.parse_paragraphs(code)
        printer = CommonHTMLPrinter(paragraphs)
        html = str(printer)
        self.assertEqual('<p>aaa</p>\n<p>bbb</p>\n', html)

    def test_common__0_27__181(self):
        code = 'aaa\nbbb\n\nccc\nddd'
        paragraphs = TestParagraph.parse_paragraphs(code)
        printer = CommonHTMLPrinter(paragraphs)
        html = str(printer)
        self.assertEqual('<p>aaa\nbbb</p>\n<p>ccc\nddd</p>\n', html)

    def test_common__0_27__182(self):
        code = 'aaa\n\n\nbbb'
        paragraphs = TestParagraph.parse_paragraphs(code)
        printer = CommonHTMLPrinter(paragraphs)
        html = str(printer)
        self.assertEqual('<p>aaa</p>\n<p>bbb</p>\n', html)

    def test_common__0_27__183(self):
        code = ' aaa\nbbb'
        paragraphs = TestParagraph.parse_paragraphs(code)
        printer = CommonHTMLPrinter(paragraphs)
        html = str(printer)
        self.assertEqual('<p>aaa\nbbb</p>\n', html)

    def test_common__0_27__184(self):
        code = 'aaa\n             bbb\n                                       ccc'
        paragraphs = TestParagraph.parse_paragraphs(code)
        printer = CommonHTMLPrinter(paragraphs)
        html = str(printer)
        self.assertEqual('<p>aaa\nbbb\nccc</p>\n', html)
