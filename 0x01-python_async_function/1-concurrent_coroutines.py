#!/usr/bin/env python3
"""
    This module contains basic async practices
    Author: Peter Ekwere
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ This function will spawn wait_random n times with specified max_delay.

    Args:
        n (int): an integer
        max_delay (int): an integer

    Returns:
        List: This is a list of all delays
    """
    coroutines = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*coroutines)
    return sorted(results)
