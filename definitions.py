import sys
from time import sleep
from random import randint

# Usage: print(color['white'] + 'string' + color['off'])
color = {
    'bold_white':      "\033[1;37m",
    'bold_yellow':     "\033[1;33m",
    'bold_green':      "\033[1;32m",
    'bold_blue':       "\033[1;34m",
    'bold_cyan':       "\033[1;36m",
    'bold_red':        "\033[1;31m",
    'bold_magenta':    "\033[1;35m",
    'bold_black':      "\033[1;30m",
    'white':           "\033[0;37m",
    'yellow':          "\033[0;33m",
    'green':           "\033[0;32m",
    'blue':            "\033[0;34m",
    'cyan':            "\033[0;36m",
    'red':             "\033[0;31m",
    'magenta':         "\033[0;35m",
    'black':           "\033[0;30m",
    'off':             "\033[0;0m",
}
'''
print(color['bold_white'] + 'string' + color['off'])
print(color['bold_yellow'] + 'string' + color['off'])
print(color['bold_green'] + 'string' + color['off'])
print(color['bold_blue'] + 'string' + color['off'])
print(color['bold_cyan'] + 'string' + color['off'])
print(color['bold_red'] + 'string' + color['off'])
print(color['bold_magenta'] + 'string' + color['off'])
print(color['bold_black'] + 'string' + color['off'])
print(color['white'] + 'string' + color['off'])
print(color['yellow'] + 'string' + color['off'])
print(color['green'] + 'string' + color['off'])
print(color['blue'] + 'string' + color['off'])
print(color['cyan'] + 'string' + color['off'])
print(color['red'] + 'string' + color['off'])
print(color['magenta'] + 'string' + color['off'])
print(color['black'] + 'string' + color['off'])
'''


def sprint(text, speed, delay):  # Print out text with a custom speed
    for c in text:
        print(c, end=""),
        sys.stdout.flush()
        if speed == "normal":  # Default printing speed
            sleep(0.035)
        if speed == "slack":  # Slow printing speed
            sleep(0.05)
        if speed == "slower":  # Slower printing speed
            sleep(0.06)
        if speed == "super":  # Fastest printing speed
            sleep(0.02)
        if speed == "faster":  # Faster printing speed
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
    sprint("I still don't know your name yet! ", "normal", "mark")
    sprint("Do you want to tell me your name? ", "normal", "mark")
    sprint("You don't have to, ", "slack", "comma")
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
            value = randint(1, 5)
            print("Please enter your name.")
            name = input("> ")
            if name == "Michael":
                if value == 1:
                    print()
                elif value == 2:
                    print()
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
                sprint("Names... ", "slack", "period")
                sprint("Such a strange thing... ", "slack", "period")
                sprint("But back to the point, ", "default", "comma")
                sprint("you didn't type one of the options!\n", "default", "mark")
            elif value == 5:
                # I thought I asked a simple yes or no question... I guess it wasn't so simple?
                sprint("I thought I asked a simple yes or no question... ", "default", "period")
                sprint("I guess it wasn't so simple?", "default", "mark")
            give_name = input("> ")
