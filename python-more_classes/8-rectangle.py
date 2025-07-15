#!/usr/bin/python3
class Rectangle:
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        Rectangle.number_of_instances += 1
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
        return "\n".join([str(self.print_symbol) * self._width for _ in range(self._height)])

    def __repr__(self):
        return f"Rectangle({self._width}, {self._height})"

    def __del__(self):
        print("Bye rectangle...")
        self.__class__.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2


my_rectangle_1 = Rectangle(8, 4)
my_rectangle_2 = Rectangle(2, 3)

if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
    print("my_rectangle_1 is bigger or equal to my_rectangle_2")
else:
    print("my_rectangle_2 is bigger than my_rectangle_1")


my_rectangle_2.width = 10
my_rectangle_2.height = 5
if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
    print("my_rectangle_1 is bigger or equal to my_rectangle_2")
else:
    print("my_rectangle_2 is bigger than my_rectangle_1")
