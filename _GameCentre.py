# Blu's Game Centre v1.0
# Aiyurn © 2016

from random import randint
from time import sleep as s
from games import arithmetic, numguess, bluadventure
from definitions import sprint, progressbar

# Introduction - Variables
game_choice = ""
menu_time = 0
give_name = ""

# Start - Game Choice input options
game_arithmetic = ["1", "a", "arithmetic"]
game_numguess = ["2", "n", "number guess"]
game_wordfind = ["3", "f", "find-a-word", "find a word"]
game_cyoa = ["4", "c", "cyoa", "choose your own adventure"]

# Start - Blu Adventure's messages
cyoamsg = ["test",
           "test2"]

# --------------- CODE BEGINS HERE ---------------

print("Blu's Game Centre v1.0")
print("Aiyurn (C) 2016\n")
s(1)
print("-------------------------------- WARNING --------------------------------\n"
      "Tailstar told me to remind you beforehard to not spam the enter button!\n"
      "He says that it will not only ruin the experience, but also screw up\n"
      "the code as you are inputting 'enter' for the upcoming inputs!\n"
      "-------------------------------------------------------------------------\n"
      "\n"
      "Now with that out of the way, let's play!")
items = list(range(0, 110))
i = 0
l = len(items)

# Initial call to print 0% progress
progressbar(i, l, prefix='Loading:', suffix='Complete', barlength=50)
for item in items:
    # Do stuff...
    s(0.1)
    # Update Progress Bar
    i += 1
    progressbar(i, l, prefix='Loading:', suffix='Complete', barlength=50)
print()

while game_choice == "":
    # Introduction text
    if menu_time < 1:  # If this is the first time the user is accessing this menu
        sprint("Welcome to my Game Centre!\n", "normal", "period")
        sprint("I'm Blu, ", "normal", "comma")
        sprint("and I'll be joining you in the games you play in this program!\n", "normal", "period")
        sprint("Here are the games you can choose from:\n", "normal", "colon")
        sprint("1) Arithmetic (Multiplication)\n", "super", "list")
        sprint("2) Number Guess\n", "super", "list")
        sprint("3) Find-a-word [IN DEVELOPMENT]\n", "super", "list")
        sprint("4) Blu's Adventures [BETA]\n", "super", "list")
        sprint("5) Tactical World [IN DEVELOPMENT]\n", "super", "list")
        sprint("6) Word Jam [IN DEVELOPMENT]\n", "super", "period")
        sprint("So, ", "normal", "comma")
        sprint("what game do you want to play?\n", "normal", "input")
    else:  # If the user has already accessed this menu i.e. coming back from a game
        print("And we're back at the menu again! What game do you want to play now?")
        print("Here are the games:\n"
              "1) Arithmetic (Multiplication)\n"
              "2) Number Guess\n"
              "3) Find-a-word [IN DEVELOPMENT]\n"
              "4) Blu's Adventures [BETA]\n"
              "5) Guess the country [IN DEVELOPMENT\n"
              "6) Letter Scramble [IN DEVELOPMENT")

    game_choice = input("> ")
    s(0.5)
    # Oh that reminds me! I still don't know your name yet!
    # Do you want to tell me your name? You don't have to, but it would be nice if you did!
    sprint("Oh that reminds me! ", "faster", "mark")
    sprint("I still don't know your name yet! ", "normal", "mark")
    sprint("Do you want to tell me your name? ", "normal", "mark")
    sprint("You don't have to, ", "slack", "comma")
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
            value = randint(1, 5)
            name = input("> ")
            print()
            break
        elif give_name == "no":
            if value == 1:
                # Oh... That's fine, let's continue to the game then...
                sprint("Oh... ", "slack", "period")
                sprint("That's fine, ", "slack", "comma")
                sprint("let's continue to the game then...\n", "slack", "period")
            elif value == 2:
                # I see... I did say you don't have to give it, let's go on to your game.
                sprint("I see... ", "slack", "period")
                sprint("I did say you don't have to give it, ", "slack", "comma")
                sprint("let's go on to your game.\n", "slack", "period")
            elif value == 3:
                # It would've been nice to call you by a name...
                sprint("It would've been nice to call you by a name...\n", "slack", "period")
            elif value == 4:
                # I guess I'm going to be still referencing you as... Well, you...
                sprint("I guess I'm going to be still referencing you as... ", "slack", "period")
                sprint("Well, ", "slack", "comma")
                sprint("you...\n", "slack", "period")
            elif value == 5:
                # So, no name? Ok then, off to the game we go...
                sprint("So, ", "slack", "comma")
                sprint("no name? ", "slack", "mark")
                sprint("Ok then, ", "slack", "comma")
                sprint("off to the game we go...\n", "slack", "period")
            s(1.5)
            break
        else:
            if value == 1:
                sprint("Wait... ", "defualt", "period")
                sprint("So are you giving me your name?", "default", "mark")
            elif value == 2:
                sprint("I don't know what you just typed, ", "default", "comma")
                sprint("but for all I know it isn't one of the options.", "default", "period")
            elif value == 3:
                sprint("A simple question and simple answer... ", "default", "period")
                sprint("Well, ", "default", "comma")
                sprint("maybe not the answer, ", "default", "comma")
                sprint("but typing the answer is simple!", "default", "mark")
            "Names... Such a strange thing... But back to the point, you didn't type one of the options!" \
            "I thought I asked a yes or no question... I guess it wasn't so simple?"
            give_name = input("> ")
    while True:
        value = randint(1, 5)  # Random number to determine which message to be displayed
        if game_choice in game_arithmetic:  # If the user selects the game Arithmetic
            if value == 1:
                # Let's check out your maths skills!
                sprint("Let's check out your maths skills!", "normal", "mark")
            elif value == 2:
                # 6 x 5 is 11 right? No? Maybe I should just leave the maths to Tailstar...
                sprint("6 x 5 is 11 right?", "normal", "mark")
                sprint("No? ", "normal", "mark")
                sprint("Maybe I should just leave the maths to Tailstar...", "normal", "period")
            elif value == 3:
                # Arithmetic? Sure let's go!
                sprint("Arithmetic? ", "normal", "mark")
                sprint("Sure let's go!", "normal", "mark")
            elif value == 4:
                # So you like maths I see... Let's see how good you are!
                sprint("So you like maths I see... ", "normal", "period")
                sprint("Let's see how good you are!", "normal", "mark")
            elif value == 5:
                # I, Blu, challenge you to a maths battle!
                sprint("I, ", "normal", "comma")
                sprint("Blu, ", "normal", "comma")
                sprint("challenge you to a maths battle!", "normal", "mark")
            s(2)
            print("\n" * 2)
            arithmetic()
            game_choice = ""  # Reset gamechoice to enter back into the while loop
            break
        elif game_choice in game_numguess:  # If the user selects the game Number Guess
            if value == 1:
                # Let's see if you can beat me, the legendary Blu!
                sprint("Let's see if you can beat me, ", "normal", "comma")
                sprint("the legendary Blu!", "normal", "mark")
            elif value == 2:
                # So you like number guessing, just like Tailstar!
                sprint("So you like number guessing, ", "normal", "comma")
                sprint("just like Tailstar!", "normal", "mark")
            elif value == 3:
                # Good choice! Let's begin!
                sprint("Good choice! ", "normal", "mark")
                sprint("Let's begin!", "normal", "mark")
            elif value == 4:
                # If you're planning to play easy mode, I'm going to guess that the number will be ***!
                number = str(randint(1, 1000))
                sprint("If you're planning to play easy mode, ", "normal", "comma")
                sprint("I'm going to guess that the number will be" + number + "!", "normal", "mark")
            elif value == 5:
                # I wonder if you'll beat me and Tailstar's high-scores... Let's play and see!
                sprint("I wonder if you'll beat me and Tailstar's high-scores... ", "normal", "period")
                sprint("Let's play and see!", "normal", "mark")
            s(2)
            print("\n"*2)
            numguess()
            game_choice = ""  # Reset gamechoice to enter back into the while loop
            break

