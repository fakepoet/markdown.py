#!/usr/bin/env python
"""
Container (block quotes and lists) parser.
"""
from .element import BlockElement


class Container(BlockElement):

    def __init__(self):
        super(Container, self).__init__()

    def parse(self, code, index, auxiliary=None):
        pass
