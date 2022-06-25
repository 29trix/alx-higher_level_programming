#!/usr/bin/python3

import sys


def safe_function(a, *args):
    try:
        result = a(*args)
        return (result)
    except Exception as a:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
