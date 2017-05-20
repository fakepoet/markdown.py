#!/usr/bin/env python
# coding=utf-8

import operator
from markdown.parser.block_elements import (ParagraphElement,
                                            AtxHeadingElement,
                                            SetextHeadingElement,
                                            ThematicBreakElement)
from markdown.parser.inline_elements import (TextualContentElement,
                                             SoftLineBreakElement)


class CommonHTMLPrinter(object):

    def __init__(self):
        pass

    def to_html(self, blocks):
        html = u''
        for block in blocks:
            if isinstance(block, TextualContentElement):
                html += block.subs[0]
            elif isinstance(block, SoftLineBreakElement):
                html += '\n'
            elif isinstance(block, ParagraphElement):
                elem = SoftLineBreakElement()
                subs = [[sub, elem] for sub in block.subs]
                text = self.to_html(reduce(operator.add, subs)[:-1])
                if block.tight:
                    html += text + '\n'
                else:
                    html += '<p>' + text + '</p>\n'
            elif isinstance(block, AtxHeadingElement) or \
                    isinstance(block, SetextHeadingElement):
                level = block.level
                html += '<h' + str(level) + '>' + \
                        self.to_html(block.subs) + \
                        '</h' + str(level) + '>\n'
            elif isinstance(block, ThematicBreakElement):
                html += '<hr />\n'
        return html
