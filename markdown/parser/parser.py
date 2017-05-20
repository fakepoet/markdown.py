#!/usr/bin/env python
"""
The markdown parser.
"""
from markdown.parser.containers.container_parser import ContainerParser


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
        # Replace insecure characters
        code = code.replace(u'\u0000', u'\uFFFD')
        # Replace line endings with newline (U+000A) character
        code = code.replace('\r\n', '\n').replace('\r', '\n')
        # Add a newline character to the end of code
        if len(code) > 0 and code[-1] != '\n':
            code += '\n'
        config['link_references'] = {}
        config['links'] = []
        container_parser = ContainerParser(config)
        container_parser.parse(code)
        return container_parser.get_blocks()
