from colorama import Fore, Back, Style
from colorama import init
from termcolor import colored

import os
import ctypes
from ctypes import wintypes
import msvcrt
import subprocess

from num2words import num2words

ctypes.windll.kernel32.SetConsoleTitleW("QWERTY Encryption - Jam - 2022")
os.system('mode con: cols=100 lines=40')
kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
user32 = ctypes.WinDLL('user32', use_last_error=True)

SW_MAXIMIZE = 3

kernel32.GetConsoleWindow.restype = wintypes.HWND
kernel32.GetLargestConsoleWindowSize.restype = wintypes._COORD
kernel32.GetLargestConsoleWindowSize.argtypes = (wintypes.HANDLE,)
user32.ShowWindow.argtypes = (wintypes.HWND, ctypes.c_int)

def maximize_console(lines=None):
    fd = os.open('CONOUT$', os.O_RDWR)
    try:
        hCon = msvcrt.get_osfhandle(fd)
        max_size = kernel32.GetLargestConsoleWindowSize(hCon)
        if max_size.X == 0 and max_size.Y == 0:
            raise ctypes.WinError(ctypes.get_last_error())
    finally:
        os.close(fd)
    cols = max_size.X
    hWnd = kernel32.GetConsoleWindow()
    if cols and hWnd:
        if lines is None:
            lines = max_size.Y
        else:
            lines = max(min(lines, 9999), max_size.Y)
        subprocess.check_call('mode.com con cols={} lines={}'.format(
                                cols, lines))
        user32.ShowWindow(hWnd, SW_MAXIMIZE)

maximize_console(lines=None)

init(autoreset=True)

global r
global g
global b
global w
global y
global c
global m
global bl

r = Fore.RED
g = Fore.GREEN
b = Fore.BLUE
w = Fore.WHITE
y = Fore.YELLOW
c = Fore.CYAN
m = Fore.MAGENTA
bl = Fore.BLACK

global rbg
global gbg
global bbg
global wbg
global ybg
global cbg
global mbg

rbg = Back.RED
gbg = Back.GREEN
bbg = Back.BLUE
wbg = Back.WHITE
ybg = Back.YELLOW
cbg = Back.CYAN
mbg = Back.MAGENTA

global bright
global dim

bright = Style.BRIGHT
dim = Style.DIM

def p(t, color):
    text = color + t
    return text

def bg(t, color):
    text = color + t
    return text

def sty(t, level):
    text = level + t
    return text

def find_qwerty_value(letter):
    
    if letter == "A":
        return "Q"
    elif letter == "a":
        return "q"
    
    elif letter == "B":
        return "W"
    elif letter == "b":
        return "w"

    elif letter == "C":
        return "E"
    elif letter == "c":
        return "e"

    elif letter == "D":
        return "R"
    elif letter == "d":
        return "r"

    elif letter == "E":
        return "T"
    elif letter == "e":
        return "t"

    elif letter == "F":
        return "Y"
    elif letter == "f":
        return "y"

    elif letter == "G":
        return "U"
    elif letter == "g":
        return "u"

    elif letter == "H":
        return "I"
    elif letter == "h":
        return "i"

    elif letter == "I":
        return "O"
    elif letter == "i":
        return "o"

    elif letter == "J":
        return "P"
    elif letter == "j":
        return "p"

    elif letter == "K":
        return "A"
    elif letter == "k":
        return "a"

    elif letter == "L":
        return "S"
    elif letter == "l":
        return "s"

    elif letter == "M":
        return "D"
    elif letter == "m":
        return "d"

    elif letter == "N":
        return "F"
    elif letter == "n":
        return "f"

    elif letter == "O":
        return "G"
    elif letter == "o":
        return "g"

    elif letter == "P":
        return "H"
    elif letter == "p":
        return "h"

    elif letter == "Q":
        return "J"
    elif letter == "q":
        return "j"

    elif letter == "R":
        return "K"
    elif letter == "r":
        return "k"

    elif letter == "S":
        return "L"
    elif letter == "s":
        return "l"

    elif letter == "T":
        return "Z"
    elif letter == "t":
        return "z"

    elif letter == "U":
        return "X"
    elif letter == "u":
        return "x"

    elif letter == "V":
        return "C"
    elif letter == "v":
        return "c"

    elif letter == "W":
        return "V"
    elif letter == "w":
        return "v"

    elif letter == "X":
        return "B"
    elif letter == "x":
        return "b"

    elif letter == "Y":
        return "N"
    elif letter == "y":
        return "n"

    elif letter == "Z":
        return "M"
    elif letter == "z":
        return "m"
    
    else:
        return letter
    

def encrypt(phrase):

    new_phrase = ""

    for i in range(len(phrase)):
        
        letter = phrase[i]

        letter_value = find_qwerty_value(letter)

        new_phrase += letter_value

    print(p(" Enrypted: ", g) + fix + "| " + new_phrase)

fix = '\033[0m'

print("")
print(sty(p(" QWERTY Encryption | by Jam | 2022", g), bright))
print("")

def main():

    up = True

    while up:
        print("------------------------------------------------------------------------------------------------")
        phrase = input(p(" Phrase:   ", c) + fix + "| ")
        encrypt(phrase)

main()
