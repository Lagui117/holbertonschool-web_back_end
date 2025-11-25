#!/usr/bin/env python3
"""
Module that contains an asynchronous coroutine wait_random.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and
    max_delay seconds and returns the delay.

    Args:
        max_delay: Maximum delay in seconds (default: 10)

    Returns:
        The actual delay waited (float value)
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
