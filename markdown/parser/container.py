#!/usr/bin/env python
"""
Container (block quotes and lists) parser.
"""
from .element import BlockElement
from .paragraph import Paragraph


class Container(BlockElement):

    def __init__(self, config):
        super(Container, self).__init__(config)
        self._blocks = []  # The parsed block elements.
        self._container_parsers = [
            # BlockQuote,
            # BulletList,
            # OrderedList,
        ]
        self._block_parsers = [
            Paragraph
        ]

    def parse(self, code, index, auxiliary=None):
        index = 0
        while index < len(code):
            # Continuation
            if len(self._blocks) > 0 and not self._blocks[-1].is_closed():
                success, index = self._blocks[-1].parse(code, index)
                if not self._blocks[-1].is_closed():
                    continue
            # Try container parsers
            # Try block parsers
            for block_parser_class in self._block_parsers:
                block_parser = block_parser_class(self._config)
                success, index = block_parser.parse(code, index)
                if success:
                    self._blocks.append(block_parser)
                    break
        if len(self._blocks) > 0:
            self._blocks[-1].close()

    def get_blocks(self):
        return self._blocks
