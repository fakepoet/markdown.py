#!/usr/bin/env python
"""
The ordered list element.
"""
from .list import List


class OrderedList(List):

    def __init__(self, config):
        super(OrderedList, self).__init__(config)

    def parse(self, code, index, auxiliary=None):
        pass
