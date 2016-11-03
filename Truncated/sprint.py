import sys
from time import sleep as s


def sprint(text, speed, delay):  # Print out text with a custom speed
    for c in text:
        print(c, end=""),
        sys.stdout.flush()
        if speed == "default":  # Normal printing speed
            s(0.035)
        elif speed == "slow":  # Slow printing speed
            s(0.05)
        elif speed == "slower":  # Slower printing speed
            s(0.06)
        elif speed == "fastest":  # Fastest printing speed
            s(0.02)
        elif speed == "faster":  # Faster printing speed
            s(0.03)
    if delay == "comma":  # If the last punctuation is a comma (,)
        s(0.45)
    elif delay == "period":  # If the last punctuation is a period (.)
        s(1)
    elif delay == "quote":  # If the last punctuation is quotes ("")
        s(0.1)
    elif delay == "colon":  # If the last punctuation is a colon (:)
        s(0.3)
    elif delay == "list":  # If the last punctuation is a list of something
        s(0.05)
    elif delay == "mark":  # If the last punctuation is a punctuation mark (! ?)
        s(0.5)
    elif delay == "input":  # If the next code asks for an input
        s(0.05)