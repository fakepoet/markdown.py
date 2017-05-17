#!/usr/bin/env python
from markdown.parser.base import BlockElement


class SetextHeadingElement(BlockElement):
    """
    The setext heading element.
    """

    def __init__(self):
        super(SetextHeadingElement, self).__init__()
        self.close()
        self._lines = []     # The lines of the setext heading.
        self._level = 1      # 1 or 2.

    def set_lines(self, lines):
        self._lines = lines

    def set_level(self, level):
        self._level = level

    def get_level(self):
        return self._level

    def get_inlines(self):
        return ['\n'.join(self._lines)]
