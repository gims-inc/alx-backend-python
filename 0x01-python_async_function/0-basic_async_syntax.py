#!/usr/bin/env python3
"""Task 1: The basics of async"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """asynchronous coroutine that waits for a random delay
    returns a random float

    max_delay : Integer
    """
    delay_time = random.random() * max_delay
    await asyncio.sleep(delay_time)
    return delay_time
