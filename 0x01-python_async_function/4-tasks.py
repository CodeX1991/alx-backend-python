#!/usr/bin/env python3
""" execute multiple coroutines at the same time with async"""


import asyncio
import random
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """
    Returns a lis of all delays

    Args:
        n: couunt to spawn wait_random
        max_delay: seconds to delay
    """
    delay_list: List[float] = []
    tasks: List[asyncio.Task] = []

    for _ in range(n):
        tasks.append(task_wait_random(max_delay))

    for task in asyncio.as_completed(tasks):
        delay = await task
        delay_list.append(delay)

    return delay_list
