#!/usr/bin/python3

def uppercase(input_str):
    for char in input_str:
        upper_char = chr(ord(char) - ord('a') + ord('A'))
        print(upper_char, end='')

    # Move the 'else' block to be aligned with the 'for' loop
    else:
        print()
