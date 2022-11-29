#!/usr/bin/python3
for i in range(0, 100):
    # The smallest combination occurs when the unit digit is larger
    #  than the tenth digit i.e in 45, 5 is larger than 4
    if (i % 10) - ((i/10) % 10) > 0:
        if i != 89:
            print("{}, ".format(i), end="")
        else:
            print("{}".format(i))
