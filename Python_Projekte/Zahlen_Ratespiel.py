#! /usr/bin/env python3

import random
import math

lower = int(input("Enter lower bound: "))
upper = int(input("Enter upper bound: "))
x = random.randint(lower, upper)

print("\n\tYou've only ", round(math.log(upper - lower +1 , 2)), " chances to guess the number!\n")

counter = 0

while counter < math.log(upper - lower +1 , 2):
    counter += 1
    guess = int(input("Guess a number: "))

    if x == guess:
        print("Congratulations you did it in ", counter, " tries")
        break
    elif x > guess:
        print("You guessed to small!")
    elif x < guess:
        print("You guessed too high!")

if counter >= math.log(upper - lower +1 , 2):
    print("\nThe number is %d"%x)
    print("\tBetter Luck next time!")
