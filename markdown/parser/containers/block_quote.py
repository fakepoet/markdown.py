#!/usr/bin/env python
"""
The block quote element.
"""
from markdown.parser.containers.container import Container


class BlockQuote(Container):

    def __init__(self, config):
        super(BlockQuote, self).__init__(config)

    def parse(self, code, index, auxiliary=None):
        pass
