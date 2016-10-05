import random
from time import sleep

# Start - program varible outputs
start1 = ["begin", "b", "start", "s"]
start2 = ["quit", "q", "leave", "l"]

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
print("Welcome to Blu's Adventure!\n"
      "Come on Tailstar we have a person who wants to join us!\n"
      "To join me in my adventure, type 'begin'! To leave, type 'quit'")

# Start
program = input("> ")
while True:
    if program in start1:
        print(random.choice(begin1))
        sleep(2)
        print("\n" * 2)
        break
    elif program in start2:
        print(random.choice(quit1))
        sleep(2)
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
