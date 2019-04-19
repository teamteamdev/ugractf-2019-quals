#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import string

PLAINTEXT = 'data/plain.txt'
TEMPLATE = 'data/template.html'
RESULT = 'static/book.html'

def generate_slug():
    return ''.join([random.choice(string.hexdigits) for _ in range(32)])


def wrap(c):
    if c in (string.ascii_letters + string.digits):
        return '''<a href="/{slug}">{c}</a>'''.format(slug=generate_slug(), c=c)
    else:
        return c


def generate_page():
    with open(PLAINTEXT, "r") as f:
        text = f.read()

    text = ''.join(map(wrap, text))

    text = "<p>" + text.replace("\n\n", "</p><p>") + "</p>"

    with open(TEMPLATE, "r") as f:
        template = f.read()

    template = template.replace("<data/>", text)

    with open(RESULT, "w") as f:
        f.write(template)


if __name__ == "__main__":
    generate_page()
