#!/usr/bin/python3

import hidden_4

if __name__ == "__main__":
    names = dir(hidden_4)
    # sort names
    names.sort()
    for name in names:

        # check if name begins with __
        if name[:2] != "__":
            print(name)
