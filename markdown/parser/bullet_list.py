#!/usr/bin/env python
"""
The bullet list element.
"""
from .element import BlockElement


class BulletList(BlockElement):

    def __init__(self):
        super(BulletList, self).__init__()

    def parse(self, code, index, auxiliary=None):
        pass
