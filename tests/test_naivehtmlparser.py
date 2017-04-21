#!/usr/env/bin python
# coding: utf-8
import os
import codecs
import unittest
from naivehtmlparser import NaiveHTMLParser


class TestNaiveHTMLParser(unittest.TestCase):

    def setUp(self):
        self.parser = NaiveHTMLParser()

    def test_doc_example(self):
        text = '<tag key1="val1" key2>text</tag>'
        self.parser.parse(text)
        expect = {
            'elem': 'body',
            'children': [
                {
                    'elem': ('tag', 'tag', {
                        'key1': 'val1',
                        'key2': None
                    }),
                    'children': [
                        ('text', 'text')
                    ]
                }
            ]
        }
        self.assertEqual(expect, self.parser.body)

    def test_no_except(self):
        path = os.path.join('cases', 'common')
        if not os.path.exists(path):
            path = os.path.join('tests', path)
        for name in os.listdir(path):
            file_path = os.path.join(path, name)
            if file_path[-4:] == '.out':
                with codecs.open(file_path, 'r', 'UTF-8') as reader:
                    self.parser.parse(reader.read())

    def test_common_122(self):
        text = u'<div id="foo"\n*hi*\n'
        self.parser.parse(text)
        expect = {
            'elem': 'body',
            'children': [
                {
                    'elem': ('tag', u'div', {
                        u'id': u'foo',
                        u'*hi*': None
                    }), 'children': []
                }
            ]
        }
        self.assertEqual(expect, self.parser.body)

    def test_common_295(self):
        text = u'<p><a href="http://example.com?find=%5C*">http://example.com?find=\\*</a></p>\n'
        self.parser.parse(text)
        expect = {
            'elem': 'body',
            'children': [
                {
                    'elem': ('tag', u'p', {}),
                    'children': [
                        {
                            'elem': ('tag', u'a', {
                                u'href': u'http://example.com?find=%5C*'
                            }),
                            'children': [
                                ('text', u'http://example.com?find=\\*')
                            ]
                        }
                    ]
                }
            ]
        }
        self.assertEqual(expect, self.parser.body)

    def test_common_308(self):
        text = u'<p><a href="/f%C3%B6%C3%B6" title="föö">foo</a></p>'
        self.parser.parse(text)
        expect = {
            'elem': 'body',
            'children': [
                {
                    'elem': ('tag', u'p', {}),
                    'children': [
                        {
                            'elem': ('tag', u'a', {
                                u'href': u'/f%C3%B6%C3%B6',
                                u'title': u'f\xf6\xf6'
                            }),
                            'children': [
                                ('text', u'foo')
                            ]
                        }
                    ]
                }
            ]
        }
        self.assertEqual(expect, self.parser.body)

    def test_common_424(self):
        text = u'<p>foo <em>*</em></p>'
        self.parser.parse(text)
        expect = {
            'elem': 'body',
            'children': [
                {
                    'elem': ('tag', u'p', {}),
                    'children': [
                        ('text', u'foo '),
                        {
                            'elem': ('tag', u'em', {}),
                            'children': [
                                ('text', u'*')
                            ]
                        }
                    ]
                }
            ]
        }
        self.assertEqual(expect, self.parser.body)

if __name__ == '__main__':
    unittest.main()
