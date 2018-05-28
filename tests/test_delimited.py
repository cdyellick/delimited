# -*- coding: utf-8 -*-
# Copyright (C) 2018, Chris Yellick
# Licensed under 2 clause BSD license; provided "as is" and without any
# express or implied warranties. See LICENSE for full agreement

import string

from hypothesis import given
from hypothesis.strategies import composite, lists, text

import cy.delimited as dlmtd


@composite
def delimited_str_printable(draw):
    """Generates a delimited string from the printable characters set
    and returns it in a dictionary with the delimiter.

      * The printable character set is defined by string.printable
      * The delimiter can be any single printable character
      * The encoded items will be at least one character long and can
        include any printable characters except the delimiter or
        leading or trailing whitespace
      * Each delimited string will have at least one item
      * The delimiter is surrounded by one space on either side

    """
    delimiter = draw(text(alphabet=string.printable, min_size=1, max_size=1))
    items = draw(lists(
        text(alphabet=string.printable, min_size=1).filter(
            lambda x: (delimiter not in x) and (x.strip() == x)),
        min_size=1))
    return {'delimiter': delimiter, 'string': f' {delimiter} '.join(items)}


@dlmtd.delimiter_magic
def echo(s):
    """Returns the results of delimiter_magic"""
    return s


@given(delimited_str_printable())
def test_delimiter_magic(dlmtd_str):
    """The results of delimiter_magic for any proper delimited string
    should be the delimited string."""
    assert(echo(dlmtd_str['string'], delimiter=dlmtd_str['delimiter']) == dlmtd_str['string'])
