#!/usr/bin/env python
"""
The abstract printer class.
"""


class Printer(object):

    def __init__(self, blocks):
        self._blocks = blocks

    def __str__(self):
        """
        Generate HTML output.

        Returns:
            HTML string.
        """
        return ''
