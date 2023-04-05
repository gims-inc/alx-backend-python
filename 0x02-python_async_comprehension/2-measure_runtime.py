#!/usr/bin/env python3
"""coroutine that will execute async_comprehension four
times in parallel using asyncio.gather
"""
import time
import asyncio


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure the total runtime and return it.
    """
    start_time = time.time()
    tasks = [asyncio.create_task(async_comprehension()) for i in range(4)]

    await asyncio.gather(*tasks)

    return (time.time() - start_time)
