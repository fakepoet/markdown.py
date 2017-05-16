#!/usr/bin/env python


class ElementParser(object):
    """
    The abstract element parser.
    """

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
            A tuple (element, index) indicating:
                element: an element if successfully parsed, otherwise None.
                index: the end index (exclusive) of the parsing.
        """
        return None, index
