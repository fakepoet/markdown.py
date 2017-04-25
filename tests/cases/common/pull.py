#!/usr/bin/env python
# coding=utf-8
"""
Pull test cases from common markdown specification.
"""
import re
import codecs
import requests

try:
    # Python 2
    from HTMLParser import HTMLParser
except ImportError:
    # Python 3
    from html.parser import HTMLParser

SPEC_URL = 'http://spec.commonmark.org/0.27/'
CASE_LEN = 622
FIRST_CASE = u'foo→baz→→bim'

response = requests.get(SPEC_URL)

examples = re.findall(
    r'<div class="example".*?language-markdown">(.*?)</code>.*?language-html">(.*?)</code>',
    response.text,
    re.DOTALL
)

parser = HTMLParser()
for index, example in enumerate(examples):
    example = map(lambda s: s.replace(u'→', '\t'), example)
    example = map(lambda s: s.replace('<span class="space"> </span>', ' '), example)
    example = map(lambda s: parser.unescape(s), example)
    with codecs.open(str(index + 1) + '.in', 'w', 'utf8') as writer:
        writer.write(example[0])
    with codecs.open(str(index + 1) + '.out', 'w', 'utf8') as writer:
        writer.write(example[1])
