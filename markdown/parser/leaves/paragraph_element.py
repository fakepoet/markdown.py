#!/usr/bin/env python
from markdown.parser.base import BlockElement


class ParagraphElement(BlockElement):
    """
    The paragraph element.
    """

    def __init__(self, config):
        super(ParagraphElement, self).__init__(config)
        self._lines = []     # The lines of the paragraph.
        self._tight = False  # Whether the paragraph is tight in a list item.
        self._level = 0      # 0 if it is not a setext heading, otherwise it could be 1 or 2.

    def append(self, line):
        self._lines.append(line)

    def close(self):
        super(ParagraphElement, self).close()
        self._lines[-1] = self._lines[-1].rstrip()

    def get_inlines(self):
        return ['\n'.join(self._lines)]

    def set_tight(self, tight):
        self._tight = tight

    def is_tight(self):
        return self._tight

    def is_setext(self):
        return self._level != 0

    def get_level(self):
        return self._level
