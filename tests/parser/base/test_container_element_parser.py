#!/usr/env/bin python
import unittest
from markdown.parser.base import ContainerElementParser


class TestElement(unittest.TestCase):

    def setUp(self):
        self.parser = ContainerElementParser(dict())

    def test_get_align(self):
        self.assertEqual(0, self.parser.get_align(None))
        self.assertEqual(0, self.parser.get_align(dict()))
        self.assertEqual(627, self.parser.get_align({
            ContainerElementParser.AUX_ALIGN: 627
        }))
