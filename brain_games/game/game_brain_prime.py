#!/usr/bin/env python
from random import randint


first_number = 1
second_number = 20

task_game = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_game_round():
    number = randint(first_number, second_number)
    d = 2
    while number % d != 0:
        d += 1
    if number == d:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return number, correct_answer
