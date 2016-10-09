<<<<<<< HEAD
from random import randint
from time import sleep as s  # All sleep functions will now be called s
from definitions import sprint

# Start - program variable outputs
start1 = ["begin", "b", "start", "s"]
start2 = ["quit", "q", "leave", "l"]
=======
# Blu's Game Centre - Blu's Adventures v1.0
# Aiyurn © 2016

'''
Bill of Player's Rights
1. Not to be killed without warning
2. Not to be given horribly unclear hints
3. To be able to win without experience of past lives
4. To be able to win without knowledge of future events
5. Not to have the game closed off without warning
6. Not to need to do unlikely things
7. Not to need to do boring things for the sake of it
8. Not to have to type exactly the right verb
9. To be allowed reasonable synonyms
10. To have a decent parser
11. To have reasonable freedom of action
12. Not to depend much on luck
13. To be able to understand a problem once it is solved
14. Not to be given too many red herrings
15. To have a good reason why something is impossible
16. Not to need to be American
17. To know how the game is getting on
'''

import time
import random

# Start - program varible outputs
start1 = ["begin","b","start","s"]
start2 = ["quit","q","leave","l"]

# Start - Begin messages
begin1 = ["Let the journey begin!",
        "You're coming? Well then what are you waiting for? Let's go!",
        "You're joining us? That makes three! Come on!",
        "Yay! Someone else who wants to come with us!",
        "We're going to have so much fun!"]

# Start - Leaving messages
quit1 = ["Aww. Tailstar really wanted you to come...",
        "I thought you'd be wanting to come...",
        "Oh... Well, you're always welcome to join when you want to!",
        "I guess I never said you had to come with us... Although I really hoped you did...",
        "But... What did I say for you to not come with us?"]

# Start - Other messages
other1 = ["I thought I said there we're only two options, 'begin' or 'quit'?",
        "I think you misspelled something...\nYou sure you typed either 'begin' or 'leave'?",
        "And here I thought Tailstar couldn't spell...\nLike I said, do you want to 'begin' or 'leave'?",
        "I don't think I said anything else other than 'begin' or 'quit'?",
        "Come on! Let's go already! Do you want to 'begin' or 'quit'?"]

# Chapter select - Blu's messages
blu1 = ["The journey finally begins! Let's go!",
        "You have no problems with starting do you? No? Ok, let's go!",
        "Now with that all over, let's start!",
        "I wonder how this story will go...",
        "Hm... I've run out of things to say!"]
>>>>>>> 4827ce23c4623b26f9242f8a422e7d85ccaa9a42

blu2 = []
blu3 = []

<<<<<<< HEAD
=======
# Chapter select - Locked chapters
locked1 = ["Tailstar locked these chapters for a reason...",
           "Don't you ever wonder why there is 'LOCKED' on the chapter?",
           "Ok, this time try choosing something that isn't locked.",
           "I can't start that chapter if it's locked!",
           "Maybe finish the unlocked chapters first before going on to the locked ones..."]

# Chapter select - Other chapters
other2 = ["There are only three chapters you know... '01', '02', and '03'.",
          "I feel like I'm talking to myself here! Well, maybe I am, but there's only three chapters to choose from!",
          "I think you just typed a non-existent chapter... There are only three chapters.",
          "Are you purposely typing the wrong characters just to get me to talk? If so it isn't working!",
          "I have this odd feeling that you might secretly be Tailstar... Or is that just me?"]

>>>>>>> 4827ce23c4623b26f9242f8a422e7d85ccaa9a42
# Chapter select - Total chapters
chapter = ["01", "1", "02", "2", "03", "3"]
locked = ["02", "2", "03", "3"]

<<<<<<< HEAD

def islocked():  # A function that checks whether the selected chapter is locked
=======
def islocked():
>>>>>>> 4827ce23c4623b26f9242f8a422e7d85ccaa9a42
    if chapsel in locked:
        return True
    else:
        return False

<<<<<<< HEAD

# Introduction text
sprint("Welcome to Blu's Adventure!\n", "default", 1.2)
sprint("Come on Tailstar we have a person who wants to join us!\n", "default", "mark")
sprint("To join me in my adventure, ", "default", "comma")
sprint("type ", "default", "quote")
sprint("'begin'! ", "default", "mark")
sprint("To go back to the menu, ", "default", "comma")
sprint("type ", "default", "quote")
sprint("'quit'.\n", "default", "input")

