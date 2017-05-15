#!/usr/bin/env python


class Element(object):
    """
    The abstract element.
    """

    def __init__(self):
        self._line_num = 0

    def set_line_num(self, line_num):
        """
        Set the start line of the parsed element.

        Args:
            line_num: The line number.

        Returns:
            Void.
        """
        self._line_num = line_num

    def line_num(self):
        """
        Get the start line of the parsed element.

        Returns:
            The line number.
        """
        return self._line_num

    def get_inlines(self):
        """
        Get the inline elements.

        Returns:
            An array.
        """
        return []
