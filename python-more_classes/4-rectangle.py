#!/usr/bin/python3
class Rectangle:
    def __init__(self, width=0, height=0):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    # setter method
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("Width must be an Integer")
        if value < 0:
            raise ValueError("Width must be >=0")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("Height must be an Integer")
        if value < 0:
            raise ValueError("Width must be >= 0")
        self._height = value

    def area(self):
        return self._width * self._height

    def perimeter(self):
        if self._width == 0 or self._height == 0:
            return "Perimiter: 0"
        else:
            return 2 * (self._height + self._width)

    def __str__(self):
        if self._width == 0 or self._height == 0:
            return ""
        return "\n".join(["#" * self._width for _ in range(self._height)])

    def __repr__(self):
        return f"Rectangle({self._width}, {self._height})"


my_rectangle = Rectangle(2, 4)
print(str(my_rectangle))
print("--")
print(my_rectangle)
print("--")
print(repr(my_rectangle))
print("--")
print(hex(id(my_rectangle)))
print("--")

# create new instance based on representation
new_rectangle = eval(repr(my_rectangle))
print(str(new_rectangle))
print("--")
print(new_rectangle)
print("--")
print(repr(new_rectangle))
print("--")
print(hex(id(new_rectangle)))
print("--")

print(new_rectangle is my_rectangle)
print(type(new_rectangle) is type(my_rectangle))
