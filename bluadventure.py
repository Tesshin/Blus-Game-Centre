import random
from time import sleep
from definitions import sprint

# Start - program varible outputs
start1 = ["begin", "b", "start", "s"]
start2 = ["quit", "q", "leave", "l"]

# Chapter select - Blu's messages
blu1 = ["The journey finally begins! Let's go!",
        "You have no problems with starting do you? No? Ok, let's go!",
        "Now with that all over, let's start!",
        "I wonder how this story will go...",
        "Hm... I've run out of things to say!"]

blu2 = []
blu3 = []

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

# Chapter select - Total chapters
chapter = ["01", "1", "02", "2", "03", "3"]
locked = ["02", "2", "03", "3"]


def islocked():
    if chapsel in locked:
        return True
    else:
        return False


# Introduction text
sprint("Welcome to Blu's Adventure!\n", "default", 1.5)
sprint("Come on Tailstar we have a person who wants to join us!\n", "default", "period")
sprint("To join me in my adventure, ", "default", "comma")
sprint("type 'begin'! ", "default", "period")
sprint("To leave, ", "default", "comma")
sprint("type 'quit'.\n", "default", "period")

# Start
program = input("> ")
while True:
    value = random.randint(1, 5)
    if program in start1:
        if value == 1:
            sprint("Let the journey begin!\n", "default", "period")
            sleep(1)
            print("\n" * 2)
            break
        elif value == 2:
            sprint("You're coming? ", "default", "period")
            sprint("Well then what are you waiting for? ", "default", "period")
            sprint("Let's go!\n", "default", "period")
            sleep(1)
            print("\n" * 2)
            break
        elif value == 3:
            sprint("You're joining us? ", "default", "period")
            sprint("That makes three! ", "default", "period")
            sprint("Come on!\n", "default", "period")
            sleep(1)
            print("\n" * 2)
            break
        elif value == 4:
            sprint("Yay! ", "default", "period")
            sprint("Someone else who wants to come with us!\n", "default", "period")
            sleep(1)
            print("\n" * 2)
            break
        elif value == 5:
            sprint("We're going to have so much fun!\n", "default", "period")
        else:
            sprint("Hm... ", "default", "period")
            sprint("Something is not right, ", "default", "comma")
            sprint("you're not supposed to get this message...", "default", "comma")
    elif program in start2:
        if value == 1:
            sprint("Aww... ", "slower", "period")
            sprint("I really wanted you to come...\n", "slower", "period")
            sleep(1)
            quit()
        elif value == 2:
            sprint("I thought you liked adventures... ", "slower", "period")
            sprint("That's why you chose this game right?\n", "slower", "period")
            sleep(1)
            quit()
        elif value == 3:
            sprint("Oh... ", "slower" , "period")
            sprint("Well, ", "slower", "comma")
            sprint("you're always welcome to come back when you want to!\n", "slower", "period")
            sleep(1)
            quit()
        elif value == 4:
            sprint("I guess I never said you had to come with us... ", "slower", "period")
            sprint("Although we really hoped you did...\n", "slower", "period")
            sleep(1)
            quit()
        elif value == 5:
            sprint("But... ", "slower", "period")
            sprint("What did I say for you to not come with us?\n", "slower", "period")
            sleep(1)
            quit()
    else:
        if value == 1:
            sprint("I thought I said there we're only two options, ", "default", "comma")
            sprint("'begin' or 'quit'?\n", "default", "period")
            program = input("> ")
        elif value == 2:
            sprint("I think you mistyped something... ", "default", "period")
            sprint("You sure you typed either 'begin' or 'leave'?\n", "default", "period")
            program = input("> ")
        elif value == 3:
            sprint("And here I thought Tailstar couldn't spell... ", "default", "period")
            sprint("Like I said, ", "default", "comma")
            sprint("do you want to 'begin' or 'leave'?\n", "default", "period")
            program = input("> ")
        elif value == 4:
            sprint("I don't think I said anything else other than 'begin' or 'quit'?\n", "default", "period")
            program = input("> ")
        elif value == 5:
            sprint("Come on! ", "default", "period")
            sprint("Let's go already! ", "default", "period")
            sprint("Do you want to 'begin' or 'quit'?\n", "default", "period")
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
            sleep(2)
            print("\n" * 10)
            break
    else:
        print(random.choice(other2))
        chapsel = input("> ")

print("Oh I completely forgot! Tailstar and I still don't know your name yet!\n"
      "Do you want to tell us your name? You don't have to, but if you don't\n"
      "give us your name we'll just use Tailstar as your name! Who knows,\n"
      "maybe you like Tailstar? ")

# Chapter 01 - The Tale of Blu
