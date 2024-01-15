#!/usr/bin/env python3
"""
    This Module contains basic practices on Async
    Author: Peter Ekwere
"""
import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """ This Funcition is an asynchronous coroutine 
    Args:
        max_delay (int, optional): this is the delay value. Defaults to 10.

    Returns:
        float: what is returned is a float
    """
    value = uniform(0, max_delay)
    await asyncio.sleep(value)
    return value
