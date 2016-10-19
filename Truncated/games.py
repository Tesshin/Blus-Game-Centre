# Blu's Game Centre - Games v1.0
# Aiyurn (C) 2016

import random
from random import randint
from time import sleep
from definitions import sprint


def arithmetic():
    # TODO Convert print messages into sprint lines
    # Non-digit rounds messages
    roundnotdigit = ["That's not a number!",
                     "You sure what you typed is a number?",
                     "You do know if you can't type out a number you'll have no chance to do this arithmetic right?",
                     "Psst... It has to be a number!",
                     "Hm... The code doesn't seem to like what you typed. Are you sure it's a number?"]

    # Negative round numbers
    negativenum = ["You can't use a negative number as a round!",
                   ""]

    # If selected 0 rounds
    norounds = ["Really? You have to at least choose one round!"]

    # Difficulty input options
    easy = ["e", "ea", "eas", "easy"]
    medium = ["m", "me", "med", "medi", "mediu", "medium"]
    hard = ["h", "ha", "har", "hard"]

    # Easy messages
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

    # Arithmetic - Play again other options
    other2 = ["Wait... So do you want to play again?"]

    playing = "y"  # Whether the game is in "Play" mode
    correct = 0
    incorrect = 0
    easytable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    mediumtable = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    hardtable = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    value = randint(1, 5)
    if value == 1:
        print()
    elif value == 2:
        print()
    elif value == 3:
        print()
    elif value == 4:
        print()
    elif value == 5:
        print()
    while playing == "y":
        sprint("How many rounds do you want to play?", "default", "mark")
        rounds = input("> ")
        while True:
            if rounds.isalpha():  # Checks if the input is a number
                print(random.choice(roundnotdigit))
                rounds = input("> ")
            elif int(rounds) < 0:  # Checks if the amount of rounds is less than 0
                print(random.choice(negativenum))
                rounds = input("> ")
            elif int(rounds) == 0:  # Checks if the amount of rounds is 0
                print(random.choice(norounds))
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
    # TODO Convert print messages into sprint lines
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
