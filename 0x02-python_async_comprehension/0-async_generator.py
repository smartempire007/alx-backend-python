#!/usr/bin/env python3
'''Write a coroutine called async_generator that takes no arguments.

The coroutine will loop 10 times, each time asynchronously wait 1 second,
then yield a random number between 0 and 10. Use the random module.'''

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''Loop 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10.'''
    new_list = []
    for _ in range(10):
        new_list.append(random.uniform(0, 10))
    for i in new_list:
        await asyncio.sleep(1)
        yield i
