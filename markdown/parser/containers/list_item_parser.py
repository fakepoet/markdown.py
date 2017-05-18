#!/usr/bin/env python
from markdown.parser.util import ParseUtil
from markdown.parser.base import ContainerElementParser
from markdown.parser.containers.list_element import ListElement


class ListItemParser(ContainerElementParser):
    """
    The block quote element.
    """

    def __init__(self, config):
        super(ListItemParser, self).__init__(config)

    def parse(self, code, index, auxiliary=None):
        start = index
        # 0~3 spaces
        align = self.get_align()
        success, index = self.check_indent(code, index, align)
        if not success:
            return None, start
        if index < len(code) and code[index] in ['-', '+', '*']:
            index += 1
            if index < len(code) and \
                    ParseUtil.is_unicode_white_space(code[index]):
                elem = ListElement()
                elem.set_bullet()
                return elem, index + 1
        digit_num = 0
        while index < len(code) and ParseUtil.is_digit(code[index]):
            digit_num += 1
            index += 1
        if 1 <= digit_num <= 9:
            if index < len(code) and code[index] in ['.', ')']:
                index += 1
                if index < len(code) and \
                        ParseUtil.is_unicode_white_space(code[index]):
                    elem = ListElement()
                    elem.set_ordered()
                    return elem, index + 1
        return None, start
