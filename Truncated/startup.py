# -*- coding: utf-8 -*-
# Blu's Game Centre v1.0
'''
    _    _
   / \  (_)_   _ _   _ _ __ _ __
  / _ \ | | | | | | | | '__| '_ \
 / ___ \| | |_| | |_| | |  | | | |
/_/   \_\_|\__, |\__,_|_|  |_| |_|
           |___/
'''

# http://stackoverflow.com/questions/4099422/printing-slowly-simulate-typing
# http://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console

# --------------- IMPORTS ---------------
import sys
from random import randint
from time import sleep as s
from games import arithmetic, numguess
from sprint import sprint

# --------------- DEFINITIONS ---------------


def progressbar(iteration, total, prefix='', suffix='', decimals=1, bar_length=100):
    format_str = "{0:." + str(decimals) + "f}"
    percents = format_str.format(100 * (iteration / float(total)))
    filled_length = int(round(bar_length * iteration / float(total)))
    bar = '█' * filled_length + '-' * (bar_length - filled_length)
    sys.stdout.write('\r%s |%s| %s%s %s' % (prefix, bar, percents, '%', suffix)),
    if iteration == total:
        sys.stdout.write('\n')
    sys.stdout.flush()

# --------------- VARIABLES ---------------
game_choice = ""
game_selected = 0
menu_time = 0
give_name = ""
asked_name = 0
read_warning = 0
warning_yes = ["y", "ye", "yes"]
warning_no = ["n", "no"]
items = list(range(0, 110))
i = 0
l = len(items)
game_arithmetic = ["1", "a", "arithmetic"]
game_numguess = ["2", "n", "number guess"]

# ---------------------------------- CODE BEGINS HERE ----------------------------------


# --------------- INTRODUCTION ---------------
print("Blu's Game Centre v1.0")
print("Aiyurn (C) 2016\n")
s(1)

# --------------- WARNING PROMPT ---------------
print("Have you read the warning before? (Yes / No)")
warning = input("> ")
warning = warning.lower()
while read_warning == 0:
    if warning in warning_yes:
        print("Welcome back!")
        s(1)
        print()
        read_warning = 1
    elif warning in warning_no:
        print("-------------------------------- WARNING --------------------------------\n"
              "Tailstar told me to remind you beforehand to not spam the enter button!\n"
              "He says that it will not only ruin the experience, but also screw up\n"
              "the code as you are inputting 'enter' for the upcoming inputs!\n"
              "-------------------------------------------------------------------------\n"
              "\n"
              "Now with that out of the way, let's play!")

        progressbar(i, l, prefix='Loading:', suffix='Complete', bar_length=50)
        for item in items:
            s(0.1)
            i += 1
            progressbar(i, l, prefix='Loading:', suffix='Complete', bar_length=50)
        print()
        read_warning = 1
    else:
        print("Invalid option.")
        warning = input("> ")

# --------------- MENU ---------------
while game_choice == "":
    # Introduction text
    if menu_time == 0:  # If this is the first time the user is accessing this menu
        sprint("Welcome to my Game Centre!\n", "default", "period")
        sprint("I'm Blu, ", "default", "comma")
        sprint("and I'll be joining you in the games you play in this program!\n", "default", "period")
        sprint("Here are the two games you can choose from:\n", "default", "colon")
        sprint("1) Arithmetic (Multiplication)\n", "fastest", "list")
        sprint("2) Number Guess\n", "fastest", "comma")
        sprint("So, ", "default", "comma")
        sprint("what game do you want to play?\n", "default", "input")
    else:  # If the user has already accessed this menu i.e. coming back from a game
        sprint("Looks like we're back here at the menu again! ", "default", "mark")
        sprint("What game do you want to play now?", "default", "mark")
        print("Here are the games:\n"
              "1) Arithmetic (Multiplication)\n"
              "2) Number Guess\n")

