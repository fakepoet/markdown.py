#!/usr/bin/env python
from markdown.parser.base import BlockElement


class ThematicBreakElement(BlockElement):
    """
    The thematic break element.
    """

    def __init__(self):
        super(ThematicBreakElement, self).__init__()
        self.close()
