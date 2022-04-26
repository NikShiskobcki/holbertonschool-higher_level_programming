#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
numberAux = number
if number < 0:
    numberAux = number * -1
last_digit = numberAux % 10
if number < 0:
    last_digit = last_digit * -1
if last_digit == 0:
    print("Last digit of", number, "is", last_digit, "and is 0")
elif last_digit < 6:
    print("Last digit of", number, "is", last_digit, "and is less than 6 and not 0")
else: 
    print("Last digit of", number, "is", last_digit, "and is greater than 5")
