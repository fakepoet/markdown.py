#!/usr/env/bin python
# coding=utf-8

import unittest
from markdown.printer.printer import Printer


class TestPrinter(unittest.TestCase):

    def test_str(self):
        self.assertEqual('', str(Printer([])))
