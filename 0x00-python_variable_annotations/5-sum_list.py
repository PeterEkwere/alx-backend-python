#!/usr/bin/env python3
"""
    This module contains basic type annotaion practices
    Author: Peter Ekwere  
"""
from typing import List

def sum_list(input_list: List[float]) -> float:
    """ This Function takes a list input_list of floats as argument and returns their sum as a float.

    Args:
        input_list (list[float]): This is a a list of float numbers

    Returns:
        float: returns a float
    """
    result = sum(input_list)
    return result