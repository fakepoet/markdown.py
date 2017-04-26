#!/usr/bin/env python
"""
The bullet list element.
"""
from .list import List


class BulletList(List):

    def __init__(self, config):
        super(BulletList, self).__init__(config)

    def parse(self, code, index, auxiliary=None):
        pass
