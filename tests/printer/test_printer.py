#!/usr/env/bin python
import unittest
from markdown.printer.printer import Printer


class TestPrinter(unittest.TestCase):

    def test_str(self):
        self.assertEqual('', str(Printer([])))
