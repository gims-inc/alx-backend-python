#!/usr/bin/env python3
"""use the regular function syntax to create an async fxn"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """regular function that takes an integer max_delay and
    returns a asyncio.Task.

    max_delay: int
    returns asyncio.Task
    """
    return asyncio.create_task(wait_random(max_delay))
