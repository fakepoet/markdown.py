#!/usr/bin/env python
from markdown.parser.base.element import Element


class BlockElement(Element):
    """
    The abstract block element.
    """

    def __init__(self):
        super(BlockElement, self).__init__()
        self._closed = False

    def is_closed(self):
        return self._closed

    def close(self):
        self._closed = True
