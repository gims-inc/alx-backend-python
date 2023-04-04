#!/usr/bin/env python3
"""Task 4 --modify fucntion wait_n"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """wait_n alternative with

    """
    list_ = []
    for i in range(n):
        task_ = task_wait_random(max_delay)
        list_.append(task_)

    res = await asyncio.gather(*list_)

    return res
