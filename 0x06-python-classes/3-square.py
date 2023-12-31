#!/usr/bin/python3

"""

"""

"""

"""
class Square:

    def __init__(self, size=0) -> None:
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        else:
            self.size = size

    def area(self) -> int:
        return self.size * self.size
