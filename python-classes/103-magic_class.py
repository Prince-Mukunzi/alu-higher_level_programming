#!/usr/bin/python3
"""MagicClass matching given bytecode."""
import math


class MagicClass:
    """A class that matches the given bytecode."""

    def __init__(self, radius=0):
        """Initialize MagicClass with radius validation.

        Args:
            radius (int or float): The radius value.

        Raises:
            TypeError: If radius is not a number.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculate and return the area.

        Returns:
            float: The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculate and return the circumference.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
