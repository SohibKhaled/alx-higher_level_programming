#!/usr/bin/python3
"""
This module is composed by a function that adds two numbers
"""


def add_integer(x, y=98):
    """ Function that adds two integer and/or float numbers
    Args:
        a: first number
        b: second number
    Returns:
        The addition of the two given numbers
    Raises:
        TypeError: If a or b aren't integer and/or float numbers
    """

    if not isinstance(x, int) and not isinstance(x, float):
        raise TypeError("x must be an integer")
    if not isinstance(y, int) and not isinstance(y, float):
        raise TypeError("y must be an integer")
    x = int(x)
    y = int(y)
    return (x + y)
