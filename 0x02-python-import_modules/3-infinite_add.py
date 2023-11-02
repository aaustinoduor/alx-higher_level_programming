#!/usr/bin/python3
if __name__ == "__main__":
    import sys, math
    result = 0
    for j in sys.argv:
        result += int(j)
        print("{}".format(result))
