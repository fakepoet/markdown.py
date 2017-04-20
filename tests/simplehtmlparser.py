

class SimpleHTMLParser(object):
    """
    A simple HTML parser for testing.

    Not suitable for harsh cases, and the time efficiency is not considered.

    Examples:
        <tag key1="val1" key2>text</tag>
        <tag />
    """

    def __init__(self):
        pass

    def parse(self, content, parent=None):
        if parent is None:
            _, children = self.parse(content, self.body)
            self.body = {
                'trunk': ('body'),
                'leaves': []
            }
            return
        if content == '':
            return None
        i = 0
        while i < len(content):
            first = i
            while i < len(content) and content[i] != '<':
                i += 1
            if first != i:
                text = content[first:i]
                parent['leaves'].append(('text', text))
            if i == len(content):
                break
            first = i
            while content[i] != '>':
                i += 1
            parts = map(lambda x: len(x) > 0, content[first + 1:i].split(' '))
            if parts[0] == '/':
                return i + 1
            attrs = {}
            for part in parts[1:]:
                if part != '/':
                    if '=' in part:
                        key, val = part.split('=')
                        attrs[key] = val
                    else:
                        attrs[part] = None
            if parts[-1] == '/':
                parent['leaves'].append(('tag', parts[0], attrs))
            else:
                leaf = {
                    'trunk': ('tag', parts[0], attrs),
                    'leaves': [],
                }
                i += self.parse(content[i + 1:], leaf)
                parent['leaves'].append(leaf)
        return len(content)
