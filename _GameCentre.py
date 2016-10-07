# Blu's Game Centre v1.0
# Aiyurn © 2016

from random import randint
from time import sleep
from games import arithmetic, numguess, bluadventure
from definitions import sprint

# Introduction - Variables
gamechoice = ""
menutime = 0

# Start - Game Choice input options
game_arithmetic = ["1", "a", "arithmetic"]
game_numguess = ["2", "n", "number guess"]
game_findaword = ["3", "f", "find-a-word", "find a word"]
game_cyoa = ["4", "c", "cyoa", "choose your own adventure"]

# Start - Number Guess messages
numguessmsg = ["Like number guessing I see... Let's go!",
               "Let's see if you can beat me, "]

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

sprint("Blu's Game Centre v1.0\n", 0.07, 0.7)
sprint("Aiyurn (C) 2016\n\n", 0.07, 1.5)

while gamechoice == "":
    # Introduction text
    if menutime < 1:
        sprint("Welcome to my Game Centre!\n", "default", "period")
        sprint("I'm Blu, ", "default", "comma")
        sprint("and I'll be joining you in the games you play in this program!\n", "default", "period")
        sprint("Here are the games you can choose from:\n", "default", "colon")
        sprint("1) Arithmetic (Multiplication)\n", "default", "list")
        sprint("2) Number Guess\n", "default", "list")
        sprint("3) Find-a-word [IN DEVELOPMENT]\n", "default", "list")
        sprint("4) Blu's Adventures [BETA]\n", "default", "list")
        sprint("5) Tactical World [IN DEVELOPMENT]\n", "default", "list")
        sprint("6) Word Jam [IN DEVELOPMENT]\n", "default", "list")
        sprint("So, ", "default", "comma")
        sprint("what game do you want to play?\n", "default", "input")
    else:
        print("And we're back at the menu again! What game do you want to play now?")
        print("Here are the games:\n"
              "1) Arithmetic (Multiplication)\n"
              "2) Number Guess\n"
              "3) Find-a-word [IN DEVELOPMENT]\n"
              "4) Blu's Adventures [BETA]\n"
              "5) Guess the country [IN DEVELOPMENT\n"
              "6) Letter Scramble [IN DEVELOPMENT")

    # Start
    gamechoice = input("> ")
    while True:
        value = randint(1,5)
        if gamechoice in game_arithmetic:
            if value == 1:
                sprint("Let's test out your maths skills!", "default", "mark")
            elif value == 2:
                sprint("Time to put your maths to the test!", "default", "mark")
            elif value == 3:
                sprint("Arithmetic? ", "default", "mark")
                sprint("Sure let's go!", "default", "mark")
            elif value == 4:
                sprint("So you like maths I see... ", "default", "period")
                sprint("Let's see how good you are!", "default", "mark")
            elif value == 5:
                sprint("I, ", "default", "comma")
                sprint("Blu, ", "default", "comma")
                sprint("challenge you to a maths battle!", "default", "mark")
            sleep(2)
            print("\n" * 2)
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

        elif gamechoice == 'quit':
            quit()

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
