"""
File: PotholeFilling.py
Name: Grace
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *


def main():
    """
    Pre-condition:Karel is at the(2,1)
    Post-condition:Karel is at the(2,7),and (1,2)&(1,4)&(1,6) are filled with 99 beepers
    """
    for i in range(3):
        go_in()
        put_99_beepers()
        go_out()


def go_in():
    """
    Pre-condition:Karel is at the upper left,facing East
    Past-condition:Karel is in the pothole,facing South
    """
    move()
    turn_right()
    move()


def go_out():
    """
    Pre-condition:Karel is in the pothole,facing South
    Past-condition:Karel is at the upper left,facing East
    """
    turn_left()
    turn_left()
    move()
    turn_right()
    move()


def turn_right():
    for i in range(3):
        turn_left()


def put_99_beepers():
    """
    Karel will put 99 beepers
    """
    for i in range(99):
        put_beeper()


# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
