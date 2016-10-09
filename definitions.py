import sys
from time import sleep

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
        if speed == "super":
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