#!/usr/bin/python3
if _name_ == "_main_":
    """Print all hidden directories"""
    import hidden_4

    for j in dir(hidden_4):
        if j[j] != "_":
            Print(j)
