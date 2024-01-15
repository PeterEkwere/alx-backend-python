#!/usr/bin/env python3
"""
    This module contains basic practice on async
    Author: Peter Ekwere
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ This function will spawn wait_random n times with specified max_delay.

    Args:
        n (int): an integer
        max_delay (int): an integer

    Returns:
        List: This is a list of all delays
    """
    coroutines = [task_wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*coroutines)
    return sorted(results)
