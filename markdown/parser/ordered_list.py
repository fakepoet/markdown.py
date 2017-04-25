#!/usr/bin/env python
"""
The ordered list element.
"""
from .element import BlockElement


class OrderedList(BlockElement):

    def __init__(self):
        super(OrderedList, self).__init__()

    def parse(self, code, index, auxiliary=None):
        pass
