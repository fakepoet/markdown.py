#!/usr/bin/env python
from markdown.parser.base import BlockElement


class EmptyLineElement(BlockElement):
    """
    A virtual element used to skip empty lines.
    """

    def __init__(self):
        super(BlockElement, self).__init__()
