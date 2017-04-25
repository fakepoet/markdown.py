#!/usr/bin/env python
"""
The abstract element.
"""


class Element(object):

    _line = -1    # The start line number.
    _column = -1  # The start column number.

    def __init__(self):
        pass

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


class BlockElement(Element):

    _finished = False  # Whether the element is closed.

    def __init__(self):
        super(BlockElement, self).__init__()

    def is_finished(self):
        return self._finished

    def get_inlines(self):
        """
        Get the inline elements.

        Returns:
            An array.
        """
        return []


class InlineElement(Element):

    def __init__(self):
        super(InlineElement, self).__init__()
