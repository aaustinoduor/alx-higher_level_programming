#!/usr/bin/python3
""" Magic String"""


def magic_string(my_list=[]) -> str:
    """_summary_

    Args:
        my_list (list, optional): _description_. Defaults to [].

    Returns:
        str: _description_
    """
    my_list.append("BestSchool")
    return ', '.join(my_list)
