<<<<<<< HEAD
#!/usr/bin/python3

"""

"""

"""

"""
class Square:

    def __init__(self, size=0, position=(0, 0)) -> None:
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")

        if size < 0:
            raise ValueError("size must be >= 0")

        else:
            self._size = size
            self._position = position

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

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple(int, int)):
            raise TypeError("position must be a tuple of 2 positive integers")

        self._position = value

s = Square(0, (3,9))

s.my_print()
=======
#!/usr/bin/python3

"""

"""


class Square:
    """
    """
    def __init__(self, size=0, position=(0, 0)) -> None:
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")

        if size < 0:
            raise ValueError("size must be >= 0")

        else:
            self._size = size
            self._position = position
    """
    """
    def area(self) -> int:
        return self._size * self._size

    """
    """
    def my_print(self):
        if self._size == 0:
            print()

        else:
            print("#" * self._size)

    """
    """
    @property
    def size(self):
        return self._size

    """
    """
    @size.setter
    def size(self, value):
        self._size = value

    """
    """
    @property
    def position(self):
        return self._position

    """
    """
    @position.setter
    def position(self, value):
        if not isinstance(value, tuple(int, int)):
            raise TypeError("position must be a tuple of 2 positive integers")

        self._position = value
>>>>>>> db8b53dc32c3d822f0830eeca0dc643965d35dbb
