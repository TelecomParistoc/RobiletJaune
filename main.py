#!/usr/bin/env python
import init_and_LED

import motion                           #from libmotors
from starting_block import add_jack_and_delay, time_elapsed, manage_time_elapsed
# the robot is "constructed" in structure_Grobot.py
from structure_Grobot import *

from time import sleep

STARTING_POINT = None #set in init_color()
STARTING_HEADING = None

PATHS_FOLDER = "/home/pi/GrobotControl/paths/"

def init_color(robot):
    global STARTING_POINT, STARTING_HEADING
    robot.color = get_team_color()
    if(robot.color == "orange"):
        print "robot is orange: ", STARTING_POINT
        STARTING_POINT = [51, 223]

        STARTING_HEADING = 180
    else:
        STARTING_POINT = [2949, 223]
        STARTING_HEADING = 0


########################  JACK MANAGEMENT ####################

# delay = 10 = maximum time the robot waits before aborting
manage_jack = add_jack_and_delay(robot, 6666)

init_and_LED.turn_orange_on()
gpio.assign_callback_on_gpio_down(jack_pin_bcm, lambda: (manage_jack(False),
                                                init_and_LED.turn_green_on()))
gpio.assign_callback_on_gpio_up(jack_pin_bcm, lambda: manage_jack(True))

robot.wait_sequence() # We wait for jack beeing pushed/pulled


############################ TOP LEVEL ACTION DEFINITION #######################
# remainder: definition != execution

def log(message):
    print message

while(True):
    sleep(1000);
    robot.move(10);
    sleep(1000);
    robot.move(-10);

