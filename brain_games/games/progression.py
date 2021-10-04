#!/usr/bin/env python
from random import randint


TASK = 'What number is missing in the progression?'


LEFT_BORDER_OF_LENGHT = 5
RIGHT_BORDER_OF_LENGHT = 10
LEFT_BORDER_OF_DIFF = 2
RIGHT_BORDER_OF_DIFF = 10
LEFT_BORDER_OF_BEGINNING = 1
RIGHT_BORDER_OF_BEGINNING = 20


def build_progression(initial_term_of_progression, difference):
    progression = [initial_term_of_progression]
    amount_number = randint(LEFT_BORDER_OF_LENGHT, RIGHT_BORDER_OF_LENGHT)
    for i in range(amount_number):
        progression.append(progression[i] + difference)
    return progression


def get_string_from_progression(progression, random_index):
    str_progression = []
    progression[random_index] = '..'
    str_progression = ' '.join([str(a) for a in progression])
    return str_progression


def get_round():
    initial_term_of_progression = randint(
        LEFT_BORDER_OF_BEGINNING,
        RIGHT_BORDER_OF_BEGINNING)
    difference = randint(LEFT_BORDER_OF_DIFF, RIGHT_BORDER_OF_DIFF)
    progression = build_progression(initial_term_of_progression, difference)
    random_index = randint(0, len(progression) - 1)
    answer = progression[random_index]
    str_progression = get_string_from_progression(progression, random_index)
    return str_progression, str(answer)
