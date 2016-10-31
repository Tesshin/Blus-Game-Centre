from random import randint
from time import sleep as s  # All sleep functions will now be called s
from definitions import sprint

# Start - program variable outputs
start1 = ["begin", "b", "start", "s"]
start2 = ["quit", "q", "leave", "l"]
current_chapter = ""

# Chapter select - Total chapters
chapter = ["01", "1", "02", "2", "03", "3"]
locked = ["02", "2", "03", "3"]


def islocked():  # A function that checks whether the selected chapter is locked
    if chapsel in locked:
        return True
    else:
        return False

# Introduction text
sprint("Welcome to Blu's Adventure!\n", "normal", "mark")
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
            sprint("Come on! ", "fast", "mark")
            sprint("Let's go already! ", "fast", "mark")
            sprint("Do you want to ", "normal", "quote")
            sprint("'begin' or ", "normal", "quote")
            sprint("'quit'?\n", "normal", "input")
        program = input("> ")

# Chapter Select
print("Chapter Select:\n",
      "'01' - The Tale of Blu\n",
      "'02' - The Adventure Begins! [LOCKED]\n",
      "'03' - Your First Pokémon [LOCKED]")

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
                # The journey finally begins! Let's go!
                sprint("The journey finally begins! ", "normal", "mark")
                sprint("Let's go!\n", "normal", "mark")
            elif value == 2:
                # You have no problems with starting do you? No? Ok, let's go!
                sprint("You have no problems with starting do you? ", "normal", "mark")
                sprint("No? ", "normal", "mark")
                sprint("Ok, ", "normal", "comma")
                sprint("let's go!\n", "normal", "mark")
            elif value == 3:
                # Now with that all over, let's start!
                sprint("Now with that all over, ", "normal", "comma")
                sprint("let's start!\n", "normal", "mark")
            elif value == 4:
                # I wonder how this story will turn out...
                sprint("I wonder how this story will turn out...\n", "normal", "period")
            elif value == 5:
                # Hm... I've run out of things to say!
                sprint("Hm... ", "normal", "period")
                sprint("I've run out of things to say!\n", "normal", "mark")
            s(2)
            print("\n" * 10)
            break

    else:
        if value == 1:
            # There aren't that many chapters to choose from you know...
            sprint("There aren't that many chapters to choose from you know...\n", "default", "input")
        elif value == 2:
            # I feel like I'm talking to myself here! Well, maybe I am, but there's only so many chapters to select!
            sprint("I feel like I'm talking to myself here! ", "fast", "mark")
            sprint("Well, ", "slack", "comma")
            sprint("maybe I am, ", "normal", "comma")
            sprint("but there's only so many chapters to select!\n", "normal", "input")
        elif value == 3:
            # I think you just typed a chapter that doesn't exist... Try typing one that exists this time.
            sprint("I think you just typed a chapter that doesn't exist... ", "normal", "period")
            sprint("Try typing one that exists this time.\n", "normal", "input")
        elif value == 4:
            # Are you purposely typing the wrong chapters just to get me to talk? If you are it isn't working!
            sprint("Are you purposely typing the wrong chapters just to get me to talk? ", "normal", "mark")
            sprint("If you are it isn't working!\n", "fast", "input")
        elif value == 5:
            # Are you by any chance secretly Tailstar... Or am I just imagining things?
            sprint("Are you by any chance secretly Tailstar... ", "normal", "period")
            sprint("Or am I just imagining things?\n", "normal", "input")
        chapsel = input("> ")

# Chapter 01 - The Tale of Blu
# TODO Finish chapter one
while chapsel == "01" or chapsel == "1":
    print("Chapter 01 - The Tale of Blu\n\n")
    s(4)
    print("Now, you may be wondering...\n")
    s(2)
    print("Who is Blu and Tailstar? Why are they inviting you on a journey?\n")
    s(3)
    print("To figure out why... We need to go back a few months...")

# Chapter 02 - The Adventure Begins!
# TODO Begin code for chapter two
while chapsel == "02" or chapsel == "2":
    print("Chapter 02 - The Adventure Begins!")

# Chapter 03 - Your First Pokémon
# TODO Begin code for chapter three
while chapsel == "03" or chapsel == "3":
    print("Chapter 03 - Your First Pokémon")