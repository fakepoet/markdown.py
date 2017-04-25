#!/usr/env/bin python
import unittest
from markdown.parser.paragraph import Paragraph


class TestParagraph(unittest.TestCase):

    @staticmethod
    def parse_paragraphs(code):
        paragraphs = []
        paragraph = Paragraph()
        index = 0
        while index < len(code):
            success, index = paragraph.parse(code, index)
            if not success:
                index += 1
            if paragraph.is_finished():
                paragraphs.append(paragraph)
                paragraph = Paragraph()
        if success:
            paragraphs.append(paragraph)
        return paragraphs

    def test_common__0_27__180(self):
        code = 'aaa\n\nbbb'
        paragraphs = TestParagraph.parse_paragraphs(code)
        self.assertEquals(2, len(paragraphs))
        self.assertEquals(['aaa'], paragraphs[0].get_inlines())
        self.assertEquals(['bbb'], paragraphs[1].get_inlines())

    def test_common__0_27__181(self):
        code = 'aaa\nbbb\n\nccc\nddd'
        paragraphs = TestParagraph.parse_paragraphs(code)
        self.assertEquals(2, len(paragraphs))
        self.assertEquals(['aaa\nbbb'], paragraphs[0].get_inlines())
        self.assertEquals(['ccc\nddd'], paragraphs[1].get_inlines())

    def test_common__0_27__182(self):
        code = 'aaa\n\n\nbbb'
        paragraphs = TestParagraph.parse_paragraphs(code)
        self.assertEquals(2, len(paragraphs))
        self.assertEquals(['aaa'], paragraphs[0].get_inlines())
        self.assertEquals(['bbb'], paragraphs[1].get_inlines())

    def test_common__0_27__183(self):
        code = ' aaa\nbbb'
        paragraphs = TestParagraph.parse_paragraphs(code)
        self.assertEquals(1, len(paragraphs))
        self.assertEquals(['aaa\nbbb'], paragraphs[0].get_inlines())

    def test_common__0_27__184(self):
        code = 'aaa\n             bbb\n                                       ccc'
        paragraphs = TestParagraph.parse_paragraphs(code)
        self.assertEquals(1, len(paragraphs))
        self.assertEquals(['aaa\nbbb\nccc'], paragraphs[0].get_inlines())
