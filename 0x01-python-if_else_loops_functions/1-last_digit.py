#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number >= 0:
    last_digit = number % 10
else:
    last_digit = ((number * -1) % 10) * -1

text = "Last digit of {} is {} and is".format(number, last_digit)

if last_digit > 5:
    print(text, "greater than 5")

elif last_digit == 0:
    print(text, "0")

else:
    print(text, "less than 6 and not 0")
