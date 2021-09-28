#!/usr/bin/env python
import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    return name


def get_game(game):
    name = welcome_user()
    print(game.TASK_GAME)
    for i in range(3):
        question, correct_answer = game.get_game_round()
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
