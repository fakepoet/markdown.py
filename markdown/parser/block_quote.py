#!/usr/bin/env python
"""
The block quote element.
"""
from .container import Container


class BlockQuote(Container):

    def __init__(self, config):
        super(BlockQuote, self).__init__(config)

    def parse(self, code, index, auxiliary=None):
        pass
