#!/usr/bin/env python3
"""Tasks module"""

import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """Returns a asyncio.Task.

    args:
        max_delay: delay count in sec
    """
    task = asyncio.create_task(wait_random(max_delay))

    return task
