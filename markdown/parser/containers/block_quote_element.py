#!/usr/bin/env python
from markdown.parser.base import ContainerElement


class BlockQuoteElement(ContainerElement):
    """
    The block quote element.
    """

    def __init__(self):
        super(BlockQuoteElement, self).__init__()
