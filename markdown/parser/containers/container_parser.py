#!/usr/bin/env python
from markdown.parser.block_parsers import \
    BlockElementParser, \
    ParagraphParser, \
    AtxHeadingParser, \
    ThematicBreakParser
from markdown.parser.block_elements import \
    ParagraphElement, \
    BlankLineElement


class ContainerParser(object):

    def __init__(self, config):
        self._blocks = []  # The parsed block elements.

        self._paragraph_parser = ParagraphParser(config)
        # self._block_quote_marker_parser = BlockQuoteMarkerParser(config)
        # self._list_marker_parser = ListMarkerParser(config)
        self._interrupt_parsers = []
        self._container_parsers = []
        self._block_parsers = []
        self.init_parsers(config)

        self._layers = []
        self._line_num = 0

    def init_parsers(self, config):
        thematic_break_parser = ThematicBreakParser(config)
        atx_heading_parser = AtxHeadingParser(config)
        self._interrupt_parsers = [
            thematic_break_parser,
            atx_heading_parser,
            # FencedCodeBlockParser(config),
            # HtmlBlockParser(config)  # Type 1-6,
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

    def get_blocks(self):
        return self._blocks

    def parse(self, code):
        lines = code.split('\n')
        for line_num, line in enumerate(lines):
            self._line_num = line_num + 1
            print self._line_num, self._blocks
            index = self.parse_container_markers(line)
            if not self.parse_continuation(line, index):
                self.parse_blocks(line, index)
        if len(self._blocks) > 0:
            self._blocks[-1].close()

    def parse_container_markers(self, line):
        """
        index = 0
        layer_index = 0
        while False:
            elem, index = self._block_quote_marker_parser.parse(line, index)
            if not elem:
                offset = 0
                if layer_index < len(self._layers) and \
                        isinstance(self._layers[layer_index], BlockQuoteElement):
                    offset = self._layers[layer_index].offset()
                elem, index = self._list_marker_parser.parse(line, index, {
                    ContainerElementParser.AUX_ALIGN: offset
                })
                if not elem:
                    break
        return index
        """
        return 0

    def parse_continuation(self, line, index):
        if len(self._blocks) > 0 and not self._blocks[-1].closed:
            if isinstance(self._blocks[-1], ParagraphElement):
                has_interrupted = False
                for interrupt_parser in self._interrupt_parsers:
                    elem = interrupt_parser.parse(line, index, {
                        BlockElementParser.AUX_INTERRUPT: True
                    })
                    if elem is not None:
                        has_interrupted = True
                        self._blocks[-1].close()
                        elem.line_num = self._line_num
                        self._blocks.append(elem)
                        break
                if not has_interrupted:
                    self._blocks[-1] = self._paragraph_parser.parse(line, index, {
                        BlockElementParser.AUX_UNCLOSED: self._blocks[-1]
                    })
            return True
        return False

    def parse_blocks(self, line, index):
        for block_parser in self._block_parsers:
            elem = block_parser.parse(line, index)
            if elem is not None:
                if isinstance(elem, BlankLineElement):
                    break
                elem.line_num = self._line_num
                self._blocks.append(elem)
                break
