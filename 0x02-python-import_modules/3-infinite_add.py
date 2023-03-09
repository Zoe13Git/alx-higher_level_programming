#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    l_a = len(argv) - 1
    sum = 0

    if (l_a == 0):
        print(0)
    else:
        for i in range(l_a):
            sum += int(argv[i + 1])
        print(sum)
