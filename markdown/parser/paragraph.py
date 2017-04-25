#!/usr/bin/env python
"""
The paragraph element.
"""
from .element import BlockElement


class Paragraph(BlockElement):

    _lines = []

    def __init__(self):
        super(Paragraph, self).__init__()
        self._lines = []

    def parse(self, code, index, auxiliary=None):
        if self._finished:
            return False, index
        start = index
        while index < len(code) and code[index] != '\n':
            index += 1
        line = code[start:index].lstrip()
        index += 1
        if line == '':
            if len(self._lines) == 0:
                return False, start
            else:
                self._finished = True
                self._lines[-1] = self._lines[-1].rstrip()
                return True, index
        self._lines.append(line)
        return True, index

    def get_inlines(self):
        return ['\n'.join(self._lines)]
