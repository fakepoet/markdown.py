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
        text = '\n'.join(paragraph.subs)
        if paragraph.tight:
            return text + '\n'
        return '<p>' + text + '</p>\n'

    @staticmethod
    def print_thematic_break_element(_):
        return '<hr />\n'

    @staticmethod
    def print_atx_heading_element(atx_heading):
        level = atx_heading.level
        text = atx_heading.subs[0]
        return '<h' + str(level) + '>' + text + '</h' + str(level) + '>\n'

    @staticmethod
    def print_setext_heading_element(setext_heading):
        level = setext_heading.level
        text = setext_heading.subs[0]
        return '<h' + str(level) + '>' + text + '</h' + str(level) + '>\n'
