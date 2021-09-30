#!/usr/bin/env python
from random import randint


LEFT_BORDER_INTERVAL = 1
RIGHT_BORDER_INTERVAL = 20

TASK = 'Find the greatest common divisor of given numbers.'


def is_gcd(random_num1, random_num2):
    while random_num1 != 0 and random_num2 != 0:
        if random_num1 > random_num2:
            random_num1 = random_num1 % random_num2
        else:
            random_num2 = random_num2 % random_num1
    return random_num1 + random_num2


def get_game_round():
    random_num1 = randint(LEFT_BORDER_INTERVAL, RIGHT_BORDER_INTERVAL)
    random_num2 = randint(LEFT_BORDER_INTERVAL, RIGHT_BORDER_INTERVAL)
    question = '{} {}'.format(random_num1, random_num2)
    correct_answer = is_gcd(random_num1, random_num2)
    return question, str(correct_answer)
