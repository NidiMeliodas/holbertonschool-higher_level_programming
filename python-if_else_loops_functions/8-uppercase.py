#!/usr/bin/python3

def uppercase(str):

    up_str = ""

    for ch in str:
        asc = ord(ch)
        if asc >= 97 and asc <= 122:
            up_str += chr(asc-32)
        else:
            up_str += ch

    print("{}".format(up_str))
    