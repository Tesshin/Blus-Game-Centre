# -*- coding: utf-8 -*-
# Blu's Game Centre v1.0
# Aiyurn © 2016

# http://stackoverflow.com/questions/4099422/printing-slowly-simulate-typing
# http://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console

import sys
from random import randint
from time import sleep as s
from games import arithmetic, numguess


def sprint(text, speed, delay):  # Print out text with a custom speed
    # TODO Add a few more sprint speeds
    for c in text:
        print(c, end=""),
        sys.stdout.flush()
        if speed == "default":  # Normal printing speed
            s(0.035)
        if speed == "slow":  # Slow printing speed
            s(0.05)
        if speed == "slower":  # Slower printing speed
            s(0.06)
        if speed == "fastest":  # Fastest printing speed
            s(0.02)
        if speed == "faster":  # Faster printing speed
            s(0.03)
    if delay == "comma":  # If the last punctuation is a comma (,)
        s(0.45)
    elif delay == "period":  # If the last punctuation is a period (.)
        s(1)
    elif delay == "quote":  # If the last punctuation is quotes ("")
        s(0.1)
    elif delay == "colon":  # If the last punctuation is a colon (:)
        s(0.3)
    elif delay == "list":  # If the last punctuation is a list of something
        s(0.05)
    elif delay == "mark":  # If the last punctuation is a punctuation mark (! ?)
        s(0.5)
    elif delay == "input":  # If the next code asks for an input
        s(0.05)


