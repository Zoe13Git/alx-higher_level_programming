#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div

    l_a = len(argv) - 1

    if l_a != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        str = "{} {} {} = {}"
        if argv[2] == '+':
            print(str.format(a, "+", b, add(a, b)))
        elif argv[2] == '-':
            print(str.format(a, "-", b, sub(a, b)))
        elif argv[2] == '*':
            print(str.format(a, "*", b, mul(a, b)))
        elif argv[2] == '/':
            print(str.format(a, "/", b, div(a, b)))
        else:
            print("Unknown operator. Available operators:",
                  "+, -, * and /")
            exit(1)