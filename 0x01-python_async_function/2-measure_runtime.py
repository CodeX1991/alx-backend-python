#!/usr/bin/env python3
"""Measeure routime"""

import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int = 0, max_delay: int = 10) -> float:
    """
    Funtion that returns the time of execution

    Args:
        n: the count of execution
        max_delay: the delay seconds
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()

    total_time = end_time - start_time

    return total_time / n
