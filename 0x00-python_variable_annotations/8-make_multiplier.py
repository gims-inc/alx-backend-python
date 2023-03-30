#!/usr/bin/env python3
"""functions"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    function make_multiplier that takes a float multiplier
    as argument and returns a function that multiplies a float
    by multiplier
    """
    def mult(multiplier: float) -> float:
        """
        function that multiplies a float by multiplier

        multiplier : callable
        return multiplier ** 2
        """
        return (multiplier * multiplier)
    return mult
