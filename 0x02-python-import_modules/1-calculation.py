#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
a = 10
b = 5
str = "10 {} 5 = {}"
if __name__ == "__main__":
    print(str.format("+", add(a, b)))
    print(str.format("-", sub(a, b)))
    print(str.format("*", mul(a, b)))
    print(str.format("/", div(a, b)))
