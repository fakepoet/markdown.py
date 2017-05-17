#!/usr/bin/env python
from markdown.parser.base.block_element import BlockElement


class ContainerElement(BlockElement):
    """
    The abstract container element.
    """

    def __init__(self):
        super(ContainerElement, self).__init__()
        self._blocks = []

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
