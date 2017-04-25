#!/usr/bin/env python
"""
The block quote element.
"""
from .element import BlockElement


class BlockQuote(BlockElement):

    def __init__(self):
        super(BlockQuote, self).__init__()

    def parse(self, code, index, auxiliary=None):
        pass
