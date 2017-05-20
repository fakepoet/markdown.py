#!/usr/bin/env python
# coding=utf-8

from .block_elements import BlockElement


class ContainerElement(BlockElement):
    """The abstract container element."""

    def __init__(self):
        super(ContainerElement, self).__init__()
        self.offset = 0


class BlockQuoteElement(ContainerElement):
    """
    The block quote element.
    """

    def __init__(self):
        super(BlockQuoteElement, self).__init__()


class ListElement(ContainerElement):
    """
    The list element.
    """

    def __init__(self):
        super(ListElement, self).__init__()
        self.ordered = False  # Whether the list is an ordered list.
        self.marker = ''      # The bullet marker if the list is unordered.
        self.start = 1        # The start number if the list is ordered.
