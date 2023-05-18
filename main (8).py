# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: Kaleb Espinoza
# Creation Date: 05/14/2023
# Below is a simple program with several.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
    print("You are in a land full of dragons. In front of you, you see two caves. 3In one cave, the dragon is friendly and will share his treasure with you. The other dragon is greedy and hungry, and will eat you on sight.")


def chooseCave(): 
    cave = ''
  #There was a simple indentation error. Just fixed it by backspacing. 
    while cave !='1' and cave !='2':
        print("Which cave will you go into? (1 or 2 )") 
        cave = input()
    return cave

def checkCave (chosenCave):
    print('You approach the cave...') 
    #sleep for 2 seconds
    time.sleep (2)
    print("It is dark and spooky---")
    #sleep for 2 seconds
    time.sleep(3)
    print("A large dragon jumps out in front of you! He opens his jaws and...") 
    print() 
    #sleep for 2 seconds
    time.sleep(2) 
    friendlyCave= random.randint(1, 2)
    if chosenCave == str(friendlyCave):
        print('Gives you his treasure!')
    else:
        print ("Gobbles you down in one bite")
#Assignment operators needed to create a loop. 
playAgain = 'yes'

while playAgain == "yes" or playAgain=="y":

    displayIntro()
  #The function name (chooseCave) was incorrect. The "C" in cave needs to be capitalized. 
    caveNumber= chooseCave()
    checkCave(caveNumber)
  #Add the operators 
    print("Do you want to play again? (yes or no)")
    playAgain =input()
    if playAgain== "no":
        print("Thanks for playing")