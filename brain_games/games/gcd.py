#!/usr/bin/env python
from random import randint


LEFT_BORDER = 1
RIGHT_BORDER = 20


TASK = 'Find the greatest common divisor of given numbers.'


def get_gcd(first_number, second_number):
    while first_number != 0 and second_number != 0:
        if first_number > second_number:
            first_number = first_number % second_number
        else:
            second_number = second_number % first_number
    return first_number + second_number


def get_round():
    random_first_number = randint(LEFT_BORDER, RIGHT_BORDER)
    random_second_number = randint(LEFT_BORDER, RIGHT_BORDER)
    question = '{} {}'.format(random_first_number, random_second_number)
    correct_answer = get_gcd(random_first_number, random_second_number)
    return question, str(correct_answer)
