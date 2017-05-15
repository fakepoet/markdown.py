#!/usr/bin/env python
"""
Container (block quotes and lists) parser.
"""
from markdown.parser.leaves import AtxHeadingParser
from markdown.parser.leaves import ParagraphParser
from markdown.parser.leaves import ThematicBreakParser
from markdown.parser.base import BlockElementParser


class ContainerParser(BlockElementParser):

    def __init__(self, config):
        super(ContainerParser, self).__init__(config)
        self._blocks = []  # The parsed block elements.
        self._interrupt_parsers = [
            ThematicBreakParser,
            AtxHeadingParser,
            # FencedCodeBlockParser,
            # HtmlBlockParser  # Type 1-6,
            # ListParser       # Not empty,
        ]
        self._container_parsers = [
            # BlockQuoteParser,
            # BulletListParser,
            # OrderedListParser,
        ]
        self._block_parsers = [
            ThematicBreakParser,
            AtxHeadingParser,
            ParagraphParser,
        ]

    def parse(self, code, index, auxiliary=None):
        index = 0
        while index < len(code):
            # Continuation
            if len(self._blocks) > 0 and not self._blocks[-1].is_closed():
                if isinstance(self._blocks[-1], ParagraphParser):
                    has_interrupted = False
                    for interrupt_parser_class in self._interrupt_parsers:
                        interrupt_parser = interrupt_parser_class(self._config)
                        success, index = interrupt_parser.parse(code, index, {
                            self.AUX_INTERRUPT: True
                        })
                        if success:
                            has_interrupted = True
                            self._blocks[-1].close()
                            self._blocks.append(interrupt_parser)
                            break
                    if not has_interrupted:
                        success, index = self._blocks[-1].parse(code, index)
                        if not self._blocks[-1].is_closed():
                            continue
            # Try container parsers
            # Try block parsers
            for block_parser_class in self._block_parsers:
                block_parser = block_parser_class(self._config)
                success, index = block_parser.parse(code, index)
                if success:
                    self._blocks.append(block_parser)
                    break
        if len(self._blocks) > 0:
            self._blocks[-1].close()

    def get_blocks(self):
        return self._blocks
