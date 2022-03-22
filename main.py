import os
import sys
import platform
import numpy
import threading
import ctypes
import string
import random
import requests
import json
from colorama import Fore

VALID = 0

INVALID = 0

BOOST_LENGTH = 24

CLASSIC_LENGTH = 16

CODESET = []

BASEURL = "https://discord.gift/"

CODESET[:0] = string.ascii_letters + string.digits


ctypes.windll.kernel32.SetConsoleTitleW(f"NoirGen and Checker | Valid: 0 | Invalid: 0")
os.system("cls")

NOIRGEN = """[40;35m
                                                                                                [40;34mv 1.0.0[40;35m
                             /$$   /$$           /$$            /$$$$$$                     
                            | $$$ | $$          |__/           /$$__  $$                    
                            | $$$$| $$  /$$$$$$  /$$  /$$$$$$ | $$  \__/  /$$$$$$  /$$$$$$$ 
                            | $$ $$ $$ /$$__  $$| $$ /$$__  $$| $$ /$$$$ /$$__  $$| $$__  $$
                            | $$  $$$$| $$  \ $$| $$| $$  \__/| $$|_  $$| $$$$$$$$| $$  \ $$
                            | $$\  $$$| $$  | $$| $$| $$      | $$  \ $$| $$_____/| $$  | $$
                            | $$ \  $$|  $$$$$$/| $$| $$      |  $$$$$$/|  $$$$$$$| $$  | $$
                            |__/  \__/ \______/ |__/|__/       \______/  \_______/|__/  |__/
                                                                                        
"""



print(NOIRGEN)

for i in range(3):
    print('')

CODE_AMOUNT = int(input("                                               [40;36mCodes to Generate =>  "))

for i in range(2):
    print('')

BOOST_CLASSIC = str(input("                                               [40;32mBoost or Classic => "))

for i in range(2):
    print('')

THREAD_COUNT = int(input("                                                   [40;31mThreads => "))

for i in range(5):
    print('')


def checkBoost(boostURL):

    global VALID

    global INVALID

    CHECKURL = f"https://discordapp.com/api/v9/entitlements/gift-codes/{boostURL}?with_application=false&with_subscription_plan=true"

    resp = requests.get(CHECKURL)

    if resp.status_code == 200:

        VALID += 1

        return True

    else:
        INVALID += 1

        return False 


def genBoost():
    global VALID

    global INVALID


    for i in range(CODE_AMOUNT):

        code = numpy.random.choice(CODESET, size=[CODE_AMOUNT, BOOST_LENGTH])

        for i in code:
            try: 
                boostCode = ''.join(e for e in i)

                boostURL = BASEURL + boostCode 

                if checkBoost(boostURL):

                    with open("valid.txt", "w") as f:

                        f.write(boostURL + "\n")

                    print(Fore.GREEN + f"[!] VALID |  {boostURL}")

                    ctypes.windll.kernel32.SetConsoleTitleW(f"NoirGen and Checker | Valid: {VALID} | Invalid: {INVALID}")

                else:
                    ctypes.windll.kernel32.SetConsoleTitleW(f"NoirGen and Checker | Valid: {VALID} | Invalid: {INVALID}")

                    print(Fore.RED + f"[!] INVALID |  {boostURL}")

            except Exception as e:
                print(e)

                print(Fore.RED + "[!] An Error has Occured!")


def checkClassic(classicURL):

    global VALID

    global INVALID

    CHECKURL = f"https://discordapp.com/api/v9/entitlements/gift-codes/{classicURL}?with_application=false&with_subscription_plan=true"

    resp = requests.get(CHECKURL)

    if resp.status_code == 200:

        VALID += 1

        return True

    else:
        INVALID += 1

        return False 


def genClassic():
    global VALID

    global INVALID


    for i in range(CODE_AMOUNT):

        code = numpy.random.choice(CODESET, size=[CODE_AMOUNT, CLASSIC_LENGTH])

        for i in code:
            try: 
                classicCode = ''.join(e for e in i)

                classicURL = BASEURL + classicCode 

                if checkClassic(classicURL):

                    with open("valid.txt", "w") as f:

                        f.write(classicURL + "\n")

                    print(Fore.GREEN + f"[!] VALID |  {classicURL}")

                    ctypes.windll.kernel32.SetConsoleTitleW(f"NoirGen and Checker | Valid: {VALID} | Invalid: {INVALID}")

                else:
                    ctypes.windll.kernel32.SetConsoleTitleW(f"NoirGen and Checker | Valid: {VALID} | Invalid: {INVALID}")

                    print(Fore.RED + f"[!] INVALID |  {classicURL}")

            except Exception as e:
                print(e)

                print(Fore.RED + "[!] An Error has Occured!")


if BOOST_CLASSIC == "Boost" or "B" or "b" or "boost":
    for i in range(THREAD_COUNT):
        threading.Thread(target=genBoost).start()
elif BOOST_CLASSIC == "Classic" or "C" or "c" or "classic":
    for i in range(THREAD_COUNT):
        threading.Thread(target=genClassic).start()

                
