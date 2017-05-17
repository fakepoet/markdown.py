#!/usr/bin/env python
from markdown.parser.base import BlockElementParser
from markdown.parser.leaves.atx_heading_element import AtxHeadingElement


class AtxHeadingParser(BlockElementParser):
    """
    The ATX heading parser.
    """

    def __init__(self, config):
        super(AtxHeadingParser, self).__init__(config)

    def parse(self, code, index, auxiliary=None):
        # 0~3 spaces
        success, index = self.check_indent(code, index)
        if not success:
            return None
        # 1~6 `#`s
        if index >= len(code) or code[index] != '#':
            return None
        level = 0
        while index < len(code) and code[index] == '#':
            index += 1
            level += 1
        if level > 6:
            return None
        # May be empty
        if index == len(code):
            elem = AtxHeadingElement()
            elem.set_level(level)
            return elem
        # One space is required
        if code[index] != ' ':
            return None
        # The title body
        start = index
        while index < len(code) and code[index] != '\n':
            index += 1
        title = code[start:index].rstrip()
        # Remove arbitrary number of tailing `#`s
        for i in range(len(title) - 1, -1, -1):
            if title[i] == ' ':
                title = title[:i]
                break
            elif title[i] != '#':
                break
        title = title.strip()
        elem = AtxHeadingElement()
        elem.set_level(level)
        elem.set_title(title)
        return elem
