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
        self._paragraph_parser = ParagraphParser(config)
        self._interrupt_parsers = [
            ThematicBreakParser(config),
            # AtxHeadingParser(config),
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
            ThematicBreakParser(config),
            # AtxHeadingParser(config),
            self._paragraph_parser,
        ]

    def parse(self, code, index, auxiliary=None):
        index = 0
        while index < len(code):
            # Continuation
            if len(self._blocks) > 0 and not self._blocks[-1].is_closed():
                if isinstance(self._blocks[-1], ParagraphElement):
                    has_interrupted = False
                    for interrupt_parser in self._interrupt_parsers:
                        success, index = interrupt_parser.parse(code, index, {
                            self.AUX_INTERRUPT: True
                        })
                        if success:
                            has_interrupted = True
                            self._blocks[-1].close()
                            self._blocks.append(interrupt_parser)
                            break
                    if not has_interrupted:
                        success, index = self._paragraph_parser.parse(code, index, {
                            BlockElementParser.AUX_UNCLOSED: self._blocks[-1]
                        })
                        if not self._blocks[-1].is_closed():
                            continue
            # Try container parsers
            # Try block parsers
            for block_parser in self._block_parsers:
                elem, index = block_parser.parse(code, index)
                if elem is not None:
                    self._blocks.append(elem)
                    break
        if len(self._blocks) > 0:
            self._blocks[-1].close()

    def get_blocks(self):
        return self._blocks
