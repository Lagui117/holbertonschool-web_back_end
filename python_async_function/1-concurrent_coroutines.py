#!/usr/bin/env python3
"""
Module that contains an async routine wait_n.
"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay and returns
    the list of all delays in ascending order.

    Args:
        n: Number of times to spawn wait_random
        max_delay: Maximum delay in seconds

    Returns:
        List of delays in ascending order
    """
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    
    # Sort the delays manually without using sort() to maintain concurrency
    sorted_delays = []
    delays_list = list(delays)
    
    while delays_list:
        min_delay = delays_list[0]
        min_index = 0
        for i in range(1, len(delays_list)):
            if delays_list[i] < min_delay:
                min_delay = delays_list[i]
                min_index = i
        sorted_delays.append(delays_list.pop(min_index))
    
    return sorted_delays