# Start
program = input("> ")
while True:
    value = randint(1, 5)  # Random number generator to select one of the messages
    if program in start1:
        if value == 1:
            # Let the journey begin!
            sprint("Let the journey begin!\n", "default", "mark")
        elif value == 2:
            # You're coming? Well then what are you waiting for? Let's go!
            sprint("You're coming? ", "default", "mark")
            sprint("Well then what are you waiting for? ", "default", "puncutation")
            sprint("Let's go!\n", "default", "mark")
        elif value == 3:
            # So you're joining me and Tailstar? That makes three! Come on let's go!
            sprint("So you're joining me and Tailstar? ", "default", "mark")
            sprint("That makes three! ", "default", "mark")
            sprint("Come on let's go!\n", "default", "mark")
        elif value == 4:
            # Yay! Someone else who wants to come with me!
            sprint("Yay! ", "default", "mark")
            sprint("Someone else who wants to come with me!\n", "default", "mark")
        elif value == 5:
            # We're going to have so much fun in this adventure!
            sprint("We're going to have so much fun in this adventure!\n", "default", "mark")
        s(1)
        print("\n" * 2)
        break
    elif program in start2:
        if value == 1:
            # Aww... I really wanted you to come...
            sprint("Aww... ", "slower", "period")
            sprint("I really wanted you to come...\n", "slower", "period")
        elif value == 2:
            # I thought you liked adventures... That's why you chose this game right?
            sprint("I thought you liked adventures... ", "slower", "period")
            sprint("That's why you chose this game right?\n", "slower", "mark")
        elif value == 3:
            # Oh... Well, you're always welcome to come back when you want to!
            sprint("Oh... ", "slower", "period")
            sprint("Well, ", "slower", "comma")
            sprint("you're always welcome to come back when you want to!\n", "slower", "mark")
        elif value == 4:
            # I guess I never said you had to come with us... Although I really hoped you did...
            sprint("I guess I never said you had to come with us... ", "slower", "period")
            sprint("Although I really hoped you did...\n", "slower", "period")
        elif value == 5:
            # But... What did I say for you to come with me?
            sprint("But... ", "slower", "period")
            sprint("What did I say for you to not come with me?\n", "slower", "mark")
        s(1)
        quit()
    else:
        if value == 1:
            # I thought I said there we're only two options, 'begin' or 'quit'?
            sprint("I thought I said there we're only two options, ", "default", "comma")
            sprint("'begin' or ", "default", "quote")
            sprint("'quit'?\n", "default", "input")
        elif value == 2:
            # I think you mistyped something... You sure you typed either 'begin' or 'leave'?
            sprint("I think you mistyped something... ", "default", "period")
            sprint("You sure you typed either ", "default", "quote")
            sprint("'begin' or ", "default", "quote")
            sprint("'leave'?\n", "default", "input")
        elif value == 3:
            # And here I thought Tailstar couldn't spell... Like I said, do you want to 'begin' or 'leave'?
            sprint("And here I thought Tailstar couldn't spell... ", "default", "period")
            sprint("Like I said, ", "default", "comma")
            sprint("do you want to ", "default", "quote")
            sprint("'begin' or ", "default", "quote")
            sprint("'leave'?\n", "default", "input")
        elif value == 4:
            # I don't think I said anything else other than 'begin' or 'quit'?
            sprint("I don't think I said anything else other than ", "default", "quote")
            sprint("'begin' or ", "default", "quote")
            sprint("'quit'?\n", "default", "input")
        elif value == 5:
            # Come on! Let's go already! Do you want to 'begin' or 'quit'?
            sprint("Come on! ", "faster", "mark")
            sprint("Let's go already! ", "faster", "mark")
            sprint("Do you want to ", "default", "quote")
            sprint("'begin' or ", "default", "quote")
            sprint("'quit'?\n", "default", "input")
        program = input("> ")

# Chapter Select
print("Chapter Select:\n",
      "'01' - The Tale of Blu\n",
      "'02' - The Adventure Begins! [LOCKED]\n",
      "'03' - Finding your first Pokémon [LOCKED]")

