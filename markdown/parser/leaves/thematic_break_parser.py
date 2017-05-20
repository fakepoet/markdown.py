#!/usr/bin/env python
from markdown.parser.base import BlockElementParser
from markdown.parser.leaves.thematic_break_element import ThematicBreakElement


class ThematicBreakParser(BlockElementParser):
    """
    The thematic break parser.

    A line consisting of 0-3 spaces of indentation, followed by a
    sequence of three or more matching -, _, or * characters, each
    followed optionally by any number of spaces, forms a thematic break.
    """

    def __init__(self, config):
        super(ThematicBreakParser, self).__init__(config)

    def parse(self, code, index, auxiliary=None):
        success, index = self.check_indent(code, index)
        if not success:
            return None
        if index >= len(code):
            return None
        first = code[index]
        if first not in ['*', '-', '_']:
            return None
        count = 0
        has_space = False
        has_inner_space = False
        while index < len(code) and code[index] != '\n':
            if code[index] == first:
                count += 1
                if has_space:
                    has_inner_space = True
            elif code[index] in [' ', '\t']:
                has_space = True
            else:
                return None
            index += 1
        if count < 3:
            return None
        if self.is_interrupting(auxiliary) and first == '-' and not has_inner_space:
            return None
        return ThematicBreakElement()
