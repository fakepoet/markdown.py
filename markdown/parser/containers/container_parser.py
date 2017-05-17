#!/usr/bin/env python
"""
Container (block quotes and lists) parser.
"""
from markdown.parser.base import BlockElementParser
from markdown.parser.leaves import AtxHeadingParser
from markdown.parser.leaves import ParagraphElement
from markdown.parser.leaves import ParagraphParser
from markdown.parser.leaves import ThematicBreakParser


class ContainerParser(BlockElementParser):

    def __init__(self, config):
        super(ContainerParser, self).__init__(config)
        self._blocks = []  # The parsed block elements.

        thematic_break_parser = ThematicBreakParser(config)
        atx_heading_parser = AtxHeadingParser(config)
        self._paragraph_parser = ParagraphParser(config)
        self._interrupt_parsers = [
            thematic_break_parser,
            atx_heading_parser,
            # FencedCodeBlockParser(config),
            # HtmlBlockParser(config)  # Type 1-6,
            # ListParser(config)       # Not empty,
        ]
        self._container_parsers = [
            # BlockQuoteParser(config),
            # BulletListParser(config),
            # OrderedListParser(config),
        ]
        self._block_parsers = [
            thematic_break_parser,
            atx_heading_parser,
            self._paragraph_parser,
        ]

    def parse(self, code, index, auxiliary=None):
        lines = code.split('\n')
        for line_num, line in enumerate(lines):
            # Try container parsers
            index = 0
            # Continuation
            if len(self._blocks) > 0 and not self._blocks[-1].is_closed():
                if isinstance(self._blocks[-1], ParagraphElement):
                    has_interrupted = False
                    for interrupt_parser in self._interrupt_parsers:
                        elem, index = interrupt_parser.parse(line, index, {
                            self.AUX_INTERRUPT: True
                        })
                        if elem is not None:
                            has_interrupted = True
                            self._blocks[-1].close()
                            elem.set_line_num(line_num)
                            self._blocks.append(elem)
                            break
                    if not has_interrupted:
                        elem, index = self._paragraph_parser.parse(line, index, {
                            BlockElementParser.AUX_UNCLOSED: self._blocks[-1]
                        })
                        if not self._blocks[-1].is_closed():
                            continue
            # Try block parsers
            for block_parser in self._block_parsers:
                elem, index = block_parser.parse(line, index)
                if elem is not None:
                    elem.set_line_num(line_num)
                    self._blocks.append(elem)
                    break
        if len(self._blocks) > 0:
            self._blocks[-1].close()

    def get_blocks(self):
        return self._blocks
