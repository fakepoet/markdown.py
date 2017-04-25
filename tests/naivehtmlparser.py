#!/usr/bin/env python
class NaiveHTMLParser(object):
    """
    A naive HTML parser for testing.

    Not suitable for harsh cases, and the time efficiency is not considered.

    Examples:
        <tag key1="val1" key2>text</tag>
        <tag />
    """

    body = {}

    def __init__(self):
        pass

    def parse(self, content, parent=None):
        """
        Parse the HTML content.

        Args:
            content: The UTF-8 encoded string.
            parent: The parent HTML element.

        Returns:
            The index of parsed content.
        """
        if parent is None:
            self.body = {
                'elem': 'body',
                'children': []
            }
            self.parse(content, self.body)
            return None
        if content == '':
            return 0
        i = 0
        while i < len(content):
            first = i
            while i < len(content) and content[i] != '<':
                i += 1
            if first != i:
                text = content[first:i]
                if text.strip() != '':
                    parent['children'].append(('text', text))
            if i == len(content):
                break
            first = i
            while i < len(content) and content[i] != '>':
                i += 1
            parts = list(filter(
                lambda x: len(x) > 0,
                content[first + 1:i].replace('\n', ' ').split(' ')
            ))
            if parts[0][0] == '/':
                return i + 1
            attributes = {}
            for part in parts[1:]:
                if part != '/':
                    if '=' in part:
                        strings = part.split('=')
                        key = strings[0]
                        val = '='.join(strings[1:])
                        if len(val) >= 2 and val[0] == '"' and val[-1] == '"':
                            val = val[1:-1]
                        attributes[key] = val
                    else:
                        attributes[part] = None
            if parts[-1] == '/':
                parent['children'].append(('tag', parts[0], attributes))
            else:
                leaf = {
                    'elem': ('tag', parts[0], attributes),
                    'children': [],
                }
                i += self.parse(content[i + 1:], leaf) + 1
                parent['children'].append(leaf)
        return len(content)
