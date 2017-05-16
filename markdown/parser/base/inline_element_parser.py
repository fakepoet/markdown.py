#!/usr/bin/env python
from markdown.parser.base.element_parser import ElementParser


class InlineElementParser(ElementParser):
    """
    The abstract inline element parser.
    """

    def __init__(self, config):
        super(InlineElementParser, self).__init__(config)
