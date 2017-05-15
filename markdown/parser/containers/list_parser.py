#!/usr/bin/env python
"""
The list elements.
"""
from markdown.parser.containers.container_parser import ContainerParser


class ListParser(ContainerParser):

    def __init__(self, config):
        super(ListParser, self).__init__(config)

    def parse(self, code, index, auxiliary=None):
        pass
