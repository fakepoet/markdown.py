#!/usr/bin/env python
"""
The markdown parser.
"""


class Parser(object):

    _config = {}            # The configuration of the parser.
    _link_references = []   # The references to links.
    _link_definitions = {}  # Link reference definitions.
    _blocks = []            # The parsed Markdown block elements.

    def __init__(self):
        self.reset()

    def reset(self):
        """
        Reset config and members.

        Returns:
            None
        """
        self._config = {
            'gfm': False    # Enable GitHub Flavored Markdown
        }
        self._link_references = []
        self._link_definitions = {}
        self._blocks = []

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
