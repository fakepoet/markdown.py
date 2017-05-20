#!/usr/bin/env python
# coding=utf-8

from .inline_elements import TextualContentElement


class InlineParser(object):

    def __init__(self):
        pass

    def parse(self, code):
        elem = TextualContentElement()
        elem.subs = [code]
        return elem
