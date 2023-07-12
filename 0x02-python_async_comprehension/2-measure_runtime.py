#!/usr/bin/env python3
'''Import async_generator from the previous task and then write a
coroutine called measure_runtime that will execute async_comprehension
four times in parallel using asyncio.gather.

measure_runtime should measure the total runtime and return it.

Notice that the total runtime is roughly 10 seconds, explain it to yourself.
'''

import asyncio
import time
import itertools as it

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Execute async_comprehension four times in parallel using
    asyncio.gather.
    '''
    time_start = time.perf_counter()
    await asyncio.gather(*list(it.repeat(async_comprehension(), 4)))
    return time.perf_counter() - time_start