def progressbar(iteration, total, prefix='', suffix='', decimals=1, barlength=100):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        barLength   - Optional  : character length of bar (Int)
    """
    formatstr = "{0:." + str(decimals) + "f}"
    percents = formatstr.format(100 * (iteration / float(total)))
    filledlength = int(round(barlength * iteration / float(total)))
    bar = '█' * filledlength + '-' * (barlength - filledlength)
    sys.stdout.write('\r%s |%s| %s%s %s' % (prefix, bar, percents, '%', suffix)),
    if iteration == total:
        sys.stdout.write('\n')
    sys.stdout.flush()

# TODO Remove useless lines from usage
'''
#
# Sample Usage
#

from time import sleep

# make a list
items = list(range(0, 100))
i = 0
l = len(items)

# Initial call to print 0% progress
progressbar(i, l, prefix='Progress:', suffix='Complete', barLength=50)
for item in items:
    # Do stuff...
    sleep(0.1)
    # Update Progress Bar
    i += 1
    progressBar(i, l, prefix='Progress:', suffix='Complete', barLength=50)
'''


# Introduction - Variables
game_choice = ""
menu_time = 0  # TODO Fix up some menutime issues
give_name = ""
asked_name = 0

# Start - Game Choice input options
game_arithmetic = ["1", "a", "arithmetic"]
game_numguess = ["2", "n", "number guess"]
game_cyoa = ["3", "c", "cyoa", "choose your own adventure"]

# --------------- CODE BEGINS HERE ---------------

print("Blu's Game Centre v1.0")
print("Aiyurn (C) 2016\n")
s(1)
print("-------------------------------- WARNING --------------------------------\n"
      "Tailstar told me to remind you beforehand to not spam the enter button!\n"
      "He says that it will not only ruin the experience, but also screw up\n"
      "the code as you are inputting 'enter' for the upcoming inputs!\n"
      "-------------------------------------------------------------------------\n"
      "\n"
      "Now with that out of the way, let's play!")
items = list(range(0, 110))
i = 0
l = len(items)
progressbar(i, l, prefix='Loading:', suffix='Complete', barlength=50)
for item in items:
    s(0.1)
    i += 1
    progressbar(i, l, prefix='Loading:', suffix='Complete', barlength=50)
print()

while game_choice == "":
    # Introduction text
    if menu_time == 0:  # If this is the first time the user is accessing this menu
        sprint("Welcome to my Game Centre!\n", "default", "period")
        sprint("I'm Blu, ", "default", "comma")
        sprint("and I'll be joining you in the games you play in this program!\n", "default", "period")
        sprint("Here are the games you can choose from:\n", "default", "colon")
        sprint("1) Arithmetic (Multiplication)\n", "fastest", "list")
        sprint("2) Number Guess\n", "fastest", "list")
        sprint("So, ", "default", "comma")
        sprint("what game do you want to play?\n", "default", "input")
    else:  # If the user has already accessed this menu i.e. coming back from a game
        print("And we're back at the menu again! What game do you want to play now?")
        print("Here are the games:\n"
              "1) Arithmetic (Multiplication)\n"
              "2) Number Guess\n")
    game_choice = input("> ")

    if asked_name == 0:  # A check to see whether the user has given his/her name.
        # Oh that reminds me! I still don't know your name yet!
        # Do you want to tell me your name? You don't have to, but it would be nice if you did!
        sprint("Oh that reminds me! ", "faster", "mark")
        sprint("I still don't know your name yet! ", "default", "mark")
        sprint("You don't have to tell me your name, ", "slow", "comma")
        sprint("but it would be nice if you did!\n", "faster", "period")
        print("Do you want to give your name? (Yes / No)")
        s(0.7)
        give_name = input("> ")
        give_name = give_name.lower()
        while True:
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
                while True:
                    value = randint(1, 3)
                    if name == "michael":  # If the name entered is Michael
                        if value == 1:
                            # Michael! You're Tailstar's friend right? Nice to meet you!
                            sprint("Michael! ", "default", "mark")
                            sprint("You're Tailstar's friend right? ", "default", "mark")
                            sprint("Nice to meet you!\n", "default", "mark")
                        elif value == 2:
                            # Your that guy who created that RPG adventure game thing right? Nice to meet you!
                            sprint("Your that guy who created that RPG adventure game thing right? ", "default", "mark")
                            sprint("Nice to meet you!", "default", "mark")
                        elif value == 3:
                            # Are you that person who plays that League of Legends game? Nice to meet you!
                            sprint("Are you that person who plays that League of Legends game?", "default", "mark")
                            sprint("Nice to meet you!", "default", "mark")
                        name = "Michael"
                        break
                    elif name == "riley":  # If the name entered is Riley
                        if value == 1:
                            # So you're Riley, the guy who plays that game called Warlight right? Nice to meet you!
                            sprint("So you're Riley, ", "default", "comma")
                            sprint("the guy who plays that game called Warlight right? ", "default", "mark")
                            sprint("Nice to meet you!", "default", "mark")
                        elif value == 2:
                            # AHHH IT'S RILEY!!! Sorry, Tailstar told me to do that if you played my game, but let's
                            # put that aside and let's go play!
                            sprint("AHHH IT'S RILEY!!! ", "default", "comma")
                            sprint("Sorry, ", "slow", "comma")
                            sprint("Tailstar told me to do that if you played my game, ", "slow", "comma")
                            sprint("but let's put that aside and let's go play!", "default", "mark")
                        elif value == 3:
                            # Aren't you the one that created that country guessing game that Tailstar is
                            # adding into my game centre? If so, nice to meet you and I hope we can be friends!
                            sprint("Aren't you the one that created that country guessing game?", "default", "mark")
                            sprint("If so, ", "default", "comma")
                            sprint("nice to meet you and I hope we can be friends!", "default", "mark")
                        name = "Riley"
                        break
                    elif name == "tailstar":  # If the name entered is Tailstar
                        if value == 1:
                            # Are you actually Tailstar? Wait, I shouldn't be talking like that to you! Sorry!
                            sprint("Are you actually Tailstar? ", "default", "mark")
                            sprint("Wait, ", "default", "comma")
                            sprint("I shouldn't be talking like that to you! ", "faster", "mark")
                            sprint("Sorry!", "faster", "mark")
                        elif value == 2:
                            # You want me to turn you into another Pokémon?
                            # What Pokémon do you want to turn into this time?
                            sprint("You want me to turn you into another Pokémon? ", "default", "mark")
                            sprint("What Pokémon do you want to turn into this time?", "default", "mark")
                        elif value == 3:
                            # Has Storm beaten Remi in a Quick Attack race yet? I could put Storm in my Blu Games again!
                            sprint("Has Storm beaten Remi in a Quick Attack race yet? ", "default", "mark")
                            sprint("I could put Storm in my Blu Games again!", "default", "mark")
                        name = "Tailstar"
                        break
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
                        break

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
                    sprint("I guess it wasn't so simple?", "default", "mark")
                give_name = input("> ")
    else:
        continue

    while True:
        value = randint(1, 5)  # Random number to determine which message to be displayed
        if game_choice in game_arithmetic:  # If the user selects the game Arithmetic
            if value == 1:
                # Let's check out your maths skills!
                sprint("Let's check out your maths skills!", "default", "mark")
            elif value == 2:
                # 6 x 5 is 11 right? No? Maybe I should just leave the maths to Tailstar...
                sprint("6 x 5 is 11 right?", "default", "mark")
                sprint("No? ", "default", "mark")
                sprint("Maybe I should just leave the maths to Tailstar...", "default", "period")
            elif value == 3:
                # Arithmetic? Sure let's go!
                sprint("Arithmetic? ", "default", "mark")
                sprint("Sure let's go!", "default", "mark")
            elif value == 4:
                # So you like maths I see... Let's see how good you are!
                sprint("So you like maths I see... ", "default", "period")
                sprint("Let's see how good you are!", "default", "mark")
            elif value == 5:
                # I, Blu, challenge you to a maths battle!
                sprint("I, ", "default", "comma")
                sprint("Blu, ", "default", "comma")
                sprint("challenge you to a maths battle!", "default", "mark")
            s(2)
            print("\n" * 2)
            arithmetic()
            game_choice = ""  # Reset gamechoice to enter back into the while loop
            menu_time = 1
            break
        elif game_choice in game_numguess:  # If the user selects the game Number Guess
            if value == 1:
                # Let's see if you can beat me, the legendary Blu!
                sprint("Let's see if you can beat me, ", "default", "comma")
                sprint("the legendary Blu!", "default", "mark")
            elif value == 2:
                # So you like number guessing, just like Tailstar!
                sprint("So you like number guessing, ", "default", "comma")
                sprint("just like Tailstar!", "default", "mark")
            elif value == 3:
                # Good choice! Let's begin!
                sprint("Good choice! ", "default", "mark")
                sprint("Let's begin!", "default", "mark")
            elif value == 4:
                # If you're planning to play easy mode, I'm going to guess that the number will be ***!
                number = str(randint(1, 1000))
                sprint("If you're planning to play easy mode, ", "default", "comma")
                sprint("I'm going to guess that the number will be" + number + "!", "default", "mark")
            elif value == 5:
                # I wonder if you'll beat me and Tailstar's high-scores... Let's play and see!
                sprint("I wonder if you'll beat me and Tailstar's high-scores... ", "default", "period")
                sprint("Let's play and see!", "default", "mark")
            s(2)
            print("\n"*2)
            numguess()
            game_choice = ""  # Reset gamechoice to enter back into the while loop
            menu_time = 1
            break

        elif game_choice == 'quit':  # If the user wants to quit
            if value == 1:
                # Why would you run this program if you weren't going to play anything...
                sprint("Why would you run this program if you weren't going to play anything...", "slow", "period")
            elif value == 2:
                # I tell you all these games you can play you tell me you want to leave?
                sprint("I tell you all these games you can play you tell me you want to leave?", "default", "mark")
            elif value == 3:
                # Tailstar created all this and you don't want to play anything?
                sprint("Tailstar created all this and you don't want to play anything?", "default", "mark")
            elif value == 4:
                # Didn't you like any of the games? Tell me a game you like and I'll get Tailstar to add it in!
                sprint("Didn't you like any of the games? ", "default", "mark")
                sprint("Tell me a game you like and I'll get Tailstar to add it in!", "default", "mark")
            elif value == 5:
                # If you want to quit... I guess I can't really stop you...
                sprint("If you want to quit... ", "default", "period")
                sprint("I guess I can't really stop you...", "slow", "period")
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

    s(2)
