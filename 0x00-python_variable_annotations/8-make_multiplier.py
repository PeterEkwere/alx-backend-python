#!/usr/bin/env python3
"""
    THis module contains the basics of type annotations
    Author: Peter Ekwere
"""
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ this function takes a float multiplier as an argument and returns another function. 

    Args:
        multiplier (float): this is a float

    Returns:
        Callable[[float], float]: _description_
    """
    def multipy_multiplyer(x: float) -> float:
        """ This function returns multiplier
        """
        return x * multiplier
    return multipy_multiplyer