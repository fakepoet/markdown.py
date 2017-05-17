#!/usr/bin/env python
from markdown.parser.base import ContainerElementParser


class BlockQuoteParser(ContainerElementParser):
    """
    The block quote parser.
    """

    def __init__(self, config):
        super(BlockQuoteParser, self).__init__(config)

    def parse(self, code, index, auxiliary=None):
        return None, index
