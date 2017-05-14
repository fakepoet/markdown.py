#!/usr/bin/env python
"""
The abstract element.
"""
from .parse_util import ParseUtil


class Element(object):

    def __init__(self, config):
        self._config = config
        self._line_num = 0

    def parse(self, code, index, auxiliary=None):
        """
        Parse the code and store the results.
        Inherited classes should implement this method.

        Args:
            code: An UTF-8 string.
            index: The start index (inclusive) of the current parsing.
            auxiliary: A dictionary with auxiliary information.

        Returns:
            A tuple (success, index) indicating:
                success: true is the parsing succeed.
                index: the end index (exclusive) of the parsing.
        """
        pass

    def set_line_num(self, line_num):
        self._line_num = line_num

    def line_num(self):
        return self._line_num


class BlockElement(Element):

    AUX_INTERRUPT = 'interrupt'

    def __init__(self, config):
        super(BlockElement, self).__init__(config)
        self._closed = False  # Whether the element is closed.

    def close(self):
        """
        The inherited classes could override this method if some checking
        need to be made when closing.

        Returns:
            void
        """
        self._closed = True

    def is_closed(self):
        return self._closed

    def get_inlines(self):
        """
        Get the inline elements.

        Returns:
            An array.
        """
        return []

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


class InlineElement(Element):

    def __init__(self, config):
        super(InlineElement, self).__init__(config)
