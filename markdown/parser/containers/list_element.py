#!/usr/bin/env python
from markdown.parser.base import ContainerElement


class ListElement(ContainerElement):
    """
    The list element.
    """

    def __init__(self):
        super(ListElement, self).__init__()
        self._is_bullet = True
        self._start = 1

    def is_bullet(self):
        return self._is_bullet

    def is_ordered(self):
        return not self._is_bullet

    def start_number(self):
        return self._start