# --------------- GAME SELECTION ---------------
    game_choice = input("> ")
    while game_selected == 0:
        game_choice = game_choice.lower()
        value = randint(1, 5)
        if game_choice in game_arithmetic: # If user selected Arithmetic
            game_selected = 1
            break
        elif game_choice in game_arithmetic: # If user selected Number Guess
            game_selected = 2
            break
        elif game_choice == 'quit' or 'leave':  # If the user wants to quit
            if value == 1:
                # Why would you run this program if you weren't going to play anything...
                sprint("Why would you run this program if you weren't going to play anything...\n", "slow", "period")
            elif value == 2:
                # I tell you all these games you can play you tell me you want to leave?
                sprint("I tell you all these games you can play you tell me you want to leave?\n", "default", "mark")
            elif value == 3:
                # Tailstar created all this and you don't want to play anything?
                sprint("Tailstar created all this and you don't want to play anything?\n", "default", "mark")
            elif value == 4:
                # Didn't you like any of the games? Tell me a game you like and I'll get Tailstar to add it in!
                sprint("Didn't you like any of the games? ", "default", "mark")
                sprint("Tell me a game you like and I'll get Tailstar to add it in!\n", "default", "mark")
            elif value == 5:
                # If you want to quit... I guess I can't really stop you...
                sprint("If you want to quit... ", "default", "period")
                sprint("I guess I can't really stop you...\n", "slow", "period")
            quit()
        else:  # If the user selects a game that isn't in the list
            if value == 1:
                # Hey that's not an option!
                sprint("Hey that's not an option!\n", "default", "mark")
            elif value == 2:
                # I think you typed something wrong... There's no option for that.
                sprint("I think you typed something wrong... ", "default", "period")
                sprint("There's no option for that.\n", "default", "period")
            elif value == 3:
                # Are you purposely typing it wrong to get me to talk? If you are, it's not working!
                sprint("Are you purposely typing it wrong to get me to talk? ", "default", "mark")
                sprint("If you are, ", "default", "comma")
                sprint("it's not working!\n", "default", "mark")
            elif value == 4:
                # I don't think that option you typed is an option...
                sprint("I don't think that option you typed is an option...\n", "default", "period")
            elif value == 5:
                # Let's go and play something already! Don't choose a game that you can't play!
                sprint("Let's go and play something already! ", "default", "mark")
                sprint("Don't choose a game that you can't play!\n", "default", "mark")
            game_choice = input("> ")

