#!/usr/bin/env python
from markdown.parser.base.block_element_parser import BlockElementParser


class ContainerElementParser(BlockElementParser):
    """
    The abstract container element parser.
    """

    AUX_ALIGN = 'align'  # The align offset for lists.

    def __init__(self, config):
        super(ContainerElementParser, self).__init__(config)

    def get_align(self, auxiliary):
        """
        Get the align offset.

        Args:
            auxiliary: A dict.

        Returns:
            An integer.
        """
        if auxiliary is None:
            return 0
        if self.AUX_ALIGN not in auxiliary:
            return 0
        return int(auxiliary[self.AUX_ALIGN])
