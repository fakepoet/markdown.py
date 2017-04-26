#!/usr/bin/env python
"""
The abstract element.
"""


class Element(object):

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

    def __init__(self):
        super(BlockElement, self).__init__()
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


class InlineElement(Element):

    def __init__(self):
        super(InlineElement, self).__init__()
