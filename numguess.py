# Blu's Game Centre - Number Guess v1.0
# Aiyurn (C) 2016

import random
import time

easy = ["e", "easy", "1"]
normal = ["n", "normal", "2"]
hard = ["h", "hard", "3"]
insane = ["i", "insane", "4"]
superinsane = ["s", "super insane", "5"]

easymsg = ["Aww easy mode? Oh well, let's go"]
normalmsg = ["So you're one of those average players. Now, let's begin!"]
hardmsg = ["I see you chose hard mode. I wish you luck."]
insanemsg = ["You're insane for choosing insane!"]
superinsanemsg = ["If you can complete this you are definitely a robot..."]

other3 = ["yo"]


def numguess():
    print("Think you're up for a game of number guessing?")
    time.sleep(1)
    print("Here are three difficulties:\n"
          "For Easy, type 'e'\n"
          "For Normal, type 'n'\n"
          "For Hard, type 'h'\n"
          "For Insane, type 'i'\n"
          "For Super Insane, type 's'")
    diff = input("> ")

    while True:
        if diff in easy:
            print(random.choice(easymsg))
            print("You'll have 30 lives to guess a number between 1-1000")
            lives = 30
            num = 1000
            break
        elif diff in normal:
            print(random.choice(normalmsg))
            print("You'll have 25 lives to guess a number between 1-1500")
            lives = 25
            num = 1500
            break
        elif diff in hard:
            print(random.choice(hardmsg))
            print("You'll have 20 lives to guess a number between 1-2200")
            lives = 20
            num = 2200
            break
        elif diff in insane:
            print(random.choice(insanemsg))
            print("You'll have 10 lives to guess a number between 1-5000")
            lives = 10
            num = 5000
            break
        elif diff in superinsane:
            print(random.choice(superinsanemsg))
            print("You'll have 5 lives to guess an number between 1-10000")
            lives = 5
            num = 10000
            break
        else:
            print(random.choice(other3))
            diff = input("> ")

    a = random.randint(1, num)  # Choose a random number between 1 and a number depending on the difficulty selected
    deaths = 0
    guess = 0
    print("Guess a number between 1-" + str(num) + ":")
    while lives > deaths:
        guess = input("> ")
        while not guess.isdigit():  # Checks if the input entered is a number
            print("That is not a number!")
            guess = input("> ")
        guess = int(guess)
        if guess > int(num):
            print("Its between 1-" + str(num) + "... It can't go higher than", str(num) + ".")
        elif guess < 0:
            print("Its between 1-" + str(num) + "... It can't go lower than 0.")
        elif guess < a:
            print("Higher!")
            deaths = deaths + 1
        elif guess > a:
            print("Lower!")
            deaths = deaths + 1
        if guess == a:
            print("Correct!")
            deaths = deaths + 1
            print("It took you", deaths, "guess(es) this round!")
        if deaths == lives:
            print("One more life remaining be careful.")
        if deaths > lives:
            print("Game over")
            print("good try but the answer was", a + ".")