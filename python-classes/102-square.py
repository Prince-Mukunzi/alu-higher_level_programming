#!/usr/bin/python3
"""Square class with comparison operators."""


class Square:
    """A class that defines a square with comparison operators."""

    def __init__(self, size=0):
        """Initialize a square with size validation.

        Args:
            size (int or float): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the square.

        Returns:
            int or float: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int or float): The size of the square.

        Raises:
            TypeError: If value is not a number.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            int or float: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """Check if squares are equal based on area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if squares are not equal based on area."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Check if this square is less than other based on area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Check if this square is less than or equal to other."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Check if this square is greater than other based on area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if this square is greater than or equal to other."""
        return self.area() >= other.area()
