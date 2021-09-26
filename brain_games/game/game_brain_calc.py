#!/usr/bin/env python
from random import choice, randint


first_number = 1
second_number = 20


task_game = 'What is the result of the expression?'


def get_game_round():
    num1 = randint(first_number, second_number)
    num2 = randint(first_number, second_number)
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
