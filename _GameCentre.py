# Blu's Game Centre v1.0
# Aiyurn © 2016

import random
from time import sleep
import sys
from games import arithmetic,numguess,bluadventure

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def print_slowly(text, speed):
    for c in text:
        print(c, end=""),
        sys.stdout.flush()
        sleep(speed)

# Introduction - Variables
gamechoice = ""
menutime = 0

# Start - Game Choice input options
game_arithmetic = ["1", "a", "arithmetic"]
game_numguess = ["2", "n", "number guess",]
game_findaword = ["3", "f", "find-a-word", "find a word"]
game_cyoa = ["4", "c", "cyoa", "choose your own adventure"]

# Start - Arithmetic messages
arithmeticmsg = ["Let's test out your maths skills!",
                 "Time to put your maths to the test!",
                 "Arithmetic? Sure let's go!",
                 "So you like maths I see... Let's see how good you are!",
                 "I, Blu, challenge you to a maths battle!"]

# Start - Number Guess messages
numguessmsg = ["lets go!"]

# Start - Blu Adventure's messages
cyoamsg = ["test",
           "test2"]

# Start - Other messages
other1 = ["Hey that not an option!",
          "I think you typed something wrong... There's no option for that.",
          "Are you purposely typing something wrong to get me to talk? If you are it's not working!",
          "I don't think that option you typed is an option...",
          "Come let's go and play something already! There isn't that many games to choose from!"]

# --------------- CODE BEGINS HERE ---------------


while gamechoice == "":
    # Introduction text
    if menutime < 1:
        print_slowly("Blu's Game Centre v1.0\n", 0.1)
        print_slowly("Aiyurn (C) 2016\n\n", 0.1)
        sleep(1.5)
        print_slowly("Welcome to my Game Centre!\n", 0.01)
        sleep(1)
        print_slowly("I'm Blu, and I'll be helping you out with things in this program!\n", 0.01)
        sleep(3)
        print("Here are the games you can choose from:\n"
              "1) Arithmetic (Multiplication)\n"
              "2) Number Guess\n"
              "3) Find-a-word [IN DEVELOPMENT]\n"
              "4) Blu's Adventures [BETA]\n"
              "5) Guess the country [IN DEVELOPMENT]")
    else:
        print("And we're back at the menu again! What game do you want to play now?")
        print("Here are the games:\n"
              "1) Arithmetic (Multiplication)\n"
              "2) Number Guess\n"
              "3) Find-a-word [IN DEVELOPMENT]\n"
              "4) Blu's Adventures [BETA]")

    # Start
    gamechoice = input("> ")
    while True:
        if gamechoice in game_arithmetic:
            print(random.choice(arithmeticmsg))
            sleep(2)
            print("\n"*2)
            arithmetic()
            gamechoice = ""
            break

        elif gamechoice in game_numguess:
            print(random.choice(numguessmsg))
            sleep(2)
            print("\n"*2)
            numguess()
            gamechoice = ""
            break

#       elif gamechoice in game_findaword:
#       print(random.choice(findaword))
#       time.sleep(2)
#       print("\n"*2)
#           break

        elif gamechoice in game_cyoa:
            print(random.choice(cyoamsg))
            sleep(2)
            print("\n"*2)
            bluadventure()
            gamechoice = ""
            break

        else:
            print(random.choice(other1))
            gamechoice = input("> ")

    sleep(2)
