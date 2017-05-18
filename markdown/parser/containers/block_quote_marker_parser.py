#!/usr/bin/env python
from markdown.parser.util import ParseUtil
from markdown.parser.base import ContainerElementParser
from markdown.parser.containers.block_quote_element import BlockQuoteElement


class BlockQuoteMarkerParser(ContainerElementParser):
    """
    The block quote marker parser.

    A block quote marker consists of 0-3 spaces of initial indent,
    plus (a) the character > together with a following space,
    or (b) a single character > not followed by a space.
    """

    def __init__(self, config):
        super(BlockQuoteMarkerParser, self).__init__(config)

    def parse(self, code, index, auxiliary=None):
        start = index
        # 0~3 spaces
        align = self.get_align()
        success, index = self.check_indent(code, index, align)
        if not success:
            return None, start
        if index >= len(code) or code[index] != '>':
            return None, start
        index += 1
        if index < len(code) and \
                ParseUtil.is_unicode_white_space(code[index]):
            index += 1
        return BlockQuoteElement(), index
