#!/usr/bin/env python


class ContainerElement(object):
    """
    The abstract container element.
    """

    def __init__(self):
        super(ContainerElement, self).__init__()
        self._blocks = []
        self._offset = 0

    def get_blocks(self):
        """
        Get the blocks elements.

        Returns:
            An array.
        """
        return self._blocks

    def add_block(self, block):
        """
        Append a block element.

        Args:
            block: a block element.

        Returns:
            None.
        """
        self._blocks.append(block)

    def set_offset(self, offset):
        self._offset = offset

    def offset(self):
        return self._offset
