#!/usr/bin/env python
"""
The paragraph element.
"""
from markdown.parser.util import BlockElement
from markdown.parser.util import ParseUtil


class Paragraph(BlockElement):

    def __init__(self, config):
        super(Paragraph, self).__init__(config)
        self._lines = []     # The lines of the paragraph.
        self._tight = False  # Whether the paragraph is tight in a list item.
        self._level = 0      # 0 if it is not a setext heading, otherwise it could be 1 or 2.

    def parse(self, code, index, auxiliary=None):
        if self._closed:
            return False, index
        start = index
        if len(self._lines) == 0:
            success, index = self.check_indent(code, index)
            if not success:
                return False, start
        while index < len(code) and code[index] != '\n':
            index += 1
        last = code[start:index]
        line = last.lstrip()
        index += 1
        if line == '':
            if len(self._lines) == 0:
                # Consumes the empty line.
                return False, index
            else:
                # The paragraph is closed by an empty line.
                self.close()
                return True, index
        self._lines.append(line)
        if len(self._lines) >= 2:
            if ParseUtil.get_heading_space_num(last) < 4:
                line = self._lines[-1].rstrip()
                # Empty lines could not exist in paragraph.
                if line[0] in ['=', '-'] and all(c == line[0] for c in line):
                    self.close()
                    if line[0] == '=':
                        self._level = 1
                    else:
                        self._level = 2
                    del self._lines[-1]
        return True, index

    def close(self):
        """
        Check whether this is a setext heading.

        Returns:
            void
        """
        super(Paragraph, self).close()
        self._lines[-1] = self._lines[-1].rstrip()

    def get_inlines(self):
        return ['\n'.join(self._lines)]

    def set_tight(self, tight):
        self._tight = tight

    def is_tight(self):
        return self._tight

    def is_setext(self):
        return self._level != 0

    def get_level(self):
        return self._level
