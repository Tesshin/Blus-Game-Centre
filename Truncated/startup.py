# -*- coding: utf-8 -*-
# Blu's Game Centre v1.0
#     _____        _    _                          ____   ___  _  __
#    / ___ \      / \  (_)_   _ _   _ _ __ _ __   |___ \ / _ \/ |/ /_
#   / / __| \    / _ \ | | | | | | | | '__| '_ \    __) | | | | | '_ \
#  | | (__   |  / ___ \| | |_| | |_| | |  | | | |  / __/| |_| | | (_) |
#   \ \___| /  /_/   \_\_|\__, |\__,_|_|  |_| |_| |_____|\___/|_|\___/
#    \_____/              |___/



# http://stackoverflow.com/questions/4099422/printing-slowly-simulate-typing
# http://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console

# All value variables are used for determining which message to display.

# --------------- IMPORTS ---------------
import sys
from random import randint
from time import sleep as s
from games import arithmetic
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

# ---------------------------------- CODE BEGINS HERE ----------------------------------

# LOGOS
print("Blu's Game Centre v1.0")
print("Aiyurn (C) 2016\n")
s(1)

# WARNING PROMPT
print("Have you read the warning before? (Yes / No)")
warning = input("> ")
# WARNING PROMPT VARIABLES
warning_yes = ["y", "ye", "yes"]
warning_no = ["n", "no"]
read_warning = 0

while read_warning == 0:  # While the user hasn't seen the warning.
    warning = warning.lower()
    if warning in warning_yes:  # If the user answered yes for reading the warning.
        print("Welcome back!")
        s(1)
        print()
        read_warning = 1
    elif warning in warning_no:  # If the user answered no for reading the warning.
        # PROGRESS BAR VARIABLES
        items = list(range(0, 110))
        i = 0
        l = len(items)

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
    else:  # If the user answered an option that isn't yes or no.
        print("Invalid option.")
        warning = input("> ")

# VARIABLES
game_choice = ""
menu_time = 0
asked_name = 0
game_selected = 0
given_name = 0
give_name = ""
game_arithmetic = ["1", "a", "arithmetic"]

