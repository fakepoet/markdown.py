#!/usr/bin/env python
from markdown.parser.base import BlockElement


class AtxHeadingElement(BlockElement):
    """
    The ATX heading element.
    """

    def __init__(self):
        super(AtxHeadingElement, self).__init__()
        self.close()
        self._title = ''
        self._level = 1

    def get_inlines(self):
        return [self._title]

    def set_title(self, title):
        self._title = title

    def set_level(self, level):
        self._level = level

    def get_level(self):
        return self._level
