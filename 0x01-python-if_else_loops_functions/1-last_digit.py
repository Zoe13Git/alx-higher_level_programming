#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = (abs(number) % 10 * -1) if number < 0 else abs(number)%10
string = "The last digit of " + str(number) + " is " + \
        str(last_digit) + " {}"
if last_digit > 5:
    print(string.format("and is greater than 5"))
elif last_digit == 0:
    print(string.format("and is 0"))
else:
    print(string.format("and is less than 6 and not 0"))
