#!/usr/bin/env python3
""" More involved type annotations """
from typing import TypeVar, Mapping

K = TypeVar('K')
V = TypeVar('V')

def safely_get_value(dct: Mapping[K, V], key: K, default: V = None) -> V:
    """ adds type annotations to the function """
    if key in dct:
        return dct[key]
    else:
        return default
