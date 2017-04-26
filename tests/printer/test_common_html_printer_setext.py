#!/usr/env/bin python
import unittest
from markdown import Parser
from markdown import CommonHTMLPrinter


class TestSetext(unittest.TestCase):

    def test_common__0_27__52(self):
        code = 'Foo\n-------------------------\n\nFoo\n='
        paragraphs = Parser.parse(code)
        printer = CommonHTMLPrinter(paragraphs)
        html = str(printer)
        self.assertEqual('<h2>Foo</h2>\n<h1>Foo</h1>\n', html)

    def test_common__0_27__53(self):
        code = '   Foo\n---\n\n  Foo\n-----\n\n  Foo\n  ==='
        paragraphs = Parser.parse(code)
        printer = CommonHTMLPrinter(paragraphs)
        html = str(printer)
        self.assertEqual('<h2>Foo</h2>\n<h2>Foo</h2>\n<h1>Foo</h1>\n', html)

    def test_common__0_27__55(self):
        code = 'Foo\n   ----      '
        paragraphs = Parser.parse(code)
        printer = CommonHTMLPrinter(paragraphs)
        html = str(printer)
        self.assertEqual('<h2>Foo</h2>\n', html)

    def test_common__0_27__56(self):
        code = 'Foo\n    ----      '
        paragraphs = Parser.parse(code)
        printer = CommonHTMLPrinter(paragraphs)
        html = str(printer)
        self.assertEqual('<p>Foo\n----</p>\n', html)

    def test_common__0_27__57_a(self):
        code = 'Foo\n= ='
        paragraphs = Parser.parse(code)
        printer = CommonHTMLPrinter(paragraphs)
        html = str(printer)
        self.assertEqual('<p>Foo\n= =</p>\n', html)
