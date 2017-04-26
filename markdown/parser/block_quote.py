#!/usr/bin/env python
"""
The block quote element.
"""
from .container import Container


class BlockQuote(Container):

    def __init__(self):
        super(BlockQuote, self).__init__()

    def parse(self, code, index, auxiliary=None):
        pass
