#!/usr/bin/env python3
"""
    This module contains basic annotations practices
    Author: Peter Ekwere 
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ THis function takes a list mxd_lst of integers and floats and returns their sum as a float.

    Args:
        mxd_lst (List[Union[int, float]]): a list of ints and floats

    Returns:
        float: a float number
    """
    return sum(mxd_lst)