#!/usr/bin/python3
for j in range(100):
    print(f"{j:02d}", end=", " if j < 99 else "\n")
    if j < 99:
        print("{j:02d}, ".format(j), end=", ")
    else:
        print("{j:02d}".format(j))
