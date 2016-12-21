#!/usr/bin/python
# Basic game in Python

import random
import time

rock = 1
paper = 2
scissors = 3

name = { rock: "Rock", paper: "Paper", scissors: "Scissors"}

rules = { rock: scissors, paper: rock, scissors: paper}

player_points = 0

npc_points = 0 

def start():
    print (r"""
            ------------------------------------------------------------------
              _______  _______  _______  _       
             (  ____ )(  ___  )(  ____ \| \    /\
             | (    )|| (   ) || (    \/|  \  / /
             | (____)|| |   | || |      |  (_/ / 
             |     __)| |   | || |      |   _ (  
             | (\ (   | |   | || |      |  ( \ \ 
             | ) \ \__| (___) || (____/\|  /  \ \
             |/   \__/(_______)(_______/|_/    \/
                                                                     
              _______  _______  _______  _______  _______ 
             (  ____ )(  ___  )(  ____ )(  ____ \(  ____ )
             | (    )|| (   ) || (    )|| (    \/| (    )|
             | (____)|| (___) || (____)|| (__    | (____)|
             |  _____)|  ___  ||  _____)|  __)   |     __)
             | (      | (   ) || (      | (      | (\ (   
             | )      | )   ( || )      | (____/\| ) \ \__
             |/       |/     \||/       (_______/|/   \__/
                                                                                               
               _______  _______ _________ _______  _______  _______  _______ 
              (  ____ \(  ____ \\__   __/(  ____ \(  ____ \(  ___  )(  ____ )
              | (    \/| (    \/   ) (   | (    \/| (    \/| (   ) || (    )|
              | (_____ | |         | |   | (_____ | (_____ | |   | || (____)|
              (_____  )| |         | |   (_____  )(_____  )| |   | ||     __)
                    ) || |         | |         ) |      ) || |   | || (\ (   
              /\____) || (____/\___) (___/\____) |/\____) || (___) || ) \ \__
              \_______)(_______/\_______/\_______)\_______)(_______)|/   \__/
           
            ---------------------------------------------------------------------
            """)
    while rps_game():
        pass
    scores()


def rps_game():
    player = turns()
    computer = random.randint(1, 3)
    result(player, computer)
    return play_again()

def turns():
    while True:
        print()
        player = raw_input("Rock = 1 \nPaper = 2 \nScissors = 3\n Pick onei\n: ")
        try:
            player = int(player)
            if player in (1, 2, 3):
                return player
        except ValueError:
            pass
        print ("Please choose a correct number")

def result(player, npc):
    print("number 1 !!!")
    time.sleep(1)
    print("number 2 !!!")
    time.sleep(1)
    print("number 3 !!!")
    time.sleep(0.5)
    print("NPC throw a {0}".format(name[npc]))
    global player_points, npc_points
    if player == npc:
        print("tie score")
    else:
        if rules[player] == npc:
            print("scored!!!!")
            player_points += 1
        else:
            print("NPC scored !!!" )
            npc_points += 1

def play_again():
    try_again = input("would you like to try again ??? \n: ")
    if try_again in ("y","Y","Yes","yes"):
        return try_again
    else:
        print("Thank you for playing :)")


def scores():
    global player_points, npc_points
    print ("Winning scores")
    print ("Player: ", player_points)
    print ("Computer:  ", npc_points)


if __name__ == '__main__':
    start()
