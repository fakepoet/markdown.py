#!/usr/bin/env python
# coding=utf-8
from .printer import Printer


class CommonHTMLPrinter(Printer):

    def __init__(self, blocks):
        super(CommonHTMLPrinter, self).__init__(blocks)

    def __str__(self):
        html = u''
        maps = {}
        for block in self._blocks:
            name = block.__class__.__name__
            if name not in maps:
                def mapping(ch):
                    if 'A' <= ch <= 'Z':
                        return '_' + chr(ord(ch) - ord('A') + ord('a'))
                    return ch
                maps[name] = ''.join(map(mapping, name))[1:]
            name = 'print_' + maps[name]
            html += getattr(CommonHTMLPrinter, name)(block)
        return html

    @staticmethod
    def print_paragraph_element(paragraph):
        text = paragraph.get_inlines()[0]
        if paragraph.is_setext():
            if paragraph.get_level() == 1:
                return '<h1>' + text + '</h1>\n'
            return '<h2>' + text + '</h2>\n'
        if paragraph.is_tight():
            return text + '\n'
        return '<p>' + text + '</p>\n'

    @staticmethod
    def print_thematic_break_element(_):
        return '<hr />\n'

    @staticmethod
    def print_atx_heading_element(atx_heading):
        level = atx_heading.get_level()
        text = atx_heading.get_inlines()[0]
        return '<h' + str(level) + '>' + text + '</h' + str(level) + '>\n'
