#!/usr/bin/python3
from ..7-base_geometry import BaseGeometry


class Rectangle(BaseGeometry):
    """A class representing a rectangle, inheriting from BaseGeometry.

    Attributes:
        __width (int): The width of the rectangle (private).
        __height (int): The height of the rectangle (private).

    Args:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.

    Raises:
        TypeError: If width or height is not an integer.
        ValueError: If width or height is less than or equal to 0.
    """

    def __init__(self, width, height):
        """Initializes the rectangle with the given width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
        """

        super().__init__()
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """

        return self.__width * self.__height

    def __str__(self):
        """Returns a string representation of the rectangle.

        Returns:
            str: A string representation of the rectangle.
        """

        return "[Rectangle] {}/{}".format(self.__width, self.__height)

