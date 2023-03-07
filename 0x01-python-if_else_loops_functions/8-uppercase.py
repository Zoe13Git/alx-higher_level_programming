#!/usr/bin/python3
def uppercase(str):
    for s in str:
        print("{}".format(chr(ord(s) - 32))if (ord(s) >= 97
              and ord(s) <= 123) else "{}".format(s), end="")
    print("", end="\n")
