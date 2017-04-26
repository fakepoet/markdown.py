#!/usr/bin/env python
"""
The bullet list element.
"""
from .list import List


class BulletList(List):

    def __init__(self):
        super(BulletList, self).__init__()

    def parse(self, code, index, auxiliary=None):
        pass
