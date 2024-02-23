#!/usr/bin/python3

"""
Module named `Square` that contains the class `Square`.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """This is the Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a new Square instance."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Returns the size of the Square instance."""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of the Square instance."""
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def __str__(self):
        """Returns the string representation of the Square instance."""
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.size))

    def update(self, *args, **kwargs):
        """Updates the Square instance."""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """Returns the dictionary representation of the Square instance."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
