#!/usr/bin/env python
from random import randint


first_number = 1
second_number = 10


task_game = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_game_round():
    rand_number = randint(first_number, second_number)
    if rand_number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return rand_number, correct_answer
