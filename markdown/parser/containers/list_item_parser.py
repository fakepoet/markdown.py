#!/usr/bin/env python
"""
The block quote element.
"""
from markdown.parser.base.block_element_parser import BlockElementParser


class BlockQuoteParser(BlockElementParser):

    def __init__(self, config):
        super(BlockQuoteParser, self).__init__(config)

    def parse(self, code, index, auxiliary=None):
        return None, index
