#!/usr/bin/env python
from random import randint


TASK = 'What number is missing in the progression?'


def build_progression(start_number_progession, step):
    progression = []
    amount_number = randint(5, 10)
    for i in range(amount_number):
        progression.append(start_number_progession)
        start_number_progession += step
    random_index = randint(0, len(progression) - 1)
    return progression, random_index


def get_string_from_progression(progression, random_index):
    str_progression = []
    progression[random_index] = '..'
    str_progression = ' '.join([str(a) for a in progression])
    return str_progression


def get_game_round():
    start_number_progession = randint(1, 20)
    step = randint(2, 10)
    progression, random_index = build_progression(start_number_progession, step)
    answer = progression[random_index]
    str_progression = get_string_from_progression(progression, random_index)
    return str_progression, str(answer)
