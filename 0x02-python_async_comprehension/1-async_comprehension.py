#!/usr/bin/env python3
"""Task 2 --Async Comprehensions"""
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """coroutine, collects 10 random numbers using an async
    comprehensing over async_generator

    return the 10 random numbers
    """
    return [i async for i in async_generator()]
