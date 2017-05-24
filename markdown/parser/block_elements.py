#!/usr/bin/env python
# coding=utf-8

from .parse_util import ParseUtil


class BlockElement(object):
    """The abstract block element."""

    def __init__(self):
        self.line_num = 0    # The first number of line in source code.
        self.subs = []       # The sub elements.
        self.closed = False  # Whether the continuation is done.

    def close(self):
        """Some post actions when stop the continuation."""
        self.closed = True


class ParagraphElement(BlockElement):
    """The paragraph element."""

    def __init__(self):
        super(ParagraphElement, self).__init__()
        self.tight = False  # Whether the paragraph is tight in a list item.

    def close(self):
        super(ParagraphElement, self).close()
        if len(self.subs) > 0:
            self.subs[-1] = self.subs[-1].rstrip()
        self.subs = [ParagraphElement.strip_line(line) for line in self.subs]

    @staticmethod
    def strip_line(line):
        num = ParseUtil.get_heading_space_num(line[::-1])
        line = line.rstrip()
        if num >= 2:
            line += '<br />'
        return line


class BlankLineElement(BlockElement):
    """A virtual element used to skip empty lines."""

    def __init__(self):
        super(BlankLineElement, self).__init__()
        self.close()


class AtxHeadingElement(BlockElement):
    """The ATX heading element."""

    def __init__(self):
        super(AtxHeadingElement, self).__init__()
        self.close()
        self.level = 0


class SetextHeadingElement(BlockElement):
    """The setext heading element."""

    def __init__(self):
        super(SetextHeadingElement, self).__init__()
        self.close()
        self.level = 0


class ThematicBreakElement(BlockElement):
    """The thematic break element."""

    def __init__(self):
        super(ThematicBreakElement, self).__init__()
        self.close()


class LinkReferenceDefinitions(BlockElement):
    """The link reference difinitions."""

    def __init__(self):
        super(LinkReferenceDefinitions, self).__init__()
        self.arg_name = None
        self.title = None
        self.href = None
        self.display = ''
