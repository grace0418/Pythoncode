"""
File: Steeplechase.py
Name: Grace
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
    #Karel is facing East
        if front_is_clear():
            move()
        else:
            jump()


def jump():
    """
    Pre-condition:Karel is on the left side of the wall,facing East
    Post-condition:Karel is on the right side of the wall,facing East
    """
    up()
    cross()
    down()


def cross():
    """
    Pre-condition:Karel is facing North
    Post-condition:Karel is at the upper right,facing South
    """
    turn_right()
    move()
    turn_right()


def up():
    """
    Pre-condition:Karel is on the left side of the wall,facing East
    Post-condition:Karel is facing North
    """
    turn_left()
    #Facing North
    while not right_is_clear():
        move()

    """
    while not front_is_clear():
        turn_left()
        move()
        turn_right()
    """


def down():
    """
    Pre-condition:Karel is at the upper right,facing South
    Post-condition:Karel is on the right side of the wall,facing East
    """
    while front_is_clear():
        move()
    turn_left()


def turn_right():
    for i in range(3):
        turn_left()

# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
