import sys
from time import sleep
from random import randint

# http://stackoverflow.com/questions/22886353/printing-colors-in-python-terminal
# http://stackoverflow.com/questions/4099422/printing-slowly-simulate-typing
# http://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console


def color(text):
    if text == "bold_white":
        return "\033[1;37m"
    elif text == "bold_yellow":
        return "\033[1;33m"
    elif text == "bold_green":
        return "\033[1;32m"
    elif text == "bold_blue":
        return "\033[1;34m"
    elif text == "bold_cyan":
        return "\033[1;36m"
    elif text == "bold_red":
        return "\033[1;31m"
    elif text == "bold_magenta":
        return "\033[1;35m"
    elif text == "bold_black":
        return "\033[1;30m"
    elif text == "white":
        return "\033[0;37m"
    elif text == "yellow":
        return "\033[0;33m"
    elif text == "green":
        return "\033[0;32m"
    elif text == "blue":
        return "\033[0;34m"
    elif text == "cyan":
        return "\033[0;36m"
    elif text == "red":
        return "\033[0;31m"
    elif text == "magenta":
        return "\033[0;35m"
    elif text == "black":
        return "\033[0;30m"
    elif text == "off":
        return "\033[0;0m"
# print(color("bold_white") + "I'm white! " + color("bold_yellow") + "I'm yellow!")


def sprint(text, speed, delay):  # Print out text with a custom speed
    # TODO Add a few more sprint speeds
    for c in text:
        print(c, end=""),
        sys.stdout.flush()
        if speed == "default":  # Normal printing speed
            sleep(0.035)
        if speed == "slow":  # Slow printing speed
            sleep(0.05)
        if speed == "slower":  # Slower printing speed
            sleep(0.06)
        if speed == "faster":  # Faster printing speed
            sleep(0.02)
        if speed == "fast":  # Fast printing speed
            sleep(0.03)
    if delay == "comma":  # If the last punctuation is a comma (,)
        sleep(0.45)
    elif delay == "period":  # If the last punctuation is a period (.)
        sleep(1)
    elif delay == "quote":  # If the last punctuation is quotes ("")
        sleep(0.1)
    elif delay == "colon":  # If the last punctuation is a colon (:)
        sleep(0.3)
    elif delay == "list":  # If the last punctuation is a list of something
        sleep(0.05)
    elif delay == "mark":  # If the last punctuation is a punctuation mark (! ?)
        sleep(0.5)
    elif delay == "input":  # If the next code asks for an input
        sleep(0.05)


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


def ask_name():
    # Oh that reminds me! I still don't know your name yet!
    # Do you want to tell me your name? You don't have to, but it would be nice if you did!
    sprint("Oh that reminds me! ", "faster", "mark")
    sprint("I still don't know your name yet! ", "default", "mark")
    sprint("You don't have to tell me your name, ", "slow", "comma")
    sprint("but it would be nice if you did!\n", "faster", "period")
    print("Do you want to give your name? (Yes / No)")
    sleep(0.7)
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
                        sprint("Are yuo that person who plays that League of Legends game?", "default", "mark")
                        sprint("Nice to meet you!", "default", "mark")
                    return "Michael"
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
                    return "Riley"
                elif name == "tailstar":  # If the name entered is Tailstar
                    if value == 1:
                        # Are you actually Tailstar? Wait, I shouldn't be talking like that to you! Sorry!
                        sprint("Are you actually Tailstar? ", "default", "mark")
                        sprint("Wait, ", "default", "comma")
                        sprint("I shouldn't be talking like that to you! ", "faster", "mark")
                        sprint("Sorry!", "faster", "mark")
                    elif value == 2:
                        # You want me to turn you into another Pokémon? What Pokémon do you want to turn into this time?
                        sprint("You want me to turn you into another Pokémon? ", "default", "mark")
                        sprint("What Pokémon do you want to turn into this time?", "default", "mark")
                    elif value == 3:
                        # Has Storm beaten Remi in a Quick Attack race yet? I could put Storm in my Blu Games again!
                        sprint("Has Storm beaten Remi in a Quick Attack race yet? ", "default", "mark")
                        sprint("I could put Storm in my Blu Games again!", "default", "mark")
                    return "Tailstar"
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
                    return name
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
            sleep(1.5)
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
                # A simple question and a simple answer... Well, maybe not the answer, but typing the answer is simple!
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
