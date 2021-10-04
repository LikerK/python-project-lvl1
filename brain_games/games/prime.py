#!/usr/bin/env python
from random import randint


LEFT_BORDER = 1
RIGHT_BORDER = 20

TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    d = 2
    while number % d != 0:
        d += 1
    if number == d:
        return True
    else:
        return False


def get_round():
    number = randint(LEFT_BORDER, RIGHT_BORDER)
    correct_answer = 'yes' if is_prime(number) else 'no'
    return number, correct_answer
