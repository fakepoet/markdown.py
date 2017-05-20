#!/usr/bin/env python
# coding=utf-8

import operator
from markdown.parser.inline_elements import SoftLineBreakElement


class CommonHTMLPrinter(object):

    def __init__(self):
        pass

    def to_html(self, blocks):
        html = u''
        for block in blocks:
            name = block.__class__.__name__
            if name == 'TextElement':
                html += self.print_text_element(block)
            elif name == 'SoftLineBreakElement':
                html += '\n'
            elif name == 'ParagraphElement':
                html += self.print_paragraph_element(block)
            elif name == 'AtxHeadingElement':
                html += self.print_atx_heading_element(block)
            elif name == 'SetextHeadingElement':
                html += self.print_setext_heading_element(block)
            elif name == 'ThematicBreakElement':
                html += self.print_thematic_break_element()
        return html

    def print_text_element(self, text):
        return text.subs[0]

    def print_paragraph_element(self, paragraph):
        elem = SoftLineBreakElement()
        subs = [[sub, elem] for sub in paragraph.subs]
        text = self.to_html(reduce(operator.add, subs)[:-1])
        if paragraph.tight:
            return text + '\n'
        return '<p>' + text + '</p>\n'

    def print_atx_heading_element(self, atx_heading):
        level = atx_heading.level
        return '<h' + str(level) + '>' + \
               self.to_html(atx_heading.subs) + \
               '</h' + str(level) + '>\n'

    def print_setext_heading_element(self, setext_heading):
        level = setext_heading.level
        return '<h' + str(level) + '>' + \
               self.to_html(setext_heading.subs) + \
               '</h' + str(level) + '>\n'

    def print_thematic_break_element(self):
        return '<hr />\n'
