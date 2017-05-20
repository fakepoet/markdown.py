#!/usr/bin/env python
# coding=utf-8
from markdown.parser.parse_util import ParseUtil
from markdown.parser.base import ContainerElementParser
from markdown.parser.containers.list_element import ListElement


class ListMarkerParser(ContainerElementParser):
    """
    The list marker parser.

    A list marker is a bullet list marker or an ordered list marker.

    A bullet list marker is a -, +, or * character.

    An ordered list marker is a sequence of 1–9 arabic digits (0-9),
    followed by either a . character or a ) character.
    """

    def __init__(self, config):
        super(ListMarkerParser, self).__init__(config)

    def parse(self, code, index, auxiliary=None):
        start = index
        # 0~3 spaces
        align = self.get_align(auxiliary)
        success, index = self.check_indent(code, index, align)
        if not success:
            return None, start
        if index < len(code) and code[index] in ['-', '+', '*']:
            index += 1
            if index < len(code) and \
                    ParseUtil.is_unicode_white_space(code[index]):
                index += 1
                elem = ListElement()
                elem.set_bullet()
                elem.set_offset(index)
                return elem, index
        digit_num = 0
        start_num = 0
        while index < len(code) and ParseUtil.is_digit(code[index]):
            digit_num += 1
            start_num = start_num * 10 + ord(code[index]) - ord('0')
            index += 1
        if 1 <= digit_num <= 9:
            if index < len(code) and code[index] in ['.', ')']:
                index += 1
                if index < len(code) and \
                        ParseUtil.is_unicode_white_space(code[index]):
                    index += 1
                    elem = ListElement()
                    elem.set_ordered()
                    elem.set_offset(index)
                    elem.set_start_number(start_num)
                    return elem, index
        return None, start
