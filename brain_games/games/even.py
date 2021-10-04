#!/usr/bin/env python
from random import randint


LEFT_BORDER = 1
RIGHT_BORDER = 20


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def get_round():
    number = randint(LEFT_BORDER, RIGHT_BORDER)
    correct_answer = 'yes' if is_even(number) else 'no'
    return number, correct_answer
