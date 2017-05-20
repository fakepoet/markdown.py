#!/usr/bin/env python
# coding=utf-8


class Printer(object):
    """The abstract printer class."""

    def __init__(self, blocks):
        self._blocks = blocks

    def __str__(self):
        """
        Generate HTML output.

        Returns:
            HTML string.
        """
        return ''
