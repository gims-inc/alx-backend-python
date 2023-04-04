#!/usr/bin/env python3
"""Task 1 --multiple coroutines at the same"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """async routine takes 2 int arguments.spawns wait_random
    n times with the specified max_delay.

    n: int
    max_delay: int
    return List of floats
    """
    list_ = []
    for i in range(n):
        task_ = asyncio.create_task(wait_random())
        list_.append(task_)

    delay_times = [await task for task in asyncio.as_completed(list_)]

    return sorted(delay_times)
