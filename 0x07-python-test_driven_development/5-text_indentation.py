#!/usr/bin/python3
"""
text indentation
"""


def text_indentation(text):
    """
    Args:
    text (str): text

    Raises:
    TypeError: text must be a string
    """
    if not isinstance(text, str) or text is None:
        raise TypeError("text must be a string")
    for c in ['.', ':', '?']:
        if c in text:
            text = text.replace(c, c+"\n\n")
    print("\n".join([x.strip() for x in text.split("\n")]), end="")
