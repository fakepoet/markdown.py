"""
The markdown parser.
"""


class Parser(object):

    def __init__(self):
        self.reset()

    def reset(self):
        """Reset config and members."""
        self._config = {
            'gfm': False    # Enable GitHub Flavored Markdown
        }
        self._linkRefs = []  # Links
        self._linkDefs = {}  # Link reference definitions
        self._blocks = []

    def config(self, key, value):
        """Update parsing configuration.
        Returns a bool value indicates the existance of the key.
        """
        if key in self._config:
            self._config[key] = value
            return True
        return False

    def parse(self, code):
        """Parse the given code string.
        Argument:
        code -- an UTF-8 encoded string.
        """
        pass
