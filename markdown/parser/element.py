#!/usr/bin/env python
"""
The abstract element.
"""


class Element(object):

    def __init__(self, config):
        self._config = config

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

    @staticmethod
    def get_heading_space_num(line, index=0):
        num = 0
        for c in line[index:]:
            if c == ' ':
                num += 1
            elif c == '\t':
                num += 4
            else:
                break
        return num


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
        space_num = Element.get_heading_space_num(code, index)
        if space_num >= 4:
            return False, index
        return True, index + space_num


class InlineElement(Element):

    def __init__(self, config):
        super(InlineElement, self).__init__(config)
