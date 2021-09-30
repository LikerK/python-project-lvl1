#!/usr/bin/env python
from random import choice, randint


LEFT_BORDER_INTERVAL = 1
RIGHT_BORDER_INTERVAL = 20


TASK = 'What is the result of the expression?'


def get_game_round():
    num1 = randint(LEFT_BORDER_INTERVAL, RIGHT_BORDER_INTERVAL)
    num2 = randint(LEFT_BORDER_INTERVAL, RIGHT_BORDER_INTERVAL)
    operators = ['+', '-', '*']
    rand_operator = choice(operators)
    if rand_operator == '+':
        result = num1 + num2
    elif rand_operator == '-':
        result = num1 - num2
    else:
        result = num1 * num2
    question = '{} {} {}'.format(num1, rand_operator, num2)
    return question, str(result)
