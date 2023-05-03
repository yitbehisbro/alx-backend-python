#!/usr/bin/env python3
""" Async Generator """
import asyncio
import random


async def async_generator():
    """ Yields a random number between 0 and 10.
    """
    for _ in range(10):
        rand = random.uniform(0, 10)
        await asyncio.sleep(1)
        yield rand
