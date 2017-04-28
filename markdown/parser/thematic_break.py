#!/usr/bin/env python
"""
The thematic break element.
"""
from .element import BlockElement


class ThematicBreak(BlockElement):

    def __init__(self, config):
        super(ThematicBreak, self).__init__(config)
        self.close()

    def parse(self, code, index, auxiliary=None):
        interrupting = False
        if auxiliary is not None \
                and self.AUX_INTERRUPT in auxiliary \
                and auxiliary[self.AUX_INTERRUPT]:
            interrupting = True
        start = index
        success, index = self.check_indent(code, index)
        if not success:
            return False, start
        if index >= len(code):
            return False, start
        first = code[index]
        if first not in ['*', '-', '_']:
            return False, start
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
                return False, start
            index += 1
        if count < 3:
            return False, start
        if interrupting and first == '-' and not has_inner_space:
            return False, start
        return True, index + 1
