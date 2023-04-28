#!/usr/bin/env python3
""" Duck typing - first element of a sequence """
from typing import Sequence, Any


def safe_first_element(lst: Sequence[Any]):
    """ the correct duck-typed annotations """
    if lst:
        return lst[0]
    else:
        return None
