#!/usr/bin/env/ python
# coding: utf-8

import sys

from .base.block_element_parser import BlockElementParser

if sys.version_info[0] >= 3:
    casefold = lambda x: x.casefold()
else:
    import py2casefold
    casefold  = py2casefold.casefold


class LinkReferenceDefinitionsParser(BlockElementParser):
    """link reference definitions.

    A link reference definition consists of a link label, indented up
    to three spaces, followed by a colon (:), optional whitespace
    (including up to one line ending), a link destination, optional
    whitespace (including up to one line ending), and an optional link
    title, which if it is present must be separated from the link
    destination by whitespace. No further non-whitespace characters
    may occur on the line.
    A link reference definition does not correspond to a structural
    element of a document. Instead, it defines a label which can be
    used in reference links and reference-style images elsewhere in
    the document. Link reference definitions can come either before
    or after the links that use them.
    """

    def __init__(self, config):
        super(LinkReferenceDefinitions, self).__init__(config)

    def parse(self, code, index, auxiliary=None):
