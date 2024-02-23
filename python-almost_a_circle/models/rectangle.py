#!/usr/bin/python3

"""
Module named `Rectangle` that contains the class `Rectangle`.
"""

from models.base import Base


class Rectangle(Base):
    """This is the Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a new Rectangle instance."""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Returns the width of the Rectangle instance."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the Rectangle instance."""
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """Returns the height of the Rectangle instance."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the Rectangle instance."""
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """Returns the x of the Rectangle instance."""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x of the Rectangle instance."""
        if type(value) is not int:
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """Returns the y of the Rectangle instance."""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y of the Rectangle instance."""
        if type(value) is not int:
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """Returns the area of the Rectangle instance."""
        return self.__width * self.__height

    def display(self):
        """Prints the Rectangle instance with the `#` character."""
        print("\n" * self.y, end="")
        for i in range(self.__height):
            print(" " * self.x, end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Returns a string representation of the Rectangle instance."""
        return (
            "[Rectangle] ({}) {}/{} - {}/{}"
            .format(self.id, self.x, self.y, self.width, self.height)
        )

    def update(self, *args, **kwargs):
        """Updates the Rectangle instance."""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """Returns the dictionary representation of the Rectangle instance."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
