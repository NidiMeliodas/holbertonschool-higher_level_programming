#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# print number is positive si number est superieur a 0
if number > 0 :
	print("{} is positive".format(number))
# print number is negative si number est inferieur a 0
if number < 0 :
	print("{} is negative".format(number))
# print number is zero si number est egale a 0
if number == 0 :
	print("{} is zero".format(number))
	