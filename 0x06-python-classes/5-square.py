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
            self._size = size

    def area(self) -> int:
        return self._size * self._size

    def my_print(self):
        if self._size == 0:
            print()

        else:
            print("#" * self._size)

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value