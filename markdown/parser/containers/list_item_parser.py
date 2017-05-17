#!/usr/bin/env python
from markdown.parser.base import ContainerElementParser


class ListItemParser(ContainerElementParser):
    """
    The block quote element.
    """

    def __init__(self, config):
        super(ListItemParser, self).__init__(config)

    def parse(self, code, index, auxiliary=None):
        start = index
        # 0~3 spaces
        success, index = self.check_indent(code, index)
        if not success:
            return None, start
