#!/usr/bin/env python
"""
The list elements.
"""
from .container import Container


class List(Container):

    def __init__(self):
        super(List, self).__init__()

    def parse(self, code, index, auxiliary=None):
        pass
