#!/usr/bin/env python3
from random import randint
import prompt


first_number = 1
second_number = 10

def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    chek = 0
    while chek < 3:
        rand_number = randint(first_number, second_number)
        print('Question:', rand_number)
        answer = prompt.string('Your answer: ')
        if rand_number % 2 == 0:
            parity_number = 'yes'
        else:
            parity_number = 'no'
        if answer == parity_number:
            print('Correct!')
            chek += 1
        else:
            return print("'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {}!".format(name))
    return print('Congratulations, {}!'.format(name))

if __name__ == "__main__":
    main()