# --------------- NAME ASKING ---------------
    if asked_name == 0:  # A check to see whether the user has given his/her name.
        # Oh that reminds me! I still don't know your name yet!
        # What is your name?
        sprint("Oh that reminds me! ", "faster", "mark")
        sprint("I still don't know your name yet! ", "default", "mark")
        sprint("What is your name? \n", "default", "period")
        print("Do you want to give your name? (Yes / No)")
        s(0.7)
        give_name = input("> ")
        give_name = give_name.lower()
        while given_name == 0:
            value = randint(1, 5)
            if give_name == "yes":
                if value == 1:
                    # Yay! So what is your name?
                    sprint("Yay! ", "default", "mark")
                    sprint("So what is your name?\n", "default", "mark")
                elif value == 2:
                    # You're name doesn't happen to be Tailstar, is it? If it is, then I already know you!
                    sprint("You're name doesn't happen to be Tailstar, ", "default", "comma")
                    sprint("is it? ", "default", "mark")
                    sprint("If it is ", "default", 0)
                    sprint("then I already know you!\n", "faster", "mark")
                elif value == 3:
                    # Let's see what cool name you have!
                    sprint("Let's see what cool name you have!\n", "default", "mark")
                elif value == 4:
                    # Tailstar told me to look out for people with names 'Riley' or 'Michael'.
                    # That doesn't happen to be you is it?
                    sprint("Tailstar told me to look out for people with names ", "default", "quote")
                    sprint("'Riley' or ", "default", "quote")
                    sprint("'Michael'. ", "default", "period")
                    sprint("That doesn't happen to be you is it?\n", "default", "mark")
                elif value == 5:
                    # I was going to guess your name, but that would be too hard wouldn't it?
                    sprint("I was about to guess your name, ", "default", "comma")
                    sprint("but that would be too hard wouldn't it?\n", "default", "mark")
                print("Please enter your name.")
                name = input("> ")
                name = name.lower()
                value = randint(1, 3)
                if name == "michael":  # If the name entered is Michael
                    if value == 1:
                            # Michael! You're Tailstar's friend right? Nice to meet you!
                            sprint("Michael! ", "default", "mark")
                            sprint("You're Tailstar's friend right? ", "default", "mark")
                            sprint("Nice to meet you!\n", "default", "mark")
                    elif value == 2:
                            # Your that guy who created that RPG adventure game thing right?
                            # Is it finished yet? I want to see what it's like!
                            sprint("You're that guy who created that RPG adventure game thing right? ", "default", "mark")
                            sprint("Is it finished yet? ", "default", "mark")
                            sprint("I want to see what it's like!\n", "default", "mark")
                    elif value == 3:
                            # Are you that person who plays that League of Legends game?
                            # I heard playing Teemo is bad... But that's not the point, let's start the game!
                            sprint("Aren't you the one who plays that League of Legends game? ", "default", "mark")
                            sprint("I heard playing Teemo is bad... ", "slow", "period")
                            sprint("But that's not the point, let's start the game!\n", "default", "mark")
                    name = "Michael"
                elif name == "riley":  # If the name entered is Riley
                    if value == 1:
                            # So you're Riley, the guy who plays that game called Warlight right? Nice to meet you!
                            sprint("So you're Riley, ", "default", "comma")
                            sprint("the guy who plays that game called Warlight right? ", "default", "mark")
                            sprint("Nice to meet you!\n", "default", "mark")
                    elif value == 2:
                            # AHHHHHH IT'S RILEY!!!!!! Sorry, Tailstar told me to do that if you played my game,
                            # but let's put that aside and go play!
                            sprint("AHHHHHH IT'S RILEY!!!!!! ", "fastest", "period")
                            sprint("Sorry about that, ", "slow", "comma")
                            sprint("Tailstar told me to do that if you played my game, ", "default", "comma")
                            sprint("but let's put that aside and go play!\n", "default", "mark")
                    elif value == 3:
                            # Aren't you the one that created that country guessing game?
                            # If so, nice to meet you and I hope we can be friends!
                            sprint("Aren't you the one that created that country guessing game?", "default", "mark")
                            sprint("If so, ", "default", "comma")
                            sprint("nice to meet you and I hope we can be friends!\n", "default", "mark")
                    name = "Riley"
                elif name == "tailstar":  # If the name entered is Tailstar
                    if value == 1:
                            # The game master has come! Everyone bow down to the game creator Tailstar!
                            sprint("The game master has come! ", "default", "mark")
                            sprint("Everyone bow down to the game creator Tailstar!\n", "default", "mark")
                    elif value == 2:
                            # You want me to turn you into another Pokémon?
                            # What Pokémon do you want to turn into this time?
                            sprint("You want me to turn you into another Pokémon? ", "default", "mark")
                            sprint("What Pokémon do you want to turn into this time?\n", "default", "mark")
                    elif value == 3:
                            # Has Storm beaten Remi in a Quick Attack race yet? I could put Storm in my Blu Games again!
                            sprint("Has Storm beaten Remi in a Quick Attack race yet? ", "default", "mark")
                            sprint("I could put Storm in my Blu Games again!", "default\n", "mark")
                    name = "Tailstar"
                else:
                    if value == 1:
                            # Nice to meet you NAME! I hope we can be friends!
                            sprint("Nice to meet you " + name + "! ", "default", "mark")
                            sprint("I hope we can be friends!\n", "default", "mark")
                    elif value == 2:
                            # So your name is NAME... Sounds catchy to me, I like it!
                            sprint("So your name is " + name + "...", "default", "mark")
                            sprint("Sounds catchy to me, ", "default", "comma")
                            sprint("I like it!\n", "default", "mark")
                    elif value == 3:
                            # NAME... NAME... I'll make sure to remember that... Um... NAME!
                            sprint(name + "... ", "slow", "period")
                            sprint(name + "... ", "slow", "period")
                            sprint("I'll make sure to remember that... ", "default", "period")
                            sprint("Um... ", "slow", "period")
                            sprint(name + "!\n", "default", "mark")
                    name = name.capitalize()
                given_name = 1
            elif give_name == "no":
                if value == 1:
                    # Oh... That's fine, let's continue to the game then...
                    sprint("Oh... ", "slow", "period")
                    sprint("That's fine, ", "slow", "comma")
                    sprint("let's continue to the game then...\n", "slow", "period")
                elif value == 2:
                    # I see... I did say you don't have to give it, let's go on to your game.
                    sprint("I see... ", "slow", "period")
                    sprint("I did say you don't have to give it, ", "slow", "comma")
                    sprint("let's go on to your game.\n", "slow", "period")
                elif value == 3:
                    # It would've been nice to call you by a name...
                    sprint("It would've been nice to call you by a name...\n", "slow", "period")
                elif value == 4:
                    # I guess I'm going to be still referencing you as... Well, you...
                    sprint("I guess I'm going to be still referencing you as... ", "slow", "period")
                    sprint("Well, ", "slow", "comma")
                    sprint("you...\n", "slow", "period")
                elif value == 5:
                    # So, no name? Ok then, off to the game we go...
                    sprint("So, ", "slow", "comma")
                    sprint("no name? ", "slow", "mark")
                    sprint("Ok then, ", "slow", "comma")
                    sprint("off to the game we go...\n", "slow", "period")
                given_name = 1
                break
            else:
                if value == 1:
                    # Wait... So are you giving me your name?
                    sprint("Wait... ", "default", "period")
                    sprint("So are you giving me your name?\n", "default", "mark")
                elif value == 2:
                    # I don't know what you just typed, but for all I know it isn't one of the options!
                    sprint("I don't know what you just typed, ", "default", "comma")
                    sprint("but for all I know it isn't one of the options!\n", "default", "mark")
                elif value == 3:
                    # A simple question and a simple answer...
                    # Well, maybe not the answer, but typing the answer is simple!
                    sprint("A simple question and simple answer... ", "default", "period")
                    sprint("Well, ", "default", "comma")
                    sprint("maybe not the answer, ", "default", "comma")
                    sprint("but typing the answer is simple!\n", "default", "mark")
                elif value == 4:
                    # Names... Such a strange thing... But back to the point, you didn't type one of the options!
                    sprint("Names... ", "slow", "period")
                    sprint("Such a strange thing... ", "slow", "period")
                    sprint("But back to the point, ", "default", "comma")
                    sprint("you didn't type one of the options!\n", "default", "mark")
                elif value == 5:
                    # I thought I asked a simple yes or no question... I guess it wasn't so simple?
                    sprint("I thought I asked a simple yes or no question... ", "default", "period")
                    sprint("I guess it wasn't so simple?\n", "default", "mark")
                give_name = input("> ")
    else:
        continue
    print()

