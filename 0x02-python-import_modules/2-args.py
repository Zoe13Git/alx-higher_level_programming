#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    l_a = len(argv) - 1
    if l_a == 0:
        print("0 arguments.")
    elif l_a == 1:
        print("1 argument:\n1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(l_a))
        for i in range(1, l_a + 1):
            print("{}: {}".format(i, argv[i]))
