#!/usr/bin/env python
"""
The paragraph element.
"""
from markdown.parser.base import BlockElementParser
from markdown.parser.util import ParseUtil
from markdown.parser.leaves.paragraph_element import ParagraphElement


class ParagraphParser(BlockElementParser):

    def __init__(self, config):
        super(ParagraphParser, self).__init__(config)

    def parse(self, code, index, auxiliary=None):
        elem = self.get_unclosed(auxiliary)
        start = index
        if elem is None:
            success, index = self.check_indent(code, index)
            if not success:
                return None, start
        while index < len(code) and code[index] != '\n':
            index += 1
        last = code[start:index]
        line = last.lstrip()
        index += 1
        if line == '':
            if elem is None:
                # Consumes the empty line.
                return None, index
            else:
                # The paragraph is closed by an empty line.
                elem.close()
                return elem, index
        if elem is None:
            elem = ParagraphElement()
        elem.append(line)
        if len(elem.get_lines()) >= 2:
            if ParseUtil.get_heading_space_num(last) < 4:
                line = line.rstrip()
                # Empty lines could not exist in paragraph.
                if line[0] in ['=', '-'] and all(c == line[0] for c in line):
                    elem.close()
                    if line[0] == '=':
                        elem.set_level(1)
                    else:
                        elem.set_level(1)
                    elem.del_last_line()
        return elem, index
