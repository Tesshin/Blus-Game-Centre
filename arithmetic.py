# Blu's Game Centre - Arithmetic v1.0
# Aiyurn © 2016

import random
import time

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
easy = ["e", "ea", "eas","easy"]
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


def arithmetic():
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
                time.sleep(3)
                # If user selects "easy", print random message and pause for 3 seconds
                break
            elif difficulty in medium:
                print(random.choice(mediummsg))
                time.sleep(3)
                # If user selects "medium", print random message and pause for 3 seconds
                break
            elif difficulty in hard:
                print(random.choice(hardmsg))
                time.sleep(3)
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