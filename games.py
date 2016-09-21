# Blu's Game Centre - Games v1.0
# Aiyurn (C) 2016

import random
from time import sleep
import sys

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


def print_slowly(text, speed):
    for c in text:
        print(c, end=""),
        sys.stdout.flush()
        sleep(speed)


def arithmetic():
    # Arithmetic - Non-digit rounds messages
    roundnotdigit = ["That's not a number!",
                     "You sure what you typed is a number?",
                     "You do know if you can't type out a number you'll have no chance to do this arithmetic right?",
                     "Psst... It has to be a number!",
                     "Hm... The code doesn't seem to like what you typed. Are you sure it's a number?"]

    # Arithmetic - Negative round numbers
    negativenum = ["You can't use a negative number as a round!",
                   ""]

    # Arithmetic - Difficulty input options
    easy = ["e", "ea", "eas", "easy"]
    medium = ["m", "me", "med", "medi", "mediu", "medium"]
    hard = ["h", "ha", "har", "hard"]

    # Arithmetic - Easy messages
    easymsg = ["Come on, easy? I thought you would choose something harder... Oh well, let's go!",
               "Easy mode? I guess everyone starts from somewhere...",
               "Aww easy mode? You could do better than that!",
               "Choosing easy mode I see... Let's see how you go!",
               "Easy come easy go... Let's go!"]

    # Arithmetic - Medium messages
    mediummsg = ["I see that you're one of those average players. Let's see how you go!",
                 "You've made a good choice! Let's begin!",
                 "Medium, not too hard, not too easy. Let's go!",
                 "Medium mode... I don't really have anything to say... Let's just start shall we?",
                 "At least you didn't choose easy mode! Let's go!"]

    # Arithmetic - Hard messages
    hardmsg = ["Going for hard mode... You must be really good at arithmetic!",
               "Hard mode here we come!",
               "Not easy, not medium, but hard. I like it! Let's go!",
               "If you think about it anything hard is easy if you know how to do it.",
               "Ha ha ha hard! That was bad wasn't it? Let's just begin..."]

    # Arithmetic - Messages if selected option isn't in difficulty
    notdifficulty = ["There is only three difficulties to choose from...",
                     "You didn't type a difficulty!",
                     "Is it so difficult to choose a difficulty? That didn't work out the way I wanted to...",
                     "I've listed the difficulties for you! All you need to do is choose one!",
                     "I feel like you're purposely typing it wrong... Or is that just me?"]

    # Arithmetic - Not digit for answers
    answernotdigit = ["Hey that's not a number!",
                      "I don't think that's a number...",
                      "It has to be a number!",
                      "Times tables won't ever have letters as an answer..."
                      "I shouldn't really have to tell you where you typed wrong with your answer..."]

    # Arithmetic - Correct answers
    answercorrect = ["You got it right!",
                     "Yay! It's correct!"]

    # Arithmetic - Incorrect answers
    answerincorrect = ["Aww, that's not right!"]

    # Arithmetic - Play again input options
    yesagain = ["y", "yes", "ye"]
    noagain = ["n", "no"]

    # Arithmatic - Play again other options
    other2 = ["Wait... So do you want to play again?"]

    playing = "y"  # Whether the game is in "Play" mode
    correct = 0
    incorrect = 0
    easytable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    mediumtable = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    hardtable = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    while playing == "y":
        print("How many rounds do you want to play?")
        rounds = input("> ")
        while True:
            if rounds.isalpha():  # Checks if the input is a number
                print(random.choice(roundnotdigit))
                rounds = input("> ")
            elif int(rounds) < 0:
                print(random.choice(negativenum))
                rounds = input("> ")
            else:
                break
        rounds = int(rounds)  # Converts rounds into a integer
        print("What difficulty do you want to play in? (e)asy, (m)edium or (h)ard?")
        difficulty = input("> ")
        while True:
            if difficulty in easy:
                print(random.choice(easymsg))
                sleep(3)
                # If user selects "easy", print random message and pause for 3 seconds
                break
            elif difficulty in medium:
                print(random.choice(mediummsg))
                sleep(3)
                # If user selects "medium", print random message and pause for 3 seconds
                break
            elif difficulty in hard:
                print(random.choice(hardmsg))
                sleep(3)
                # If user selects "hard", print random message and pause for 3 seconds
                break
            else:
                print(random.choice(notdifficulty))
                difficulty = input("> ")
        while rounds > 0:
            if difficulty in easy:
                table1 = random.choice(easytable)
                table2 = random.choice(easytable)

            elif difficulty in medium:
                table1 = random.choice(mediumtable)
                table2 = random.choice(mediumtable)

            elif difficulty in hard:
                table1 = random.choice(hardtable)
                table2 = random.choice(hardtable)

            tableanswer = table1 * table2
            print(table1, "x", table2, "=")
            useranswer = input("Answer: ")
            while not useranswer.isdigit():
                print(random.choice(answernotdigit))
                useranswer = input("Answer: ")
            useranswer = int(useranswer)
            if useranswer == tableanswer:
                print(random.choice(answercorrect))
                correct += 1

            elif useranswer != tableanswer:
                print(random.choice(answerincorrect))
                incorrect += 1
                print("The right answer is", tableanswer)

            else:
                print("If you see this message you definitely broke something.")
            rounds -= 1  # Minus one from the rounds the user has asked to play
        print("You got it correct:", correct, "time(s)!", "You got it wrong:", incorrect, "time(s)!")
        print("Do you want to play again? Yes or no?")
        while True:
            playagain = input("> ")
            if playagain in yesagain:
                correct = 0
                incorrect = 0
                playing = "y"
                # If user plays again, reset correct and incorrect
                break
            elif playagain in noagain:
                playing = "n"
                break
            else:
                print(random.choice(other2))


