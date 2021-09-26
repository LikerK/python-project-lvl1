#!/usr/bin/env python
from random import randint


first_number = 1
second_number = 20

task_game = 'Find the greatest common divisor of given numbers.'


def get_game_round():
    random_num1 = randint(first_number, second_number)
    random_num2 = randint(first_number, second_number)
    question = '{} {}'.format(random_num1, random_num2)
    while random_num1 != 0 and random_num2 != 0:
        if random_num1 > random_num2:
            random_num1 = random_num1 % random_num2
        else:
            random_num2 = random_num2 % random_num1
    correct_answer = random_num1 + random_num2
    return question, str(correct_answer)
