#!/usr/env/bin python
# coding=utf-8
import os
import codecs
import unittest
from markdown import Parser
from markdown import CommonHTMLPrinter


class TestCommon(unittest.TestCase):

    def print_tree(self, node, indent=0):
        print(' ' * indent + str(node))
        if hasattr(node, 'subs'):
            for sub in node.subs:
                self.print_tree(sub, indent + 4)

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
        parser = Parser()
        parsed = parser.parse(standard_input)
        html = str(CommonHTMLPrinter(parsed))
        message = 'Common: ' + str(index) + '\n'
        message += '=' * 80 + '\n'
        message += standard_output
        message += '-' * 80 + '\n'
        message += html
        message += '=' * 80 + '\n'
        self.print_tree(parsed)
        self.assertEqual(standard_output, html, message)

    def test_commons(self):
        intervals = [
            (13, 17),
            (19, 25),
            (28, 29),
            (32, 34),
            (37, 38),
            (40, 45),
            (47, 49),
            (52, 53),
            (55, 56),
            (180, 184),
        ]
        for interval in intervals:
            for index in range(interval[0], interval[1] + 1):
                self.check(index)
