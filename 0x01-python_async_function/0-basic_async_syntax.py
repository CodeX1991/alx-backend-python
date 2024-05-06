#!/usr/bin/env python3
"""Async module"""

import asyncio
import random


async def wait_random(max_delay=10):
    """
    An asynchronous coroutine

    Attr:
        max_delay: upper bound for random integer
    """
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)

    return random_delay
