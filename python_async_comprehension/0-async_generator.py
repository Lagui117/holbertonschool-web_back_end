#!/usr/bin/env python3
"""
Module that contains an async generator coroutine.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator that yields 10 random numbers between 0 and 10.
    Each iteration waits 1 second before yielding.

    Yields:
        Random float values between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