def numguess():
    num = 0
    easy = ["e", "easy", "1"]
    normal = ["n", "normal", "2"]
    hard = ["h", "hard", "3"]
    insane = ["i", "insane", "4"]
    superinsane = ["s", "super insane", "5"]

    easymsg = ["Aww easy mode? Oh well, let's go"]
    normalmsg = ["So you're one of those average players. Now, let's begin!"]
    hardmsg = ["I see you chose hard mode. I wish you luck."]
    insanemsg = ["You're insane for choosing insane!"]
    superinsanemsg = ["If you can complete this you are definitely a robot..."]

    other3 = ["yo"]

    print("Think you're up for a game of number guessing?")
    sleep(1)
    print("Here are three difficulties:\n"
          "For Easy, type 'e'\n"
          "For Normal, type 'n'\n"
          "For Hard, type 'h'\n"
          "For Insane, type 'i'\n"
          "For Super Insane, type 's'")
    diff = input("> ")

    while True:
        if diff in easy:
            print(random.choice(easymsg))
            print("You'll have 30 lives to guess a number between 1-1000")
            lives = 30
            num = 1000
            break
        elif diff in normal:
            print(random.choice(normalmsg))
            print("You'll have 25 lives to guess a number between 1-1500")
            lives = 25
            num = 1500
            break
        elif diff in hard:
            print(random.choice(hardmsg))
            print("You'll have 20 lives to guess a number between 1-2200")
            lives = 20
            num = 2200
            break
        elif diff in insane:
            print(random.choice(insanemsg))
            print("You'll have 10 lives to guess a number between 1-5000")
            lives = 10
            num = 5000
            break
        elif diff in superinsane:
            print(random.choice(superinsanemsg))
            print("You'll have 5 lives to guess an number between 1-10000")
            lives = 5
            num = 10000
            break
        else:
            print(random.choice(other3))
            diff = input("> ")

    a = random.randint(1, num)  # Choose a random number between 1 and a number depending on the difficulty selected
    deaths = 0
    print("Guess a number between 1-" + str(num) + ":")
    while lives > deaths:
        guess = input("> ")
        while not guess.isdigit():  # Checks if the input entered is a number
            print("That is not a number!")
            guess = input("> ")
        guess = int(guess)
        if guess > int(num):
            print("Its between 1-" + str(num) + "... It can't go higher than", str(num) + ".")
        elif guess < 0:
            print("Its between 1-" + str(num) + "... It can't go lower than 0.")
        elif guess < a:
            print("Higher!")
            deaths += 1
        elif guess > a:
            print("Lower!")
            deaths += 1
        if guess == a:
            print("Correct!")
            deaths += 1
            print("It took you", deaths, "guess(es) this round!")
        if deaths == lives:
            print("One more life remaining be careful.")
        if deaths > lives:
            print("Game over")
            print("good try but the answer was", a + ".")


def bluadventure():
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

    # Chapter select - Locked chapters
    locked1 = ["Tailstar locked these chapters for a reason...",
               "Don't you ever wonder why there is 'LOCKED' on the chapter?",
               "Ok, this time try choosing something that isn't locked.",
               "I can't start that chapter if it's locked!",
               "Maybe finish the unlocked chapters first before going on to the locked ones..."]

    # Chapter select - Other chapters
    other2 = ["There are only three chapters you know... '01', '02', and '03'.",
              "I feel like I'm talking to myself here! Maybe I am, but there's only three chapters to choose from!",
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
          "maybe you like Tailstar?")

    # Chapter 01 - The Tale of Blu


def guesscountry():
    print("no code")
    # NO CODE EXISTS FOR THIS GAME YET.
