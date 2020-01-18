import art
import os
from time import sleep

#Ryan Dalton - SWDV640 - Week 1
#Simple program to run text art of a user name and also
#allow the user to play a simple text game found on pypi.org

#Links to python modules
#art - https://pypi.org/project/art/ - displays user's name in fancy art
#python-wars-solo - https://pypi.org/project/python-wars-solo/ - simple text game that is fun to play and is launched via shell command with os


username = input("Enter your first name: ")
print("Hello....")
sleep(.5)
newName = username + "!"

Art = art.text2art(newName)
print(Art)

userChoice = input("Commander {}, do you want to play Python Wars? (y/n): ".format(username))

userChoice.lower()

while userChoice != "y" or userChoice != "n":
    if userChoice == "y":
        os.system("pythonwarsolo")
    elif userChoice == "n":
        print("k, bye!")
        break
    else:
        userChoice = input("Commander {}, do you want to play Python Wars? (y/n): ".format(username))
    
"""

while choice != "N" or choice != "n":
    choice = ("Hello Captain {}.  Do you want to play Python-Wars? (Y/N): ".format(username))
    if choice == "y" or choice == "Y":
        pythonwarsolo
        exit()
"""
