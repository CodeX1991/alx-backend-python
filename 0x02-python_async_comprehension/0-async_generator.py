#!/usr/bin/env python3
"""Async Generator"""


from typing import Generator
import random
import asyncio


async def async_generator() -> Generator[int, None, None]:
    """Return a random value"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
