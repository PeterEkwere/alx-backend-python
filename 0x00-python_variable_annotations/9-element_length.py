#!/usr/bin/env python3
"""
    This Module contains basic annotation practices
    Author: Peter Ekwere
"""
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ This function takes a list of strings

    Args:
        lst (Iterable[Sequence]): _description_

    Returns:
        List[Tuple[Sequence, int]]: _description_
    """
    return [(i, len(i)) for i in lst]