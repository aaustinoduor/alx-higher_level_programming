<<<<<<< HEAD
#!/usr/bin/python3
"""define a class sqare."""


class Square:
    """represent a square."""

    def __init__(self, size=0):
        """initialize a new Square.
        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
=======
#!/usr/bin/python3

"""

"""


class Square:
    """_summary_
    """
    def __init__(self, size=0) -> None:
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        else:
            self._size = size
>>>>>>> db8b53dc32c3d822f0830eeca0dc643965d35dbb