# --------------- GAME SELECTOR ---------------
    value = randint(1, 5)  # Random number to determine which message to be displayed
    if game_selected == 1:  # If the user selects the game Arithmetic
        if value == 1:
                # Let's check out your maths skills!
                sprint("Let's check out your maths skills!\n", "default", "mark")
        elif value == 2:
                # 6 x 5 is 11 right? No? Maybe I should just leave the maths to Tailstar...
                sprint("6 x 5 is 11 right? ", "default", "mark")
                sprint("No? ", "default", "mark")
                sprint("Maybe I should just leave the maths to Tailstar...\n", "default", "period")
        elif value == 3:
                # Arithmetic? Sure let's go!
                sprint("Arithmetic? ", "default", "mark")
                sprint("Sure let's go!\n", "default", "mark")
        elif value == 4:
                # So you like maths I see... Let's see how good you are!
                sprint("So you like maths I see... ", "default", "period")
                sprint("Let's see how good you are!\n", "default", "mark")
        elif value == 5:
                # I, Blu, challenge you to a maths battle!
                sprint("I, ", "default", "comma")
                sprint("Blu, ", "default", "comma")
                sprint("challenge you to a maths battle!\n", "default", "mark")
        s(2)
        print("\n" * 2)
        arithmetic(name)
        game_choice = ""  # Reset gamechoice to enter back into the while loop
        menu_time = 1
    elif game_selected == 2:  # If the user selects the game Number Guess
        if value == 1:
                # Let's see if you can beat me, the legendary Blu!
                sprint("Let's see if you can beat me, ", "default", "comma")
                sprint("the legendary Blu!\n", "default", "mark")
        elif value == 2:
                # So you like number guessing, just like Tailstar!
                sprint("So you like number guessing, ", "default", "comma")
                sprint("just like Tailstar!\n", "default", "mark")
        elif value == 3:
                # Good choice! Let's begin!
                sprint("Good choice! ", "default", "mark")
                sprint("Let's begin!\n", "default", "mark")
        elif value == 4:
                # If you're planning to play easy mode, I'm going to guess that the number will be ***!
                number = str(randint(1, 1000))
                sprint("If you're planning to play easy mode, ", "default", "comma")
                sprint("I'm going to guess that the number will be" + number + "!\n", "default", "mark")
        elif value == 5:
                # I wonder if you'll beat me and Tailstar's high-scores... Let's play and see!
                sprint("I wonder if you'll beat me and Tailstar's high-scores... ", "default", "period")
                sprint("Let's play and see!", "default\n", "mark")
        s(2)
        print("\n"*2)
        numguess(name)
        game_choice = ""  # Reset game_choice to enter back into the while loop
        menu_time = 1
    s(2)
