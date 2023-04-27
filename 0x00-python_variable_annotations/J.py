#!/usr/bin/env python3
""" Multiplexer """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Returns the product"""
    def mult_multiplier(num: float) -> float:
        """ Multiply """
        return num * multiplier
    return mult_multiplier
