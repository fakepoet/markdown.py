#!/usr/bin/env python
# coding=utf-8
from .printer import Printer


class CommonHTMLPrinter(Printer):

    def __init__(self, blocks):
        super(CommonHTMLPrinter, self).__init__(blocks)

    def __str__(self):
        html = u''
        for block in self._blocks:
            name = 'print_' + block.__class__.__name__.lower()
            html += getattr(CommonHTMLPrinter, name)(block)
        return html

    @staticmethod
    def print_paragraph(paragraph):
        text = paragraph.get_inlines()[0]
        if paragraph.is_setext():
            if paragraph.get_level() == 1:
                return '<h1>' + text + '</h1>\n'
            return '<h2>' + text + '</h2>\n'
        if paragraph.is_tight():
            return text + '\n'
        return '<p>' + text + '</p>\n'
