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

    def set_bullet(self):
        self._is_bullet = True

    def set_ordered(self):
        self._is_bullet = False

    def is_bullet(self):
        return self._is_bullet

    def is_ordered(self):
        return not self._is_bullet

    def set_start_number(self, start):
        self._start = start

    def start_number(self):
        return self._start
