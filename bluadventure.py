from random import randint
from time import sleep as s
from definitions import sprint

# Start - program varible outputs
start1 = ["begin", "b", "start", "s"]
start2 = ["quit", "q", "leave", "l"]

blu2 = []
blu3 = []

# Chapter select - Total chapters
chapter = ["01", "1", "02", "2", "03", "3"]
locked = ["02", "2", "03", "3"]


def islocked():
    if chapsel in locked:
        return True
    else:
        return False


# Introduction text
sprint("Welcome to Blu's Adventure!\n", "default", 1.2)
sprint("Come on Tailstar we have a person who wants to join us!\n", "default", "mark")
sprint("To join me in my adventure, ", "default", "comma")
sprint("type ", "default", "quote")
sprint("'begin'! ", "default", "mark")
sprint("To leave, ", "default", "comma")
sprint("type ", "default", "quote")
sprint("'quit'.\n", "default", "input")

# Start
program = input("> ")
while True:
    value = randint(1, 5)
    if program in start1:
        if value == 1:
            sprint("Let the journey begin!\n", "default", "mark")
        elif value == 2:
            sprint("You're coming? ", "default", "mark")
            sprint("Well then what are you waiting for? ", "default", "puncutation")
            sprint("Let's go!\n", "default", "mark")
        elif value == 3:
            sprint("You're joining us? ", "default", "mark")
            sprint("That makes three! ", "default", "mark")
            sprint("Come on!\n", "default", "mark")
        elif value == 4:
            sprint("Yay! ", "default", "mark")
            sprint("Someone else who wants to come with us!\n", "default", "mark")
        elif value == 5:
            sprint("We're going to have so much fun!\n", "default", "mark")
        s(1)
        print("\n" * 2)
        break
    elif program in start2:
        if value == 1:
            sprint("Aww... ", "slower", "period")
            sprint("I really wanted you to come...\n", "slower", "period")
        elif value == 2:
            sprint("I thought you liked adventures... ", "slower", "period")
            sprint("That's why you chose this game right?\n", "slower", "mark")
        elif value == 3:
            sprint("Oh... ", "slower", "period")
            sprint("Well, ", "slower", "comma")
            sprint("you're always welcome to come back when you want to!\n", "slower", "mark")
        elif value == 4:
            sprint("I guess I never said you had to come with us... ", "slower", "period")
            sprint("Although we really hoped you did...\n", "slower", "period")
        elif value == 5:
            sprint("But... ", "slower", "period")
            sprint("What did I say for you to not come with us?\n", "slower", "mark")
        s(1)
        quit()
    else:
        if value == 1:
            sprint("I thought I said there we're only two options, ", "default", "comma")
            sprint("'begin' or 'quit'?\n", "default", "input")
        elif value == 2:
            sprint("I think you mistyped something... ", "default", "period")
            sprint("You sure you typed either 'begin' or 'leave'?\n", "default", "input")
        elif value == 3:
            sprint("And here I thought Tailstar couldn't spell... ", "default", "period")
            sprint("Like I said, ", "default", "comma")
            sprint("do you want to 'begin' or 'leave'?\n", "default", "input")
        elif value == 4:
            sprint("I don't think I said anything else other than 'begin' or 'quit'?\n", "default", "input")
        elif value == 5:
            sprint("Come on! ", "default", "mark")
            sprint("Let's go already! ", "default", "mark")
            sprint("Do you want to 'begin' or 'quit'?\n", "default", "input")
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
                sprint("Hey don't go on ahead! ", "default", "mark")
                sprint("See what happens before first!\n", "default", "input")
            elif value == 2:
                sprint("Don't you ever wonder why there is ", "default", "quote")
                sprint("'LOCKED' on the chapter?\n", "default", "input")
            elif value == 3:
                sprint("Ok, ", "default", "comma")
                sprint("this time try choosing something that isn't locked.\n", "default", "input")
            elif value == 4:
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

print("Oh I completely forgot! Tailstar and I still don't know your name yet!\n"
      "Do you want to tell us your name? You don't have to, but if you don't\n"
      "give us your name we'll just use Tailstar as your name! Who knows,\n"
      "maybe you like Tailstar? ")

# Chapter 01 - The Tale of Blu
