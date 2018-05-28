# -*- coding: utf-8 -*-
# Copyright (C) 2018, Chris Yellick
# Licensed under 2 clause BSD license; provided "as is" and without any
# express or implied warranties. See LICENSE for full agreement


def delimiter_magic(func):
    """Decorator that allows functions operating on lists to operate
    on delimited strings.

    Splits a delimited string to a list before calling the decorated
    functions and then converts the result back to a delimited string
    before returning.

    Parameters
    ----------
    s : string
        Delimited string that is converted to a list and passed as the
        first argument to the decorated function
    delimiter : string
        Delimiter to split string on (default is '|')
    strip : Boolean
        If true, whitespace surrounding delimiters is removed; returned
        string will have one space on either side of the delimiter
        (Default is None, which causes the function to guess whether to
        use stripping)

    Returns
    -------
    string
        Delimited string created from the list returned by the
        decorated function

    """
    def _wrapper(s, *args, delimiter='|', strip=None, **kwargs):
        # If delimiter is None, bypass delimitation steps and call func
        # directly, allows decorated functions to be used with lists
        if delimiter is None:
            return func(s, *args, **kwargs)
        else:
            # Split string to list
            s = s.split(delimiter)

            # Strip leading and trailing whitespace
            if strip is not False:
                s_stripped = [x.strip() for x in s]
                # If strip is None guess if it should be used
                if strip is None:
                    if s == s_stripped:
                        strip = False
                    else:
                        strip = True
                        s = s_stripped
                else:
                    s = s_stripped
                del s_stripped

            # call func
            result = func(s, *args, **kwargs)

            # convert back to delimited form, with spaces if removed
            if strip:
                result = f' {delimiter} '.join(result)
            else:
                result = delimiter.join(result)
            return result

    return _wrapper
