#!/usr/bin/env python3
""" Editing"""
from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """Let's duck type an iterable object"""
    return [(i, len(i)) for i in lst]
