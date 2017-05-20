#!/usr/bin/env python
# coding=utf-8

from .parse_util import ParseUtil
from .container_elements import (BlockQuoteElement,
                                 ListElement)


class ContainerElementParser(object):
    """
    The abstract container element parser.
    """

    AUX_ALIGN = 'align'  # The align offset for lists.

    def __init__(self, config):
        super(ContainerElementParser, self).__init__(config)

    def get_align(self, auxiliary):
        """
        Get the align offset.

        Args:
            auxiliary: A dict.

        Returns:
            An integer.
        """
        if auxiliary is None:
            return 0
        if self.AUX_ALIGN not in auxiliary:
            return 0
        return int(auxiliary[self.AUX_ALIGN])


class BlockQuoteMarkerParser(ContainerElementParser):
    """
    The block quote marker parser.

    A block quote marker consists of 0-3 spaces of initial indent,
    plus (a) the character > together with a following space,
    or (b) a single character > not followed by a space.
    """

    def __init__(self, config):
        super(BlockQuoteMarkerParser, self).__init__(config)

    def parse(self, code, index, _=None):
        start = index
        # 0~3 spaces
        success, index = self.check_indent(code, index)
        if not success:
            return None, start
        if index >= len(code) or code[index] != '>':
            return None, start
        index += 1
        if index < len(code) and \
                ParseUtil.is_unicode_white_space(code[index]):
            index += 1
        return BlockQuoteElement(), index


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
            marker = code[index]
            index += 1
            if index < len(code) and \
                    ParseUtil.is_unicode_white_space(code[index]):
                index += 1
                elem = ListElement()
                elem.ordered = False
                elem.marker = marker
                elem.offset = index
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
                    elem.ordered = True
                    elem.offset = index
                    elem.start = start_num
                    return elem, index
        return None, start
