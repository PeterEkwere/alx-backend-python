#!usr/bin/env python3
"""
    This Module contains basic practices on Async
    Author: Peter Ekwere
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> int:
    """ This function waits for a random delay between 0 and max_delay """
    value = random.uniform(0, max_delay)
    await asyncio.sleep(value)
    return value


if __name__ == "__main__":
    pass