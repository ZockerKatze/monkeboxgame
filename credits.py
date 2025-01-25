import pyfiglet
import os
from colorama import *
import time


def creds():
    tester = ["Jeremias","Eli","Marian","Niklas"]
    idea = ["Neuralink"]
    writers = ["Rattatwinko"]

    colors = [Fore.RED,Fore.YELLOW,Fore.GREEN,Fore.CYAN,Fore.BLUE,Fore.MAGENTA]

    for i,c in zip(tester,colors):
        nn = pyfiglet.figlet_format("--Testers!--")
        os.system("clear" if os.name != "nt" else "cls")
        f = pyfiglet.figlet_format(i);

        print(f"{nn}")

        print(f"\n{c + f}")
        time.sleep(2)
        os.system("clear" if os.name != "nt" else "cls")


    for i,c in zip(idea,colors):
        nw = pyfiglet.figlet_format("--Idea!--")
        os.system("clear" if os.name != "nt" else "cls")
        f = pyfiglet.figlet_format(i)
        print(nw)
        print(f"{c + f}")
        time.sleep(2)
        os.system("clear" if os.name != "nt" else "cls")

    for i,c in zip(writers,colors):
        ne = pyfiglet.figlet_format("--Writers!--")
        f = pyfiglet.figlet_format(i)
        os.system("clear"if os.name != "nt" else "cls")
        print(ne)
        print(f"{c+f}")
        time.sleep(2)
        os.system("clear"if os.name != "nt" else "cls") ## checks for Linux "clear" and Windows "cls"

