#!/usr/bin/env python3
""" The basics of async """
import random


async def wait_random(max_delay=10):
    """ Waits for a random delay between 0 and max_delay
    seconds and eventually returns it.
    """
    rand = random.uniform(0, max_delay)
    return rand
