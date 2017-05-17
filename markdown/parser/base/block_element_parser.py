#!/usr/bin/env python
from markdown.parser.base.element_parser import ElementParser
from markdown.parser.util.parse_util import ParseUtil


class BlockElementParser(ElementParser):
    """
    The abstract block element parser.
    """

    AUX_UNCLOSED = 'unclosed'    # The last unclosed element.
    AUX_INTERRUPT = 'interrupt'  # Whether it is interrupting a paragraph.

    def __init__(self, config):
        super(BlockElementParser, self).__init__(config)

    @staticmethod
    def check_indent(code, index):
        """
        Check whether the number of heading spaces is less than 4.

        Args:
            code: An UTF-8 string.
            index: The start index (inclusive) of the current parsing.

        Returns:
            A tuple (success, index) indicating:
                success: true is the parsing succeed.
                index: the end index (exclusive) of the parsing.
        """
        space_num = ParseUtil.get_heading_space_num(code, index)
        if space_num >= 4:
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
