#!/usr/bin/env python3
'''Import wait_random from 0-basic_async_syntax.

Write a function (do not create an async function, use the regular
function syntax to do this) task_wait_random that takes an integer
max_delay and returns a asyncio.Task.'''

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the total execution time for
    `wait_n(n, max_delay)`, and returns `total_time / n`."""
    s: float = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    return (time.perf_counter() - s) / n
