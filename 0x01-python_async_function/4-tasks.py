#!/usr/bin/env python3
'''Take the code from wait_n and alter it into a new function task_wait_n.
The code is nearly identical to wait_n except task_wait_random is being
called.'''

import asyncio
import itertools as it
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ return the list of all the delays (float values)
    generated from wait_random"""
    resp = await asyncio.gather(*(it.repeat(task_wait_random(max_delay), n)))
    return list(resp)