# INTRODUCTION
while game_choice != "end":  # While the user hasn't selected a game.
    if menu_time == 0:  # If this is the first time the user is accessing this menu
        # Welcome to my Game Centre!
        # I'm Blu, and I'll be joining you in the games you play in this program!
        # Here are the games you can choose from:
        # 1) Arithmetic (Multiplication)
        # So, what game do you want to play?
        sprint("Welcome to my Game Centre!\n", "default", "period")
        sprint("I'm Blu, ", "default", "comma")
        sprint("and I'll be joining you in the games you play in this program!\n", "default", "period")
        sprint("Here are the games you can choose from:\n", "default", "colon")
        sprint("1) Arithmetic (Multiplication)\n", "fastest", "comma")
        sprint("So, ", "default", "comma")
        sprint("what game do you want to play?\n", "default", "input")
    else:  # If the user has already accessed this menu i.e. coming back from a game
        # Looks like we're back here at the menu again! What game do you want to play now?
        # Here are the games:
        # 1) Arithmetic (Multiplication)
        sprint("Looks like we're back here at the menu again! ", "default", "mark")
        sprint("What game do you want to play now?\n", "default", "mark")
        sprint("Here are the games:\n", "default", "colon")
        sprint("1) Arithmetic (Multiplication)\n", "fastest", "input")

    # GAME SELECTION
    game_choice = input("> ")
    while game_selected == 0:  # While user hasn't selected a game
        game_choice = game_choice.lower()
        value = randint(1, 5)
        if game_choice in game_arithmetic:  # If user selected Arithmetic
            game_selected = 1
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
                # Let's go play something already! Don't choose a game that you can't play!
                sprint("Let's go play something already! ", "default", "mark")
                sprint("Don't choose a game that you can't play!\n", "default", "mark")
            game_choice = input("> ")

    # NAME ASKING
    if asked_name == 0:  # If the program hasn't asked user for their name.
        # Oh that reminds me! I still don't know your name yet!
        sprint("Oh that reminds me! ", "faster", "mark")
        sprint("I still don't know your name yet!\n", "default", "mark")
        print("Do you want to give your name? (Yes / No)")
        give_name = input("> ")
        give_name = give_name.lower()
        while given_name == 0:  # While user hasn't given name.
            value = randint(1, 5)
            if give_name == "yes":  # If the user agrees to give their name.
                if value == 1:
                    # Yay! So what is your name?
                    sprint("Yay! ", "default", "mark")
                    sprint("So what is your name?\n", "default", "mark")
                elif value == 2:
                    # You're name doesn't happen to be Tailstar, is it?
                    sprint("You're name doesn't happen to be Tailstar, ", "default", "comma")
                    sprint("is it?\n", "default", "mark")
                elif value == 3:
                    # Let's see what cool name you have!
                    sprint("Let's see what cool name you have!\n", "default", "mark")
                elif value == 4:
                    # Tailstar told me to look out for people with names 'Riley' or 'Michael'...
                    sprint("Tailstar told me to look out for people with names ", "default", "quote")
                    sprint("'Riley' or ", "default", "quote")
                    sprint("'Michael'...\n", "default", "period")
                elif value == 5:
                    # I was going to guess your name, but that would be too hard wouldn't it?
                    sprint("I was about to guess your name, ", "default", "comma")
                    sprint("but that would be too hard wouldn't it?\n", "default", "mark")
                print("Please enter your name.")
                username = input("> ")
                username = username.lower()
                value = randint(1, 3)
                if username == "michael":  # If the name entered is Michael.
                    if value == 1:
                            # Hey there Michael! You're Tailstar's friend right? Nice to meet you!
                            sprint("Hey there Michael! ", "default", "mark")
                            sprint("You're Tailstar's friend right? ", "default", "mark")
                            sprint("Nice to meet you!\n", "default", "mark")
                    elif value == 2:
                            # Your that guy who created that RPG adventure game right?
                            # Is it finished yet?
                            sprint("You're that guy who created that RPG adventure game right? ", "default", "mark")
                            sprint("Is it finished yet?\n", "default", "mark")
                    elif value == 3:
                            # Aren't you the one who plays that League of Legends game?
                            # I heard playing Teemo is bad... But that's not the point, let's go play!
                            sprint("Aren't you the one who plays that League of Legends game? ", "default", "mark")
                            sprint("I heard playing Teemo is bad... ", "slow", "period")
                            sprint("But that's not the point, let's go play!\n", "default", "mark")
                    username = "Michael"
                elif username == "riley":  # If the name entered is Riley.
                    if value == 1:
                            # So you're Riley, the guy who plays that game called Warlight right? Nice to meet you!
                            sprint("So you're Riley, ", "default", "comma")
                            sprint("the guy who plays that game called Warlight right? ", "default", "mark")
                            sprint("Nice to meet you!\n", "default", "mark")
                    elif value == 2:
                            # AHHHHHH IT'S RILEY!!!!!! Sorry, Tailstar told me to do that if you played my game,
                            # but let's put that aside and go play!
                            sprint("AHHHHHH IT'S RILEY!!!!!! ", "fastest", "period")
                            sprint("Sorry, ", "default", "comma")
                            sprint("Tailstar told me to do that if you played my game, ", "default", "comma")
                            sprint("but let's put that aside and go play!\n", "default", "mark")
                    elif value == 3:
                            # Aren't you the one that created that country guessing game?
                            # If you are, I hope we can be friends!
                            sprint("Aren't you the one that created that country guessing game? ", "default", "mark")
                            sprint("If you are, ", "default", "comma")
                            sprint("I hope we can be friends!\n", "default", "mark")
                    username = "Riley"
                elif username == "tailstar":  # If the name entered is Tailstar.
                    if value == 1:
                            # The game master has come! I bow down to you Tailstar!
                            sprint("The game master has come! ", "default", "mark")
                            sprint("I bow down to you Tailstar!\n", "default", "mark")
                    elif value == 2:
                            # Have you come to be to turn into another Pokémon?
                            # Let's wait until we've finished the game ok?
                            sprint("Have you come to me to turn into another Pokémon? ", "default", "mark")
                            sprint("Let's wait until we've finished the game ok?\n", "default", "mark")
                    elif value == 3:
                            # Oh yes Tailstar! Has Storm beaten Remi in a race yet?
                            sprint("Oh yes Tailstar!", "default", "mark")
                            sprint("Has Storm beaten Remi in a race yet?\n", "default", "mark")
                    username = "Tailstar"
                else:
                    if value == 1:
                            # Nice to meet you NAME! I hope we can be friends!
                            sprint("Nice to meet you " + username + "! ", "default", "mark")
                            sprint("I hope we can be friends!\n", "default", "mark")
                    elif value == 2:
                            # So your name is NAME... Sounds catchy to me, I like it!
                            sprint("So your name is " + username + "...", "default", "mark")
                            sprint("Sounds catchy to me, ", "default", "comma")
                            sprint("I like it!\n", "default", "mark")
                    elif value == 3:
                            # NAME... NAME... I'll make sure to remember that... Um... Oh yea NAME!
                            sprint(username + "... ", "slow", "period")
                            sprint(username + "... ", "slow", "period")
                            sprint("I'll make sure to remember that... ", "default", "period")
                            sprint("Um... ", "slow", "period")
                            sprint("Oh yea " + username + "!\n", "default", "mark")
                    username = username.capitalize()
                given_name = 1
                asked_name = 1
            elif give_name == "no":  # If the user rejects to give their name.
                if value == 1:
                    # Oh... That's fine, I guess I'll call you User for the time being...
                    sprint("Oh... ", "slow", "period")
                    sprint("That's fine, ", "slow", "comma")
                    sprint("I guess I'll call you User for the time being...\n", "slow", "period")
                elif value == 2:
                    # I did say you don't have to give it, let's go on to the game then.
                    sprint("I did say you don't have to give it, ", "slow", "comma")
                    sprint("let's go on to the game then.\n", "slow", "period")
                elif value == 3:
                    # It would've been nice to call you by a name, right now you're just User...
                    sprint("It would've been nice to call you by a name, ", "slow", "period")
                    sprint("right now you're just User...\n", "slow", "period")
                elif value == 4:
                    # I guess I'm going to be referencing you as... Well, User...
                    sprint("I guess I'm going to be referencing you as... ", "slow", "period")
                    sprint("Well, ", "slow", "comma")
                    sprint("User...\n", "slow", "period")
                elif value == 5:
                    # So, no name? Ok then, off to the game we go...
                    sprint("So, ", "slow", "comma")
                    sprint("no name? ", "slow", "mark")
                    sprint("Ok then, ", "slow", "comma")
                    sprint("off to the game we go...\n", "slow", "period")
                given_name = 1
                asked_name = 1
                username = "User"
            else:
                if value == 1:
                    # So... Are you giving me your name?
                    sprint("So... ", "default", "period")
                    sprint("Are you giving me your name?\n", "default", "mark")
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
    else:  # If the program has already asked for the user's name.
        continue
    print()

    # GAME SELECTOR
    value = randint(1, 5)
    if game_selected == 1:  # If the user selects the game Arithmetic
        if value == 1:
                # Let's check out your maths skills NAME!
                sprint("Let's go check out your maths skills " + username + "!\n", "default", "mark")
        elif value == 2:
                # 6 x 5 is 11 right? No? Maybe I should just leave the maths to Tailstar...
                sprint("6 x 5 is 11 right? ", "default", "mark")
                sprint("No? ", "default", "mark")
                sprint("Maybe I should just leave the maths to Tailstar...\n", "default", "period")
        elif value == 3:
                # So you've chosen Arithmetic... Sure let's go!
                sprint("So you've chosen Arithmetic... ", "default", "period")
                sprint("Sure let's go!\n", "default", "mark")
        elif value == 4:
                # So you like maths NAME? Let's check how good you are!
                sprint("So you like maths " + username + "? ", "default", "period")
                sprint("Let's check how good you are!\n", "default", "mark")
        elif value == 5:
                # I, Blu, challenge you to a maths battle!
                sprint("I, ", "default", "comma")
                sprint("Blu, ", "default", "comma")
                sprint("challenge you to a maths battle!\n", "default", "mark")
        print("\n" * 2)
        play = arithmetic(username)  # Play is whether the user wants to go back to the menu or end the program.
        if play == "yes":  # If the user wanted to go back to the menu
            game_choice = ""
            menu_time = 1
            game_selected = 0
        elif play == "no":  # If the user wanted to end the program
            game_choice = "end"
