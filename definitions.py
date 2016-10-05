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


def sprint(text, speed, delay):
    for c in text:
        print(c, end=""),
        sys.stdout.flush()
        sleep(speed)
    sleep(delay)