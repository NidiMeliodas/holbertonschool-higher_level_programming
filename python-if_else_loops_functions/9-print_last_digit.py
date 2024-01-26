#!/usr/bin/python3

def print_last_digit(number):
    if number < 0:
        number = number * -1
        print(number % 10)
    else:
        print(number % 10)
