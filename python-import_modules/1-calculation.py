#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    add = add(a, b)
    sub = sub(a, b)
    mul = mul(a, b)
    div = div(a, b)

    print("{} + {} = {}".format(a, b, add))
    print("{} - {} = {}".format(a, b, sub))
    print("{} * {} = {}".format(a, b, mul))
    print("{} / {} = {}".format(a, b, div))