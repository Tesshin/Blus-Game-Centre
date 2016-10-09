from graphics import *

<<<<<<< HEAD
from time import sleep
import sys


def print_slowly(text):
    for c in text:
        print(c, end=""),
        sys.stdout.flush()
        sleep(0.5)

print_slowly('LOADING')

window = GraphWin("Arithmetic", 750, 750)
window.getMouse()  # Pause to view result
window.close()
print("\n\nProcess finshed with exit code 1 then")


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(bcolors.WARNING + "Warning: No active frommets remain. Continue?" + bcolors.ENDC)
=======
window = GraphWin("Arithmetic", 750, 750)
window.getMouse() # Pause to view result
window.close()
print("\n\nProcess finshed with exit code 1 then")
>>>>>>> 4827ce23c4623b26f9242f8a422e7d85ccaa9a42
