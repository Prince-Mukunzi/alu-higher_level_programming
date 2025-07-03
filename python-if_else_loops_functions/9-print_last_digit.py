#!/usr/bin/python3
def print_last_digit(number):
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")

    last_digit = abs(number) % 10
    print(last_digit, end="")
    return last_digit
print_last_digit(98)
print_last_digit(0)
r = print_last_digit(-1024)
print(r)
