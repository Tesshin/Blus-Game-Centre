from random import randint
from time import sleep as s  # All sleep functions will now be called s
from definitions import sprint

# Start - program variable outputs
start1 = ["begin", "b", "start", "s"]
start2 = ["quit", "q", "leave", "l"]

# Chapter select - Total chapters
chapter = ["01", "1", "02", "2", "03", "3"]
locked = ["02", "2", "03", "3"]


def islocked():  # A function that checks whether the selected chapter is locked
    if chapsel in locked:
        return True
    else:
        return False

# Introduction text
sprint("Welcome to Blu's Adventure!\n", "normal", 1.2)
sprint("Come on Tailstar we have a person who wants to join us!\n", "normal", "mark")
sprint("To join me in my adventure, ", "normal", "comma")
sprint("type ", "normal", "quote")
sprint("'begin'! ", "normal", "mark")
sprint("To go back to the menu, ", "normal", "comma")
sprint("type ", "normal", "quote")
sprint("'quit'.\n", "normal", "input")

# Start
program = input("> ")
while True:
    value = randint(1, 5)  # Random number generator to select one of the messages
    if program in start1:
        if value == 1:
            # Let the journey begin!
            sprint("Let the journey begin!\n", "normal", "mark")
        elif value == 2:
            # You're coming? Well then what are you waiting for? Let's go!
            sprint("You're coming? ", "normal", "mark")
            sprint("Well then what are you waiting for? ", "normal", "puncutation")
            sprint("Let's go!\n", "normal", "mark")
        elif value == 3:
            # So you're joining me and Tailstar? That makes three! Come on let's go!
            sprint("So you're joining me and Tailstar? ", "normal", "mark")
            sprint("That makes three! ", "normal", "mark")
            sprint("Come on let's go!\n", "normal", "mark")
        elif value == 4:
            # Yay! Someone else who wants to come with me!
            sprint("Yay! ", "normal", "mark")
            sprint("Someone else who wants to come with me!\n", "normal", "mark")
        elif value == 5:
            # We're going to have so much fun in this adventure!
            sprint("We're going to have so much fun in this adventure!\n", "normal", "mark")
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
            sprint("I thought I said there we're only two options, ", "normal", "comma")
            sprint("'begin' or ", "normal", "quote")
            sprint("'quit'?\n", "normal", "input")
        elif value == 2:
            # I think you mistyped something... You sure you typed either 'begin' or 'leave'?
            sprint("I think you mistyped something... ", "normal", "period")
            sprint("You sure you typed either ", "normal", "quote")
            sprint("'begin' or ", "normal", "quote")
            sprint("'leave'?\n", "normal", "input")
        elif value == 3:
            # And here I thought Tailstar couldn't spell... Like I said, do you want to 'begin' or 'leave'?
            sprint("And here I thought Tailstar couldn't spell... ", "normal", "period")
            sprint("Like I said, ", "normal", "comma")
            sprint("do you want to ", "normal", "quote")
            sprint("'begin' or ", "normal", "quote")
            sprint("'leave'?\n", "normal", "input")
        elif value == 4:
            # I don't think I said anything else other than 'begin' or 'quit'?
            sprint("I don't think I said anything else other than ", "normal", "quote")
            sprint("'begin' or ", "normal", "quote")
            sprint("'quit'?\n", "normal", "input")
        elif value == 5:
            # Come on! Let's go already! Do you want to 'begin' or 'quit'?
            sprint("Come on! ", "faster", "mark")
            sprint("Let's go already! ", "faster", "mark")
            sprint("Do you want to ", "normal", "quote")
            sprint("'begin' or ", "normal", "quote")
            sprint("'quit'?\n", "normal", "input")
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
                sprint("Hey don't go on ahead! ", "normal", "mark")
                sprint("See what happens before first!\n", "normal", "input")
            elif value == 2:
                # Don't you ever wonder why there is 'LOCKED' on the chapter?
                sprint("Don't you ever wonder why there is ", "normal", "quote")
                sprint("'LOCKED' on the chapter?\n", "normal", "input")
            elif value == 3:
                # Ok, this time try choosing something that isn't locked.
                sprint("Ok, ", "normal", "comma")
                sprint("this time try choosing something that isn't locked.\n", "normal", "input")
            elif value == 4:
                # I can't start that chapter if it's locked!
                sprint("I can't start that chapter if it's locked!\n", "normal", "input")
            elif value == 5:
                sprint("I'm pretty sure Tailstar locked these chapters for a reason...\n", "normal", "input")
            chapsel = input("> ")

        else:
            if value == 1:
                sprint("The journey finally begins! ", "normal", "mark")
                sprint("Let's go!\n", "normal", "mark")
            elif value == 2:
                sprint("You have no problems with starting do you? ", "normal", "mark")
                sprint("No? ", "normal", "mark")
                sprint("Ok, ", "normal", "comma")
                sprint("let's go!\n", "normal", "mark")
            elif value == 3:
                sprint("Now with that all over, ", "normal", "comma")
                sprint("let's start!\n", "normal", "mark")
            elif value == 4:
                sprint("I wonder how this story will go...\n", "normal", "period")
            elif value == 5:
                sprint("Hm... ", "normal", "period")
                sprint("I've run out of things to say!", "normal", "mark")
            s(2)
            print("\n" * 10)
            break

    else:
        if value == 1:
            sprint("There are only three chapters you know... ", "normal", "period")
            sprint("'01', ", "normal", "comma")
            sprint("'02', ", "normal", "comma")
            sprint("and '03'.\n", "normal", "input")
        elif value == 2:
            sprint("I feel like I'm talking to myself here! ", "normal", "mark")
            sprint("Well, ", "normal", "comma")
            sprint("maybe I am, ", "normal", "comma")
            sprint("but there's only three chapters to choose from!\n", "normal", "input")
        elif value == 3:
            sprint("I think you just typed a non-existent chapter... ", "normal", "period")
            sprint("There are only three chapters.\n", "normal", "input")
        elif value == 4:
            sprint("Are you purposely typing the wrong characters just to get me to talk? ", "normal", "mark")
            sprint("If you are it isn't working!\n", "normal", "input")
        elif value == 5:
            sprint("I have this odd feeling that you might secretly be Tailstar... ", "normal", "period")
            sprint("Or is that just me?\n", "normal", "input")
        chapsel = input("> ")

# Chapter 01 - The Tale of Blu
