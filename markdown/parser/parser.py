#!/usr/bin/env python
"""
The markdown parser.
"""
from .container import Container
from .paragraph import Paragraph


class Parser(object):

    def __init__(self):
        self._block_parsers = [      # Block parsers.
            Container,
            Paragraph,
        ]
        self._config = {             # The configuration of the parser.
            'gfm': False             # Enable GitHub Flavored Markdown.
        }
        self._link_references = []   # The references to links.
        self._link_definitions = {}  # Link reference definitions.
        self._blocks = []            # The parsed Markdown block elements.

    def config(self, key, value):
        """
        Update parsing configuration.

        Args:
            key: a string.
            value: a string.

        Returns:
            A bool value indicates the existence of the key.
        """
        if key in self._config:
            self._config[key] = value
            return True
        return False

    def parse(self, code):
        """
        Parse the given code string.

        Args:
            code: an UTF-8 encoded string.

        Returns:
            The parsed elements.
        """
        index = 0
        while index < len(code):
            for block_parser_class in self._block_parsers:
                block_parser = block_parser_class.__init__()
                success, index = block_parser.parse(code, index)
                if success:
                    self._blocks.append(block_parser)
        return self._blocks
