#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    a = 10
    b = 5
    str = "{0} {2} {1} = {3}"

    print(str.format(a, b, "+", add(a, b)))
    print(str.format(a, b, "-", sub(a, b)))
    print(str.format(a, b, "*", mul(a, b)))
    print(str.format(a, b, "/", div(a, b)))
