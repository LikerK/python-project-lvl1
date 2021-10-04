#!/usr/bin/env python
import prompt


def execute(game):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, {}!\n{}'.format(name, game.TASK))
    for i in range(3):
        question, correct_answer = game.get_round()
        print('Question:', question)
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print(
                "'{}' is wrong answer ;(. "
                "Correct answer was '{}'.\n"
                "Let's try again, {}!".format(answer, correct_answer, name))
            return
    return print('Congratulations, {}!'.format(name))
