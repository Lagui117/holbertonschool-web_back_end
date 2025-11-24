#!/usr/bin/env python3
"""Module for creating multiplier function."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Create a multiplier function.
    
    Args:
        multiplier: The multiplier value
        
    Returns:
        A function that multiplies a float by multiplier
    """
    def multiply(n: float) -> float:
        """Multiply n by multiplier."""
        return n * multiplier
    
    return multiply
