# Blu's Game Centre v1.0
# Aiyurn © 2016

import random
import time
from arithmetic import arithmetic
from numguess import numguess
from bluadventure import bluadventure

# Introduction - Game Choice variable
gamechoice = ""

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

# Start - Other messages
other1 = ["Hey that not an option!",
          "I think you typed something wrong... There's no option for that.",
          "Are you purposely typing something wrong to get me to talk? If you are it's not working!",
          "I don't think that option you typed is an option...",
          "Come let's go and play something already! There isn't that many games to choose from!"]

# --------------- CODE BEGINS HERE ---------------


while gamechoice == "":
    # Introduction text
    print("Blu's Game Centre v1.0\n"
          "Aiyurn (C) 2016\n")
    time.sleep(1)
    print("Welcome to my Game Centre!")
    time.sleep(1)
    print("I'm Blu, and I'll be helping you out with things in this program!")
    time.sleep(3)
    print("Here are the games you can choose from:\n"
          "1) Arithmetic (Multiplication)\n"
          "2) Number Guess\n"
          "3) Find-a-word [IN DEVELOPMENT]\n"
          "4) Blu's Adventures [BETA]")

    # Start
    gamechoice = input("> ")
    while True:
        if gamechoice in game_arithmetic:
            print(random.choice(arithmeticmsg))
            time.sleep(2)
            print("\n"*2)
            arithmetic()
            gamechoice = ""
            break

        elif gamechoice in game_numguess:
            print(random.choice(numguessmsg))
            time.sleep(2)
            print("\n"*2)
            numguess()
            gamechoice = ""
            break

        elif gamechoice in game_cyoa:
            print(random.choice(cyoa))
            time.sleep(2)
            print("\n"*2)
            bluadventure()
            gamechoice = ""
            break

        else:
            print(random.choice(other1))
            gamechoice = input("> ")
        '''
        elif gamechoice in game_findaword:
            print(random.choice(findaword))
            time.sleep(2)
            print("\n"*2)
            break
        '''

    time.sleep(2)
    print("Hello!")