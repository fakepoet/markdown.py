#!/usr/bin/env python
"""
The abstract element.
"""


class Element(object):

    line = -1
    pos = -1

    def __init__(self):
        self.line = -1
        self.pos = -1
