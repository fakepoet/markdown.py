#!/usr/bin/env python
# coding=utf-8
from markdown.parser.parse_util import ParseUtil
from .block_elements import ParagraphElement, \
    BlankLineElement, \
    AtxHeadingElement, \
    SetextHeadingElement, \
    ThematicBreakElement


class BlockElementParser(object):
    """The abstract block element parser."""

    AUX_UNCLOSED = 'unclosed'    # The last unclosed element.
    AUX_INTERRUPT = 'interrupt'  # Whether it is interrupting a paragraph.

    def __init__(self, config):
        self._config = config

    @staticmethod
    def check_indent(code, index, align=0):
        """
        Check whether the number of heading spaces is less than 4.

        Args:
            code: An UTF-8 string.
            index: The start index (inclusive) of the current parsing.
            align: The align index.

        Returns:
            A tuple (success, index) indicating:
                success: true is the parsing succeed.
                index: the end index (exclusive) of the parsing.
        """
        space_num = ParseUtil.get_heading_space_num(code, index)
        if space_num >= align + 4:
            return False, index
        return True, index + space_num

    def get_unclosed(self, auxiliary):
        """
        Get last unclosed element.

        Args:
            auxiliary: A dict.

        Returns:
            Returns None if it is not existed.
        """
        if auxiliary is None:
            return None
        if self.AUX_UNCLOSED not in auxiliary:
            return None
        return auxiliary[self.AUX_UNCLOSED]

    def is_interrupting(self, auxiliary):
        """
        Whether it is interrupting a paragraph.

        Args:
            auxiliary: A dict.

        Returns:
            Boolean.
        """
        if auxiliary is None:
            return False
        if self.AUX_INTERRUPT not in auxiliary:
            return False
        return auxiliary[self.AUX_INTERRUPT]


class ParagraphParser(BlockElementParser):
    """
    The paragraph parser.

    A sequence of non-blank lines that cannot be interpreted as other
    kinds of blocks forms a paragraph. The contents of the paragraph are
    the result of parsing the paragraph’s raw content as inlines. The
    paragraph’s raw content is formed by concatenating the lines and
    removing initial and final whitespace.
    """

    def __init__(self, config):
        super(ParagraphParser, self).__init__(config)

    def parse(self, code, index, auxiliary=None):
        elem = self.get_unclosed(auxiliary)
        start = index
        if elem is None:
            success, index = self.check_indent(code, index)
            if not success:
                return None
        while index < len(code) and code[index] != '\n':
            index += 1
        last = code[start:index]
        line = last.lstrip()
        index += 1
        if line == '':
            if elem is None:
                # Consumes the blank line.
                return BlankLineElement()
            else:
                # The paragraph is closed by an empty line.
                elem.close()
                return elem
        if elem is None:
            elem = ParagraphElement()
        elem.subs.append(line)
        print elem.subs
        if len(elem.subs) >= 2:
            if ParseUtil.get_heading_space_num(last) < 4:
                line = line.rstrip()
                # Empty lines could not exist in paragraph.
                if line[0] in ['=', '-'] and all(c == line[0] for c in line):
                    del elem.subs[-1]
                    elem.close()
                    heading_elem = SetextHeadingElement()
                    heading_elem.subs = elem.subs
                    if line[0] == '=':
                        heading_elem.level = 1
                    else:
                        heading_elem.level = 2
                    return heading_elem
        return elem


class AtxHeadingParser(BlockElementParser):
    """
    The ATX heading parser.

    An ATX heading consists of a string of characters, parsed as inline
    content, between an opening sequence of 1–6 unescaped # characters
    and an optional closing sequence of any number of unescaped #
    characters. The opening sequence of # characters must be followed
    by a space or by the end of line. The optional closing sequence
    of #s must be preceded by a space and may be followed by spaces
    only. The opening # character may be indented 0-3 spaces. The raw
    contents of the heading are stripped of leading and trailing spaces
    before being parsed as inline content. The heading level is equal
    to the number of # characters in the opening sequence.
    """

    def __init__(self, config):
        super(AtxHeadingParser, self).__init__(config)

    def parse(self, code, index, _=None):
        # 0~3 spaces
        success, index = self.check_indent(code, index)
        if not success:
            return None
        # 1~6 `#`s
        if index >= len(code) or code[index] != '#':
            return None
        level = 0
        while index < len(code) and code[index] == '#':
            index += 1
            level += 1
        if level > 6:
            return None
        # May be empty
        if index == len(code):
            elem = AtxHeadingElement()
            elem.subs = ['']
            elem.level = level
            return elem
        # One space is required
        if code[index] != ' ':
            return None
        # The title body
        start = index
        while index < len(code) and code[index] != '\n':
            index += 1
        title = code[start:index].rstrip()
        # Remove arbitrary number of tailing `#`s
        for i in range(len(title) - 1, -1, -1):
            if title[i] == ' ':
                title = title[:i]
                break
            elif title[i] != '#':
                break
        title = title.strip()
        elem = AtxHeadingElement()
        elem.subs = [title]
        elem.level = level
        return elem


class ThematicBreakParser(BlockElementParser):
    """
    The thematic break parser.

    A line consisting of 0-3 spaces of indentation, followed by a
    sequence of three or more matching -, _, or * characters, each
    followed optionally by any number of spaces, forms a thematic break.
    """

    def __init__(self, config):
        super(ThematicBreakParser, self).__init__(config)

    def parse(self, code, index, auxiliary=None):
        success, index = self.check_indent(code, index)
        if not success:
            return None
        if index >= len(code):
            return None
        first = code[index]
        if first not in ['*', '-', '_']:
            return None
        count = 0
        has_space = False
        has_inner_space = False
        while index < len(code) and code[index] != '\n':
            if code[index] == first:
                count += 1
                if has_space:
                    has_inner_space = True
            elif code[index] in [' ', '\t']:
                has_space = True
            else:
                return None
            index += 1
        if count < 3:
            return None
        if self.is_interrupting(auxiliary) and first == '-' and not has_inner_space:
            return None
        return ThematicBreakElement()
