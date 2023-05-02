#!/usr/bin/env python3
""" Let's execute multiple coroutines
at the same time with async
"""
import asyncio
import heapq
from itertools import chain
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Spawn wait_random n times with the specified max_delay
    and returns the list of all the delays (float values)
    """
    lists = []
    for _ in range(n):
        lists.append(await asyncio.gather(task_wait_random(max_delay)))

    heapq.heapify(lists)    # Sorts the list
    sorted_lists = []
    while lists:
        sorted_lists.append(heapq.heappop(lists))

    return list(chain.from_iterable(sorted_lists))
