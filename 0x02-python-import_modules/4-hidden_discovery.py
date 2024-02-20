#!/usr/bin/python3
if _name_ == "_main_":
    """Print all hidden directories"""
    import hidden_4

    name = dir(hidden_4):
    for name in name:
        if name[:2] != "_":
            print(name)
