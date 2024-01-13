#!/usr/bin/env python3
"""
    This module contains basic annotation practices
    Author: Peter Ekwere
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ ...

    Args:
        k (str): this is a string variable
        v (Union[int, float]): this variable can be integer or float

    Returns:
        Tuple[str, float]: this tuple contains a string and a float
    """
    return (k, v ** 2)