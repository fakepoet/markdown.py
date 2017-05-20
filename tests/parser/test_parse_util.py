#!/usr/env/bin python
# coding=utf-8

import unittest
from markdown.parser.parse_util import ParseUtil


class TestParseUtil(unittest.TestCase):

    def test_get_heading_space_num(self):
        num = ParseUtil.get_heading_space_num(' \t a', 0)
        self.assertEqual(6, num)
        num = ParseUtil.get_heading_space_num(' \t a', 1)
        self.assertEqual(5, num)
        num = ParseUtil.get_heading_space_num(' \t a', 2)
        self.assertEqual(1, num)
        num = ParseUtil.get_heading_space_num(' \t a', 3)
        self.assertEqual(0, num)

    def test_is_white_space(self):
        self.assertTrue(ParseUtil.is_white_space(' '))
        self.assertTrue(ParseUtil.is_white_space('\t'))
        self.assertFalse(ParseUtil.is_white_space('a'))
        self.assertFalse(ParseUtil.is_white_space(u'\u1680'))

    def test_is_unicode_white_space(self):
        self.assertTrue(ParseUtil.is_unicode_white_space(' '))
        self.assertTrue(ParseUtil.is_unicode_white_space('\t'))
        self.assertFalse(ParseUtil.is_unicode_white_space('a'))
        self.assertTrue(ParseUtil.is_unicode_white_space(u'\u1680'))

    def test_is_ascii_punctuation(self):
        self.assertFalse(ParseUtil.is_ascii_punctuation(' '))
        self.assertTrue(ParseUtil.is_ascii_punctuation('@'))
        self.assertFalse(ParseUtil.is_ascii_punctuation(u'\u2046'))

    def test_is_punctuation(self):
        self.assertFalse(ParseUtil.is_punctuation(' '))
        self.assertTrue(ParseUtil.is_punctuation('@'))
        self.assertTrue(ParseUtil.is_punctuation(u'\u2046'))
