#!/usr/env/bin python
import unittest
from tests.parser.test_paragraph import TestParagraph
from markdown.printer.common_html_printer import CommonHTMLPrinter


class TestSetext(unittest.TestCase):

    def test_common__0_27__52(self):
        code = 'Foo\n-------------------------\n\nFoo\n='
        paragraphs = TestParagraph.parse_paragraphs(code)
        printer = CommonHTMLPrinter(paragraphs)
        html = str(printer)
        self.assertEqual('<h2>Foo</h2>\n<h1>Foo</h1>\n', html)

    def test_common__0_27__53(self):
        code = '   Foo\n---\n\n  Foo\n-----\n\n  Foo\n  ==='
        paragraphs = TestParagraph.parse_paragraphs(code)
        printer = CommonHTMLPrinter(paragraphs)
        html = str(printer)
        self.assertEqual('<h2>Foo</h2>\n<h2>Foo</h2>\n<h1>Foo</h1>\n', html)

    def test_common__0_27__55(self):
        code = 'Foo\n   ----      '
        paragraphs = TestParagraph.parse_paragraphs(code)
        printer = CommonHTMLPrinter(paragraphs)
        html = str(printer)
        self.assertEqual('<h2>Foo</h2>\n', html)

    def test_common__0_27__56(self):
        code = 'Foo\n    ----      '
        paragraphs = TestParagraph.parse_paragraphs(code)
        printer = CommonHTMLPrinter(paragraphs)
        html = str(printer)
        self.assertEqual('<p>Foo\n----</p>\n', html)

    def test_common__0_27__57_a(self):
        code = 'Foo\n= ='
        paragraphs = TestParagraph.parse_paragraphs(code)
        printer = CommonHTMLPrinter(paragraphs)
        html = str(printer)
        self.assertEqual('<p>Foo\n= =</p>\n', html)
