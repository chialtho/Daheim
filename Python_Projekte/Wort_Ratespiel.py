#! /usr/bin/env python3

import random

name = input("What is your name? ")

print("Good Luck! ", name)

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'java', 'water', 'board', 'geeks', 'bioinformatics']

word = random.choice(words)

print("Guess the characters")
guesses = ''
turns = 12

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end="")
        else:
            print("_", end="")
            failed += 1
    if failed == 0:
        print("\nYou win")
        print("The word is:", word)
        break
    guess = input(" Guess a character: ")
    guesses += guess
    if guess not in word:
        turns -= 1
        print("Wrong")
        print("You have ", turns, " more guesses")
        if turns == 0:
            print("You Loose")