#!/usr/bin/env python
"""
The bullet list element.
"""
from markdown.parser.containers.list_parser import ListParser


class BulletListParser(ListParser):

    def __init__(self, config):
        super(BulletListParser, self).__init__(config)

    def parse(self, code, index, auxiliary=None):
        pass
