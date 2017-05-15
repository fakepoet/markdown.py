#!/usr/bin/env python
"""
The ATX heading element.
"""
from markdown.parser.util import BlockElement


class AtxHeading(BlockElement):

    def __init__(self, config):
        super(AtxHeading, self).__init__(config)
        self._level = 0
        self._title = ''

    def parse(self, code, index, auxiliary=None):
        start = index
        # 0~3 spaces
        success, index = self.check_indent(code, index)
        if not success:
            return False, start
        # 1~6 `#`s
        if index >= len(code) or code[index] != '#':
            return False, start
        self._level = 0
        while index < len(code) and code[index] == '#':
            index += 1
            self._level += 1
        if self._level > 6:
            return False, start
        # May be empty
        if index == len(code):
            return True, index
        if code[index] == '\n':
            return True, index + 1
        # One space is required
        if code[index] != ' ':
            return False, start
        # The title body
        start = index
        while index < len(code) and code[index] != '\n':
            index += 1
        self._title = code[start:index].rstrip()
        # Remove arbitrary number of tailing `#`s
        for i in range(len(self._title) - 1, -1, -1):
            if self._title[i] == ' ':
                self._title = self._title[:i]
                break
            elif self._title[i] != '#':
                break
        self._title = self._title.strip()
        self.close()
        return True, index + 1

    def get_level(self):
        return self._level

    def get_inlines(self):
        return [self._title]
