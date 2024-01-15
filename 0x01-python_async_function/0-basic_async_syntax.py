#!usr/bin/env python3
"""
    This Module contains basic practices on Async
    Author: Peter Ekwere
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ This Funcition is an asynchronous coroutine that
        takes in an integer argument (max_delay, with a default value of 10)
        named wait_random that waits for a random delay between 0 and max_delay
        (included and float value) seconds and eventually returns it.

    Args:
        max_delay (int, optional): this is the delay value. Defaults to 10.

    Returns:
        float: what is returned is a float
    """
    value = random.uniform(0, max_delay)
    await asyncio.sleep(value)
    return value


if __name__ == "__main__":
    pass
