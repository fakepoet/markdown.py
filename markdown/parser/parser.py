#!/usr/bin/env python
"""
The markdown parser.
"""


class Parser(object):

    def __init__(self):
        self._config = {             # The configuration of the parser.
            'gfm': False             # Enable GitHub Flavored Markdown
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
        return self._blocks
