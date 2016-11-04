# Blu's Game Centre - Games v1.0
# Aiyurn (C) 2016

import random
from random import randint
from time import sleep
from sprint import sprint


def arithmetic(name):
    # TODO Convert print messages into sprint lines

    # Difficulty input options
    easy = ["e", "ea", "eas", "easy"]
    medium = ["m", "me", "med", "medi", "mediu", "medium"]
    hard = ["h", "ha", "har", "hard"]

    # Arithmetic - Correct answers
    answercorrect = ["You got it right!",
                     "Yay! It's correct!"]

    # Arithmetic - Incorrect answers
    answerincorrect = ["Aww, that's not right!"]

    # Arithmetic - Play again input options
    yesagain = ["y", "yes", "ye"]
    noagain = ["n", "no"]

    playing = "y"  # Whether the game is in "Play" mode
    correct = 0
    incorrect = 0
    easytable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    mediumtable = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    hardtable = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    while playing == "y":
        value = randint(1, 3)
        if value == 1:
            # Ok NAME, how many rounds do you want to play?
            sprint("Ok " + name + ", ", "default", "comma")
            sprint("how many rounds do you want to play?\n", "default", "mark")
        elif value == 2:
            # Looks like we're here, how many rounds do you wnat to play NAME?
            sprint("Looks like we're here, ", "default", "comma")
            sprint("how many rounds do you want to play " + name + "?\n", "default", "mark")
        elif value == 3:
            # Now I can challenge you! How many rounds NAME?
            sprint("Now I can challenge you! ", "fast", "mark")
            sprint("How many rounds " + name + "?\n", "fast", "mark")
        rounds = input("> ")
        while True:  # Checks if the input is a number
            if rounds.isalpha():  # If input is a letter
                value = randint(1, 5)
                if value == 1:
                    # That's not a number!
                    sprint("That's not a number!\n", "default", "mark")
                elif value == 2:
                    # You sure what you typed is a number?
                    sprint("You sure what you typed is a number?\n", "default", "mark")
                elif value == 3:
                    # If you can't type out numbers what chance do you have against this game?
                    sprint("If you can't type numbers what chance do you have against this game?\n", "default", "mark")
                elif value == 4:
                    # Psst... It has to be a number!
                    sprint("Psst... ", "slow", "period")
                    sprint("It has to be a number!\n", "default", "mark")
                elif value == 5:
                    # Hm... The code doesn't seem to like what you typed. Are you sure it's a number?
                    sprint("Hm... ", "default", "period")
                    sprint("The code doesn't seem to like what you typed. ", "default", "period")
                    sprint("Are you sure it's a number?", "default", "mark")
                rounds = input("> ")
            elif int(rounds) < 0:  # If the amount of rounds is less than 0
                # You can't use a negative number as a round!
                sprint("You can't use a negative number as a round!", "default", "mark")
                rounds = input("> ")
            elif int(rounds) == 0:  # If the amount of rounds is 0
                # Really? You have to at least choose one round!
                sprint("Really? ", "default", "comma")
                sprint("You have to at least choose one round!", "default", "mark")
                rounds = input("> ")
            else:
                break
        rounds = int(rounds)  # Converts rounds into a integer
        # What difficulty do you want to play in? (e)asy, (m)edium or (h)ard?
        sprint("What difficulty do you want to play in? ", "default", "mark")
        sprint("(e)asy, ", "faster", "comma")
        sprint("(m)edium or (h)ard?\n", "faster", "mark")
        difficulty = input("> ")
        while True:
            value = randint(1, 5)
            if difficulty in easy:  # If user selects "easy", print random message.
                if value == 1:
                    # Come on, easy NAME? I thought you would choose something harder...
                    # Oh well, let's go!
                    sprint("Come on, ", "default", "comma")
                    sprint("easy " + name + "? ", "default", "mark")
                    sprint("I thought you would choose something harder... ", "default", "period")
                    sprint("Oh well, ", "default", "comma")
                    sprint("let's go!\n", "default", "mark")
                elif value == 2:
                    # Easy mode? I guess everyone starts from somewhere...
                    sprint("Easy mode? ", "default", "mark")
                    sprint("I guess everyone starts from somewhere...\n", "default", "period")
                elif value == 3:
                    # Aww easy mode? You could do better than that NAME!
                    sprint("Aww easy mode? ", "default", "mark")
                    sprint("You could do better than that " + name + "!\n", "default", "mark")
                elif value == 4:
                    # Choosing easy mode I see... Let's see how you go!
                    sprint("Choosing easy mode I see... ", "default", "period")
                    sprint("Let's see how you go!\n", "default", "mark")
                elif value == 5:
                    # Easy come easy go... Let's go!
                    sprint("Easy come easy go... ", "default", "period")
                    sprint("Let's go!\n", "default", "mark")
                break
            elif difficulty in medium:  # If user selects "medium", print random message.
                if value == 1:
                    # So you're one of those average players NAME... Let's see how you go!
                    sprint("So you're one of those average players " + name + "... ", "default", "period")
                    sprint("Let's see how you go!\n", "default", "mark")
                elif value == 2:
                    # You've made a good choice! Let's begin!
                    sprint("You've made a good choice! ", "default", "mark")
                    sprint("Let's begin!\n", "default", "mark")
                elif value == 3:
                    # Medium, not too hard, not too easy. Let's go!
                    sprint("Medium, ", "default", "comma")
                    sprint("not too hard, ", "default", "comma")
                    sprint("not too easy. ", "default", "period")
                    sprint("Let's go!\n", "default", "mark")
                elif value == 4:
                    # Medium mode... I don't really have anything to say... Let's just start shall we?
                    sprint("Medium mode... ", "slow", "period")
                    sprint("I don't really have anything to say... ", "default", "period")
                    sprint("Let's just start shall we?\n", "default", "mark")
                elif value == 5:
                    # At least you didn't choose easy mode! Let's go!
                    sprint("At least you didn't choose easy mode! ", "default", "mark")
                    sprint("Let's go!\n", "default", "mark")
                break
            elif difficulty in hard:  # If user selects "hard", print random message.
                if value == 1:
                    # Going for hard mode NAME... You must be really good at arithmetic!
                    sprint("Going for hard mode " + name + "...", "default", "period")
                    sprint("You must be really good at arithmetic!\n", "default", "mark")
                if value == 2:
                    # Hard mode here we come!
                    sprint("Hard mode here we come!\n", "default", "mark")
                if value == 3:
                    # Not easy, not medium, but hard. I like it! Let's go!
                    sprint("Not easy, ", "default", "comma")
                    sprint("not medium, ", "default", "comma")
                    sprint("but hard. ", "default", "period")
                    sprint("I like it! ", "default", "mark")
                    sprint("Let's go!\n", "default", "mark")
                if value == 4:
                    # If you think about it, anything hard is easy if you know how to do it!
                    sprint("If you think about it, ", "default", "comma")
                    sprint("anything hard is easy if you know how to do it!\n", "default", "mark")
                if value == 5:
                    # Ha ha ha hard! That was bad wasn't it? Let's just begin...
                    sprint("Ha ha ha hard! ", "slow", "mark")
                    sprint("That was bad wasn't it? ", "default", "mark")
                    sprint("Let's just begin...\n", "default", "period")
                break
            else:
                if value == 1:
                    # There is only three difficulties to choose from...
                    sprint("There is only three difficulties to choose from...\n", "default", "period")
                elif value == 2:
                    # You didn't type a difficulty!
                    sprint("You didn't type a difficulty!\n", "default", "mark")
                elif value == 3:
                    # Is it so difficult to choose a difficulty?
                    sprint("Is it so difficult to choose a difficulty?\n", "default", "mark")
                elif value == 4:
                    # I've listed the difficulties for you! All you need to do is choose one!
                    sprint("I've listed the difficulties for you! ", "default", "mark")
                    sprint("All you need to do is choose one!\n", "default", "mark")
                elif value == 5:
                    sprint("I feel like you're purposely typing it wrong... ", "default", "period")
                    sprint("Or is that just me?\n", "default", "mark")
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

            table_answer = table1 * table2
            print(table1, "x", table2, "=")
            user_answer = input("Answer: ")
            while not user_answer.isdigit():
                value = randint(1, 5)
                if value == 1:
                    # Hey that's not a number!
                    sprint("Hey that's not a number!\n", "default", "mark")
                elif value == 2:
                    # I don't think that's a number...
                    sprint("I don't think that's a number...\n", "default", "period")
                elif value == 3:
                    # It has to be a number!
                    sprint("It has to be a number!\n", "default", "mark")
                elif value == 4:
                    # This times tables will never have letters as an answer...
                    sprint("This times tables will never have letters as an answer...\n", "default", "period")
                elif value == 5:
                    # I shouldn't have to say what you typed wrong with your answer...
                    sprint("I shouldn't have to say what you typed wrong with your answer...\n", "default", "period")
                user_answer = input("Answer: ")
            user_answer = int(user_answer)
            if user_answer == table_answer:
                print(random.choice(answercorrect))
                correct += 1
            elif user_answer != table_answer:
                print(random.choice(answerincorrect))
                incorrect += 1
                print("The right answer is", table_answer)
            else:
                sprint("I think you broke something...", "default", "period")
            rounds -= 1  # Minus one from the rounds the user has asked to play
        sprint("You got it correct " + correct + " time(s)! ", "default", "mark")
        sprint("You got it wrong " + incorrect + " time(s)!\n", "default", "mark")
        sprint("Do you want to play again? (Yes / No)", "default", "input")
        play_again = input("> ")
        while True:
            play_again = play_again.lower()
            if play_again in yesagain:
                correct = 0
                incorrect = 0
                playing = "y"
                # If user plays again, reset correct and incorrect
                break
            elif play_again in noagain:
                playing = "n"
                sprint("Do you want to go back to the main menu? (Yes / No)\n", "default", "input")
                main_menu = input("> ")
                while True:
                    main_menu = main_menu.lower()
                    if main_menu in yesagain:
                        return "yes"
                        break
                    elif main_menu in noagain:
                        return "no"
                        break
                    else:
                        print("Invalid option.")
                        main_menu = input("> ")
            else:
                sprint("Wait... ", "default", "period")
                sprint("So do you want to play again?\n", "default", "mark")
                play_again = input("> ")
