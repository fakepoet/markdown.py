#!/usr/bin/env python
"""
The list elements.
"""
from markdown.parser.containers.container import Container


class List(Container):

    def __init__(self, config):
        super(List, self).__init__(config)

    def parse(self, code, index, auxiliary=None):
        pass
