#!/usr/bin/env python
"""
The ordered list element.
"""
from markdown.parser.containers.list_parser import ListParser


class OrderedListParser(ListParser):

    def __init__(self, config):
        super(OrderedListParser, self).__init__(config)

    def parse(self, code, index, auxiliary=None):
        pass
