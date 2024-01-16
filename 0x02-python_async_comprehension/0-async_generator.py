#!/usr/bin/env python3
"""
    This Module contains basic async practices
    Author: Peter Ekwere
"""
import asyncio
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ This funcition yields an integer

    Returns:
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