chapsel = input("> ")
while True:
    value = randint(1, 5)
    if chapsel in chapter:
        if islocked():
            if value == 1:
                # Hey don't go on ahead! See what happens before first!
                sprint("Hey don't go on ahead! ", "default", "mark")
                sprint("See what happens before first!\n", "default", "input")
            elif value == 2:
                # Don't you ever wonder why there is 'LOCKED' on the chapter?
                sprint("Don't you ever wonder why there is ", "default", "quote")
                sprint("'LOCKED' on the chapter?\n", "default", "input")
            elif value == 3:
                # Ok, this time try choosing something that isn't locked.
                sprint("Ok, ", "default", "comma")
                sprint("this time try choosing something that isn't locked.\n", "default", "input")
            elif value == 4:
                # I can't start that chapter if it's locked!
                sprint("I can't start that chapter if it's locked!\n", "default", "input")
            elif value == 5:
                sprint("I'm pretty sure Tailstar locked these chapters for a reason...\n", "default", "input")
            chapsel = input("> ")

        else:
            if value == 1:
                sprint("The journey finally begins! ", "default", "mark")
                sprint("Let's go!\n", "default", "mark")
            elif value == 2:
                sprint("You have no problems with starting do you? ", "default", "mark")
                sprint("No? ", "default", "mark")
                sprint("Ok, ", "default", "comma")
                sprint("let's go!\n", "default", "mark")
            elif value == 3:
                sprint("Now with that all over, ", "default", "comma")
                sprint("let's start!\n", "default", "mark")
            elif value == 4:
                sprint("I wonder how this story will go...\n", "default", "period")
            elif value == 5:
                sprint("Hm... ", "default", "period")
                sprint("I've run out of things to say!", "default", "mark")
            s(2)
            print("\n" * 10)
            break

    else:
        if value == 1:
            sprint("There are only three chapters you know... ", "default", "period")
            sprint("'01', ", "default", "comma")
            sprint("'02', ", "default", "comma")
            sprint("and '03'.\n", "default", "input")
        elif value == 2:
            sprint("I feel like I'm talking to myself here! ", "default", "mark")
            sprint("Well, ", "default", "comma")
            sprint("maybe I am, ", "default", "comma")
            sprint("but there's only three chapters to choose from!\n", "default", "input")
        elif value == 3:
            sprint("I think you just typed a non-existent chapter... ", "default", "period")
            sprint("There are only three chapters.\n", "default", "input")
        elif value == 4:
            sprint("Are you purposely typing the wrong characters just to get me to talk? ", "default", "mark")
            sprint("If you are it isn't working!\n", "default", "input")
        elif value == 5:
            sprint("I have this odd feeling that you might secretly be Tailstar... ", "default", "period")
            sprint("Or is that just me?\n", "default", "input")
        chapsel = input("> ")

# Chapter 01 - The Tale of Blu
=======
def bluadventure():
    # Introduction text
    print("Welcome to Blu's Adventure!\n"
          "Come on Tailstar we have a person who wants to join us!\n"
          "To join me in my adventure, type 'begin'! To leave, type 'quit'")

    # Start
    program = input("> ")
    while True:
        if program in start1:
            print(random.choice(begin1))
            time.sleep(2)
            print("\n"*2)
            break
        elif program in start2:
            print(random.choice(quit1))
            time.sleep(2)
            quit()
        else:
            print(random.choice(other1))
            program = input("> ")

    # Chapter Select
    print("Chapter Select:\n",
          "'01' - The Tale of Blu\n",
          "'02' - The Adventure Begins! [LOCKED]\n",
          "'03' - Finding your first Pokémon [LOCKED]")

    chapsel = input("> ")
    while True:
        if chapsel in chapter:
            if islocked():
                print(random.choice(locked1))
                chapsel = input("> ")
            else:
                print(random.choice(blu1))
                time.sleep(2)
                print("\n"*10)
                break
        else:
            print(random.choice(other2))
            chapsel = input("> ")

    # Chapter 01 - The Tale of Blu
>>>>>>> 4827ce23c4623b26f9242f8a422e7d85ccaa9a42
