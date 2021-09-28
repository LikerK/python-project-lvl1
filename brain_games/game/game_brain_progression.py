#!/usr/bin/env python
from random import randint


TASK_GAME = 'What number is missing in the progression?'


def get_game_round():
    amount_number = randint(5, 10)
    start_number_progession = randint(1, 20)
    arithmetic_progression = randint(2, 10)
    result = []
    for i in range(amount_number):
        result.append(start_number_progession)
        start_number_progession += arithmetic_progression
    random_index = randint(0, len(result) - 1)
    correct_answer = result[random_index]
    result[random_index] = '..'
    result = ' '.join([str(a) for a in result])
    return result, str(correct_answer)
