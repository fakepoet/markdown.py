#!/usr/bin/env python
"""
The markdown parser.
"""
from .container import Container


class Parser(object):

    @staticmethod
    def parse(code, config=None):
        """
        Parse the given code string.

        Args:
            code: an UTF-8 encoded string.
            config: a dict.

        Returns:
            The parsed elements.
        """
        if config is None:
            config = {}
        container_parser = Container(config)
        container_parser.parse(code, 0)
        return container_parser.get_blocks()
