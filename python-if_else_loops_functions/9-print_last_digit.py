#!/usr/bin/python3
def uppercase(str):
    print("{}".format("".join(chr(ord(char) - 32) if ord(char) >= 97 and
                              ord(char) <= 122 else char for char in str)))
    