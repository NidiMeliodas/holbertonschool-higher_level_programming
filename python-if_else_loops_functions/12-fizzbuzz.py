#!/usr/bin/python3
for i in range(1, 101):
    fizz = i % 3
    buzz = i % 5

    if fizz == 0 and buzz == 0:
        print("FizzBuzz", end=' ')
        continue
    if fizz == 0:
        print("Fizz", end=' ')
        continue
    if buzz == 0:
        print("Buzz", end=' ')
        continue
    else:
        print(i, end=' ')
