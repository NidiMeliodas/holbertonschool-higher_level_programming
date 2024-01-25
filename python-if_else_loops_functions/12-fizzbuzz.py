#!/usr/bin/python3
for i in range(1, 101):
    fizz = i % 3
    buzz = i % 5
    
    if fizz == 0:
        print("Fizz", end=' ')
    if buzz == 0:
        print("Buzz", end=' ')
    else:
        print(i, end=' ')

