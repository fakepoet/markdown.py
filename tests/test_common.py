#!/usr/env/bin python
# coding=utf-8
import os
import codecs
import unittest
from markdown import Parser
from markdown import CommonHTMLPrinter


class TestCommon(unittest.TestCase):

    def check(self, index):
        path = os.path.join('cases', 'common')
        if not os.path.exists(path):
            path = os.path.join('tests', path)
        input_path = os.path.join(path, str(index) + '.in')
        with codecs.open(input_path, 'r', 'utf8') as reader:
            standard_input = reader.read()
        output_path = os.path.join(path, str(index) + '.out')
        with codecs.open(output_path, 'r', 'utf8') as reader:
            standard_output = reader.read()
        parsed = Parser.parse(standard_input)
        html = str(CommonHTMLPrinter(parsed))
        self.assertEqual(standard_output, html, 'Common: ' + str(index))

    def test_commons(self):
        intervals = [
            (52, 53),
            (55, 56),
            (180, 184),
        ]
        for interval in intervals:
            for index in range(interval[0], interval[1] + 1):
                self.check(index)
