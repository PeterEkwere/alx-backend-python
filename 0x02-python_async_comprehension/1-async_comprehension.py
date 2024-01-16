#!/usr/bin/env python3
"""
    This Module contains basic async practices
    Author: Peter Ekwere
"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List:
    """ async comprehensing over async_generator

    Returns:
        List:
    """
    a_list = []
    async for i in async_generator():
        a_list.append(i)
    return a_list