#       elif gamechoice in game_wordfind:
#       print(random.choice(wordfind))
#       time.sleep(2)
#       print("\n"*2)
#           break

        elif game_choice in game_cyoa:  # If the user selects the game Blu's Adventure
            if value == 1:
                # I knew it! You are the adventurous type! COme on Tailstar is waiting for us!
                sprint("I knew it! ", "normal", "mark")
                sprint("You are the adventurous type! ", "normal", "mark")
                sprint("Come on Tailstar is waiting for us!", "normal", "mark")
            elif value == 2:
                # You like adventures too? Come join me in my adventures with Tailstar!
                sprint("You like adventures too? ", "normal", "mark")
                sprint("Come join me in my adventures with Tailstar!", "normal", "mark")
            elif value == 3:
                # Everyone loves adventures! Especially when I'm in it! ...Right?
                sprint("Everyone loves adventures! ", "normal", "mark")
                sprint("Especially when I'm in it! ", "normal", "mark")
                sprint("...Right?", "slower", "mark")
            elif value == 4:
                # You're joining my adventure? Yay! We must hurry to the meeting point!
                sprint("You're joining my adventure? ", "normal", "mark")
                sprint("Yay! ", "faster", "mark")
                sprint("We must hurry to the meeting point!", "normal", "mark")
            elif value == 5:
                # Hopefully my adventure doesn't have that 'breaking the fourth wall' people have been talking about...
                sprint("Hopefully my adventure doesn't have that ", "normal", "quote")
                sprint("'breaking the fourth wall' people have been talking about...", "normal", "period")
            s(2)
            print("\n"*2)
            bluadventure()
            game_choice = ""
            break

        elif game_choice == 'quit':  # If the user wants to quit
            quit()

        else:  # If the user selects a game that isn't in the list
            if value == 1:
                # Hey that's not an option!
                sprint("Hey that's not an option!\n", "normal", "mark")
            elif value == 2:
                # I think you typed something wrong... There's no option for that.
                sprint("I think you typed something wrong... ", "normal", "period")
                sprint("There's no option for that.\n", "normal", "period")
            elif value == 3:
                # Are you purposely typing it wrong to get me to talk? If you are, it's not working!
                sprint("Are you purposely typing it wrong to get me to talk? ", "normal", "mark")
                sprint("If you are, ", "normal", "comma")
                sprint("it's not working!\n", "normal", "mark")
            elif value == 4:
                # I don't think that option you typed is an option...
                sprint("I don't think that option you typed is an option...\n", "normal", "period")
            elif value == 5:
                # Let's go and play something already! Don't choose a game that you can't play!
                sprint("Let's go and play something already! ", "normal", "mark")
                sprint("Don't choose a game that you can't play!\n", "normal", "mark")
            game_choice = input("> ")

    s(2)
